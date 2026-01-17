#!/usr/bin/env python3
"""AUTHORITATIVE REPRODUCTION SCRIPT (JSON-only)

Purpose
- Read stored judge JSON bundles under:
    supplement/04_results/02_raw_judge_evaluations/
      - diagnostic/v0_baseline_judge/
      - final/v1_paraphrase_judge/
      - final/v2_schema_strict_judge/
- Materialize processed artifacts under:
    supplement/04_results/03_processed_evaluations/<judge_version>/
      - valid_evaluations/main_method_cross_model/*.json
      - summary_tables/scores_long.csv
      - summary_tables/scores_grouped.csv
      - summary_tables/excluded_records.jsonl (only if needed)

Hard constraints
- No PDF parsing.
- No placeholder self-evaluation.
- Consume stored judge JSON bundles only.
- Output ordering is deterministic (explicit sorting; JSON keys are sorted).
- Treat `per_file_scores` as the lowest-common protocol.

Notes
- Judge / generator model identifiers are parsed from the bundle file name (stable artifact identifier):
    judge_<judge>_bundle_<generator>.json
  If not matched, set to "unknown".
"""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
import re
from collections import defaultdict
from pathlib import Path
from typing import Any, Dict, Iterable, List, Optional, Tuple


RUNS: Dict[str, Dict[str, str]] = {
    "v0_baseline_judge": {
        "in_rel": "supplement/04_results/02_raw_judge_evaluations/diagnostic/v0_baseline_judge",
        "out_rel": "supplement/04_results/03_processed_evaluations/v0_baseline_judge",
    },
    "v1_paraphrase_judge": {
        "in_rel": "supplement/04_results/02_raw_judge_evaluations/final/v1_paraphrase_judge",
        "out_rel": "supplement/04_results/03_processed_evaluations/v1_paraphrase_judge",
    },
    "v2_schema_strict_judge": {
        "in_rel": "supplement/04_results/02_raw_judge_evaluations/final/v2_schema_strict_judge",
        "out_rel": "supplement/04_results/03_processed_evaluations/v2_schema_strict_judge",
    },
}

SCORE_FIELDS = [
    "A_structure",
    "B_snapshot_constraint",
    "C_actionability",
    "D_completeness",
    "E_drift_failure",
]

# Deterministic CSV column order
LONG_FIELDS: List[str] = [
    "judge_version",
    "source_bundle",
    "judge_model",
    "generator_model",
    "file",
    "question_id",
    "prompt_variant",
    "trigger_type",
] + SCORE_FIELDS + ["total"]

GROUP_KEY_FIELDS: List[str] = ["judge_version", "generator_model", "question_id", "prompt_variant", "trigger_type"]
GROUPED_FIELDS: List[str] = GROUP_KEY_FIELDS + ["n"] + [f"{k}_mean" for k in (SCORE_FIELDS + ["total"])]



# -------------------------
# Small helpers
# -------------------------

