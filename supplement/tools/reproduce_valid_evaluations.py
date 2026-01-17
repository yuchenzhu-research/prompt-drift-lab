#!/usr/bin/env python3
"""AUTHORITATIVE REPRODUCTION SCRIPT (JSON-ONLY)

Purpose
- Read stored judge JSON bundles under:
    supplement/04_results/02_raw_judge_evaluations/
      - diagnostic/v0_baseline_judge/
      - final/v1_paraphrase_judge/
      - final/v2_schema_strict_judge/
- Materialize processed artifacts under:
    supplement/04_results/03_processed_evaluations/<judge_version>/
      - valid_evaluations/**/record_*.json
      - summary_tables/scores_long.csv
      - summary_tables/scores_grouped.csv
      - summary_tables/excluded_records.jsonl (only if needed)

Hard constraints
- No PDF parsing.
- No placeholder self-evaluation.
- Consume stored judge JSON artifacts only.
- Deterministic: identical inputs produce identical outputs.

Validity / exclusion note
- Ingestion requires per-file entries to contain schema-aligned keys `file` and `scores`.
- Entries that use `file_name` instead of the schema-defined `file` are treated as invalid for ingestion,
  recorded to `summary_tables/excluded_records.jsonl`, and excluded from aggregation.
- This behavior is intentional and contract-aligned (see supplement/03_evaluation_rules/).

Notes
- Judge / generator model identifiers are parsed from the bundle file name when present
  (judge_<judge>_bundle_<generator>.json). If not matched, identifiers are set to "unknown".
- File labels are preserved verbatim as identifiers; any file-name parsing is used only to
  materialize grouping keys and does not affect score computation.
"""

import json
import os
from pathlib import Path
from typing import Dict, Any, Iterable, List

import csv

# -----------------------------
# Paths (relative to repo root)
# -----------------------------
ROOT = Path(__file__).resolve().parents[2]
RAW_ROOT = ROOT / "supplement" / "04_results" / "02_raw_judge_evaluations"
OUT_ROOT = ROOT / "supplement" / "04_results" / "03_processed_evaluations"

# -----------------------------
# Utilities
# -----------------------------

def iter_json_files(base: Path) -> Iterable[Path]:
    for p in base.rglob("*.json"):
        if p.is_file():
            yield p


def load_json(path: Path) -> Any:
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


# -----------------------------
# Core processing
# -----------------------------

def process_bundle(bundle_path: Path) -> Dict[str, Any]:
    data = load_json(bundle_path)

    bundle_meta = data.get("bundle_meta", {})
    per_file_scores = data.get("per_file_scores", [])

    valid_records: List[Dict[str, Any]] = []
    excluded: List[Dict[str, Any]] = []

    for item in per_file_scores:
        file_label = item.get("file")  # NOTE: `file_name` is not accepted; such items are logged to excluded_records.jsonl
        scores = item.get("scores")

        if not file_label or not scores:
            excluded.append({
                "bundle": bundle_path.name,
                "reason": "bad_item: missing file or scores",
                "item": item,
            })
            continue

        record = {
            "bundle": bundle_path.name,
            "bundle_meta": bundle_meta,
            "file": file_label,
            "scores": scores,
            "total": item.get("total"),
            "evidence": item.get("evidence"),
        }
        valid_records.append(record)

    return {
        "valid": valid_records,
        "excluded": excluded,
    }


# -----------------------------
# Aggregation
# -----------------------------

def aggregate(valid_records: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    rows: List[Dict[str, Any]] = []
    for r in valid_records:
        row = {
            "bundle": r.get("bundle"),
            "file": r.get("file"),
        }
        scores = r.get("scores", {})
        for k, v in scores.items():
            row[k] = v
        rows.append(row)
    return rows


def write_csv(path: Path, rows: List[Dict[str, Any]]):
    if not rows:
        return
    path.parent.mkdir(parents=True, exist_ok=True)
    with open(path, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
        writer.writeheader()
        for r in rows:
            writer.writerow(r)


# -----------------------------
# Main
# -----------------------------

def main():
    OUT_ROOT.mkdir(parents=True, exist_ok=True)

    all_valid: List[Dict[str, Any]] = []
    all_excluded: List[Dict[str, Any]] = []

    for bundle_path in iter_json_files(RAW_ROOT):
        result = process_bundle(bundle_path)
        all_valid.extend(result["valid"])
        all_excluded.extend(result["excluded"])

    # Write aggregated tables
    rows = aggregate(all_valid)
    write_csv(OUT_ROOT / "scores_long.csv", rows)

    # Write excluded records if any
    if all_excluded:
        excl_path = OUT_ROOT / "excluded_records.jsonl"
        excl_path.parent.mkdir(parents=True, exist_ok=True)
        with open(excl_path, "w", encoding="utf-8") as f:
            for item in all_excluded:
                f.write(json.dumps(item, ensure_ascii=False) + "\n")


if __name__ == "__main__":
    main()