def _load_json(path: Path) -> Dict[str, Any]:
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def _write_json(path: Path, obj: Dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        json.dump(obj, f, ensure_ascii=False, indent=2, sort_keys=True)


def _append_jsonl(path: Path, records: Iterable[Dict[str, Any]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        for r in records:
            f.write(json.dumps(r, ensure_ascii=False, sort_keys=True) + "\n")


def _sha12(s: str) -> str:
    return hashlib.sha256(s.encode("utf-8")).hexdigest()[:12]


def _infer_models_from_bundle_name(stem: str) -> Tuple[str, str]:
    """Best-effort parse: judge_<judge>_bundle_<generator>"""
    m = re.match(r"^judge_(?P<judge>.+?)_bundle_(?P<gen>.+?)$", stem)
    if not m:
        return "unknown", "unknown"
    return m.group("judge"), m.group("gen")


def _parse_file_label(file_label: str) -> Dict[str, Optional[str]]:
    """Identifier parsing for grouping only.

    This does not affect validity decisions or score computation; it only materializes
    stable grouping keys used by summary tables.

    Supported formats include:
    - q3_baseline_explicit.pdf
    - google_gemini-3-pro/q3_baseline_explicit.pdf
    - q3 baseline explicit.pdf

    Returns: question_id, prompt_variant, trigger_type
    """
    label = file_label
    base = label.split("/")[-1]  # drop possible model prefix
    if base.lower().endswith(".pdf"):
        base = base[:-4]

    # normalize separators
    norm = re.sub(r"[_\s]+", " ", base.strip())
    toks = norm.split(" ")

    q = next((t.lower() for t in toks if re.fullmatch(r"q\d+", t.lower())), None)

    # These vocabularies match your observed naming.
    variants = {"baseline", "conflict", "weak", "long"}
    triggers = {"explicit", "implicit"}

    v = next((t.lower() for t in toks if t.lower() in variants), None)
    tr = next((t.lower() for t in toks if t.lower() in triggers), None)

    return {"question_id": q, "prompt_variant": v, "trigger_type": tr}


def _mean(xs: List[Optional[float]]) -> Optional[float]:
    vals = [x for x in xs if isinstance(x, (int, float))]
    if not vals:
        return None
    return round(sum(vals) / len(vals), 6)


# -------------------------
# Core processing
# -------------------------

def process_run(repo_root: Path, run_name: str, overwrite: bool = False) -> None:
    cfg = RUNS[run_name]
    in_dir = repo_root / cfg["in_rel"]
    out_dir = repo_root / cfg["out_rel"]

    if not in_dir.exists():
        raise FileNotFoundError(f"Missing input directory: {in_dir}")

    valid_dir = out_dir / "valid_evaluations" / "main_method_cross_model"
    summary_dir = out_dir / "summary_tables"

    if overwrite:
        # Only remove generated files under our owned subtrees.
        for p in [valid_dir, summary_dir]:
            if p.exists():
                for x in p.rglob("*"):
                    if x.is_file():
                        x.unlink()

    valid_dir.mkdir(parents=True, exist_ok=True)
    summary_dir.mkdir(parents=True, exist_ok=True)

    # preserve run_meta if present
    run_meta_path = in_dir / "run_meta.json"
    if run_meta_path.exists():
        _write_json(summary_dir / "run_meta.json", _load_json(run_meta_path))

    rows_long: List[Dict[str, Any]] = []
    excluded: List[Dict[str, Any]] = []

    bundle_paths = sorted([p for p in in_dir.glob("*.json") if p.name != "run_meta.json"])

    for bundle_path in bundle_paths:
        try:
            bundle = _load_json(bundle_path)
        except Exception as e:
            excluded.append({"bundle": bundle_path.name, "reason": f"json_load_failed: {e}"})
            continue

        if "per_file_scores" not in bundle:
            excluded.append({"bundle": bundle_path.name, "reason": "missing_key: per_file_scores"})
            continue

        per_file = bundle.get("per_file_scores") or []
        if not isinstance(per_file, list):
            excluded.append({"bundle": bundle_path.name, "reason": "bad_type: per_file_scores not list"})
            continue

        judge_model, generator_model = _infer_models_from_bundle_name(bundle_path.stem)
        # keep bundle_meta for audit only
        bundle_meta = bundle.get("bundle_meta") if isinstance(bundle.get("bundle_meta"), dict) else {}

        for item in per_file:
            if not isinstance(item, dict):
                excluded.append({"bundle": bundle_path.name, "reason": "bad_item: not dict"})
                continue

            file_label = item.get("file")
            scores = item.get("scores") or {}
            total = item.get("total")
            evidence = item.get("evidence") or {}
            notes = item.get("notes")

            if not file_label or not isinstance(scores, dict):
                excluded.append({
                    "bundle": bundle_path.name,
                    "reason": "bad_item: missing file or scores",
                    "item": item,
                })
                continue

            parsed = _parse_file_label(str(file_label))

            # File name must be safe: never embed raw file_label (it may include '/').
            rid = _sha12(f"{bundle_path.name}::{file_label}")
            out_name = f"record_{rid}.json"

            record = {
                "judge_version": run_name,
                "method": "cross_model",
                "source_bundle": bundle_path.name,
                "bundle_meta": bundle_meta,
                "judge_model": judge_model,
                "generator_model": generator_model,
                "file": file_label,
                **parsed,
                "scores": scores,
                "total": total,
                "evidence": evidence,
                "notes": notes,
            }

            _write_json(valid_dir / out_name, record)

            row = {
                "judge_version": run_name,
                "source_bundle": bundle_path.name,
                "judge_model": judge_model,
                "generator_model": generator_model,
                "file": file_label,
                "question_id": parsed.get("question_id"),
                "prompt_variant": parsed.get("prompt_variant"),
                "trigger_type": parsed.get("trigger_type"),
            }
            for k in SCORE_FIELDS:
                row[k] = scores.get(k)
            row["total"] = total
            rows_long.append(row)

    # Write excluded records log (only if non-empty)
    if excluded:
        _append_jsonl(summary_dir / "excluded_records.jsonl", excluded)

    # If nothing collected, still succeed (empty run)
    if not rows_long:
        return

    # Deterministic ordering for outputs
    rows_long.sort(key=lambda r: (r.get("source_bundle", ""), str(r.get("file", ""))))

    # 1) Long table
    long_csv = summary_dir / "scores_long.csv"
    with open(long_csv, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=LONG_FIELDS)
        writer.writeheader()
        writer.writerows(rows_long)

    # 2) Grouped means: by generator_model + question_id + prompt_variant + trigger_type
    key_fields = GROUP_KEY_FIELDS
    grouped: Dict[Tuple[Any, ...], List[Dict[str, Any]]] = defaultdict(list)

    for r in rows_long:
        key = tuple(r.get(k) for k in key_fields)
        grouped[key].append(r)

    grouped_rows: List[Dict[str, Any]] = []
    for key, rs in grouped.items():
        out = dict(zip(key_fields, key))
        out["n"] = len(rs)
        for k in SCORE_FIELDS + ["total"]:
            out[f"{k}_mean"] = _mean([r.get(k) for r in rs])
        grouped_rows.append(out)

    grouped_rows.sort(key=lambda r: tuple(r.get(k) for k in key_fields))

    grouped_csv = summary_dir / "scores_grouped.csv"
    with open(grouped_csv, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=GROUPED_FIELDS)
        writer.writeheader()
        writer.writerows(grouped_rows)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--runs",
        nargs="*",
        default=["v0_baseline_judge", "v1_paraphrase_judge", "v2_schema_strict_judge"],
        choices=list(RUNS.keys()),
        help="Which judge versions to process",
    )
    parser.add_argument(
        "--overwrite",
        action="store_true",
        help="Delete previously generated files under 03_processed_evaluations/<run>/ before writing",
    )
    args = parser.parse_args()

    # supplement/tools/<this file> -> repo root is two parents up
    repo_root = Path(__file__).resolve().parents[2]

    for run_name in args.runs:
        print(f"[RUN] {run_name}")
        process_run(repo_root, run_name, overwrite=args.overwrite)

    print("✓ Finished")


if __name__ == "__main__":
    main()