#!/usr/bin/env python3
"""
compute_scores.py
=================

CANONICAL SCORING IMPLEMENTATION (AUTHORITATIVE)
-----------------------------------------------
This file defines the *only* authoritative logic for aggregating
judged evaluation results into summary scores scores.

Contract:
- Input:  a directory containing judged score files (JSON / JSONL)
- Output: a single CSV summary file

This script is intentionally self-contained and stable.
Other scripts (e.g., tools/reproduce_summary.sh) MUST call this file
and MUST NOT re-implement scoring logic.

Any modification to this file constitutes a change to the evaluation
protocol and MUST be versioned, documented, and reported.
"""

import argparse
import json
import os
import re
from dataclasses import dataclass
from pathlib import Path
from typing import Dict, List, Optional

import pandas as pd


# PDF filename pattern:
#   q3 baseline implicit.pdf / q4 long explicit.pdf
FILE_RE = re.compile(
    r"^(q[34])\s+(baseline|long|weak|conflict)\s+(implicit|explicit)\.pdf$",
    re.IGNORECASE,
)

# main_method judge JSON pattern:
#   judge_chatgpt_bundle_gemini_v2.json
JUDGE_RE = re.compile(r"^judge_(.+)_bundle_(.+)_v2\.json$", re.IGNORECASE)

DIM_KEYS = [
    "A_structure",
    "B_snapshot_constraint",
    "C_actionability",
    "D_completeness",
    "E_drift_failure",
]


@dataclass
class Validity:
    ok: bool
    reasons: List[str]


def load_json(path: Path) -> Dict:
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def parse_pdf_name(pdf_name: str) -> Dict[str, str]:
    m = FILE_RE.match(pdf_name.strip())
    if not m:
        return {"q": "", "version": "", "trigger": ""}
    return {
        "q": m.group(1).lower(),
        "version": m.group(2).lower(),
        "trigger": m.group(3).lower(),
    }


def validate_eval_json(obj: Dict, path: Path, strict: bool = True) -> Validity:
    """
    Validate a single evaluation JSON against structural constraints.
    This function does NOT assign scores; it only checks consistency.
    """
    reasons = []

    for k in ["bundle_meta", "per_file_scores"]:
        if k not in obj:
            reasons.append(f"missing_key:{k}")
    if reasons:
        return Validity(False, reasons)

    meta = obj["bundle_meta"]
    if "bundle_size" not in meta or meta["bundle_size"] != 16:
        reasons.append("bundle_meta.bundle_size_not_16")

    pfs = obj["per_file_scores"]
    if not isinstance(pfs, list) or len(pfs) != 16:
        reasons.append("per_file_scores_len_not_16")

    seen_files = set()
    for i, item in enumerate(pfs):
        if "file" not in item or "scores" not in item:
            reasons.append(f"per_file_scores[{i}]_missing_file_or_scores")
            continue

        fname = item["file"]
        if fname in seen_files:
            reasons.append(f"duplicate_file:{fname}")
        seen_files.add(fname)

        parsed = parse_pdf_name(fname)
        if strict and (not parsed["q"] or not parsed["version"] or not parsed["trigger"]):
            reasons.append(f"bad_filename:{fname}")

        scores = item["scores"]
        for dk in DIM_KEYS:
            if dk not in scores:
                reasons.append(f"missing_dim:{fname}:{dk}")
                continue
            v = scores[dk]
            if not isinstance(v, int) or v < 0 or v > 2:
                reasons.append(f"bad_dim_value:{fname}:{dk}={v}")

        calc_total = sum(
            int(scores.get(dk, 0))
            for dk in DIM_KEYS
            if isinstance(scores.get(dk, None), int)
        )
        if "total" in item:
            if item["total"] != calc_total:
                reasons.append(f"total_mismatch:{fname}:json={item['total']},calc={calc_total}")
        else:
            reasons.append(f"missing_total:{fname}")

        # Strict mode: if A_structure == 0, all other dimensions must be 0
        if strict and scores.get("A_structure", 0) == 0:
            others = [scores.get(k, 0) for k in DIM_KEYS[1:]]
            if any(v != 0 for v in others):
                reasons.append(f"A0_but_others_nonzero:{fname}:{others}")

    return Validity(len(reasons) == 0, reasons)


def eval_to_df(obj: Dict, judge: str, generator: str) -> pd.DataFrame:
    rows = []
    for item in obj["per_file_scores"]:
        fname = item["file"]
        parsed = parse_pdf_name(fname)
        scores = item["scores"]
        row = {
            "judge": judge.lower(),
            "generator": generator.lower(),
            "file": fname,
            "q": parsed["q"],
            "version": parsed["version"],
            "trigger": parsed["trigger"],
            **{k: scores.get(k, None) for k in DIM_KEYS},
            "total": item.get("total", None),
        }
        rows.append(row)
    return pd.DataFrame(rows)


def summarize_generator(df: pd.DataFrame) -> pd.DataFrame:
    """
    df may contain multiple judges per generator/file.
    First average across judges per (generator, file), then aggregate.
    """
    file_mean = (
        df.groupby(["generator", "file", "q", "version", "trigger"], as_index=False)
        .agg(total_mean=("total", "mean"))
    )

    def _avg(sub: pd.DataFrame) -> float:
        return float(sub["total_mean"].mean()) if len(sub) else float("nan")

    out_rows = []
    for gen, sub in file_mean.groupby("generator"):
        all_avg = _avg(sub)
        exp_avg = _avg(sub[sub["trigger"] == "explicit"])
        imp_avg = _avg(sub[sub["trigger"] == "implicit"])
        perfect = int((sub["total_mean"] == 10).sum())
        zero = int((sub["total_mean"] == 0).sum())
        out_rows.append(
            {
                "generator": gen,
                "avg_total": round(all_avg, 4),
                "explicit_avg": round(exp_avg, 4),
                "implicit_avg": round(imp_avg, 4),
                "zero_count(mean==0)": zero,
                "perfect_count(mean==10)": perfect,
                "n_files": int(len(sub)),
            }
        )
    return pd.DataFrame(out_rows).sort_values("generator")


def summarize_slices(df: pd.DataFrame, out_dir: Path, prefix: str) -> None:
    """
    Export mean scores by question, by version,
    and by question × version (after judge-level averaging).
    """
    file_mean = (
        df.groupby(["generator", "file", "q", "version", "trigger"], as_index=False)
        .agg(total_mean=("total", "mean"))
    )

    by_q = (
        file_mean.groupby(["generator", "q"], as_index=False)
        .agg(avg_total=("total_mean", "mean"))
    )
    by_v = (
        file_mean.groupby(["generator", "version"], as_index=False)
        .agg(avg_total=("total_mean", "mean"))
    )
    by_qv = (
        file_mean.groupby(["generator", "q", "version"], as_index=False)
        .agg(avg_total=("total_mean", "mean"))
    )

    by_q.to_csv(out_dir / f"{prefix}_by_question.csv", index=False, encoding="utf-8-sig")
    by_v.to_csv(out_dir / f"{prefix}_by_version.csv", index=False, encoding="utf-8-sig")
    by_qv.to_csv(out_dir / f"{prefix}_by_question_version.csv", index=False, encoding="utf-8-sig")


def inter_judge_agreement(df: pd.DataFrame) -> pd.DataFrame:
    """
    Compute MAE and exact-match counts between judges
    for the same generator and file.
    """
    piv = df.pivot_table(
        index=["generator", "file"], columns="judge", values="total", aggfunc="first"
    )
    judges = list(piv.columns)
    rows = []
    for a_i in range(len(judges)):
        for b_i in range(a_i + 1, len(judges)):
            a, b = judges[a_i], judges[b_i]
            pair = piv[[a, b]].dropna()
            if pair.empty:
                continue
            mae = float((pair[a] - pair[b]).abs().mean())
            exact = int((pair[a] == pair[b]).sum())
            n = int(len(pair))
            rows.append(
                {
                    "judge_a": a,
                    "judge_b": b,
                    "n": n,
                    "mae_total": round(mae, 4),
                    "exact_match": exact,
                }
            )
    if not rows:
        return pd.DataFrame(
            columns=["judge_a", "judge_b", "n", "mae_total", "exact_match"]
        )
    return pd.DataFrame(rows).sort_values(["judge_a", "judge_b"])


def _print_gen_summary(df: pd.DataFrame, title: str) -> None:
    print(f"\n=== {title} ===")
    if df.empty:
        print("(empty)")
        return

    trig = df["trigger"].astype(str).str.lower()
    by_gen = (
        df.groupby("generator")
        .agg(
            n=("total", "size"),
            avg_total=("total", "mean"),
            explicit_avg=(
                "total",
                lambda x: float(
                    x[trig.reindex(x.index, fill_value=False) == "explicit"].mean()
                )
                if (trig.reindex(x.index, fill_value=False) == "explicit").any()
                else float("nan"),
            ),
            implicit_avg=(
                "total",
                lambda x: float(
                    x[trig.reindex(x.index, fill_value=False) == "implicit"].mean()
                )
                if (trig.reindex(x.index, fill_value=False) == "implicit").any()
                else float("nan"),
            ),
            zero_count=("total", lambda x: int((x == 0).sum())),
            perfect_count=("total", lambda x: int((x == 10).sum())),
        )
        .reset_index()
    )
    print(by_gen.to_string(index=False))


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument(
        "--main_dir",
        required=True,
        help="Directory: valid_results/main_method (contains judge_*.json)",
    )
    ap.add_argument(
        "--support_dir",
        required=False,
        default="",
        help="Directory: valid_results/supporting_method (contains self_judge_*.json)",
    )
    ap.add_argument(
        "--out_dir", required=True, help="Output directory for CSV files"
    )
    ap.add_argument(
        "--valid_judges",
        nargs="*",
        default=["chatgpt", "gemini", "claude"],
        help="Judges included in main_method statistics (default: chatgpt gemini claude)",
    )
    ap.add_argument(
        "--strict",
        action="store_true",
        help="Enable stricter validity checks (recommended)",
    )
    args = ap.parse_args()

    out_dir = Path(args.out_dir)
    out_dir.mkdir(parents=True, exist_ok=True)

    main_dir = Path(args.main_dir)
    support_dir = Path(args.support_dir) if args.support_dir else None

    # ========= main_method =========
    main_paths = sorted([p for p in main_dir.iterdir() if p.suffix.lower() == ".json"])
    main_records: List[pd.DataFrame] = []
    invalid: List[tuple] = []

    for p in main_paths:
        fn = p.name
        m = JUDGE_RE.match(fn)
        if not m:
            invalid.append((fn, ["bad_filename_for_judge_json"]))
            continue
        judge = m.group(1).lower()
        generator = m.group(2).lower()

        obj = load_json(p)
        v = validate_eval_json(obj, p, strict=args.strict)
        if not v.ok:
            invalid.append((fn, v.reasons))
            continue

        df = eval_to_df(obj, judge=judge, generator=generator)
        main_records.append(df)

    if not main_records:
        raise SystemExit("No valid main_method judge JSON found.")

    df_main = pd.concat(main_records, ignore_index=True)
    found_judges = sorted(df_main["judge"].dropna().unique().tolist())
    found_gens = sorted(df_main["generator"].dropna().unique().tolist())

    valid_judges = [j.lower() for j in args.valid_judges]
    df_main_valid = df_main[df_main["judge"].isin(valid_judges)].copy()

    if df_main_valid.empty:
        raise SystemExit(
            "df_main_valid is empty. "
            f"Found judges={found_judges}, but valid_judges={valid_judges}. "
            "Please check --valid_judges or JSON filenames."
        )

    # Export: per-row detail (main)
    df_main_valid.to_csv(
        out_dir / "main_method_by_row.csv", index=False, encoding="utf-8-sig"
    )

    # Export: per-generator summary (main)
    gen_sum_main = summarize_generator(df_main_valid)
    gen_sum_main.to_csv(
        out_dir / "main_method_by_generator.csv",
        index=False,
        encoding="utf-8-sig",
    )

    # Export: by question / by version / by question×version (main)
    summarize_slices(df_main_valid, out_dir, "main_method")

    # Export: inter-judge agreement (main)
    agree = inter_judge_agreement(df_main_valid)
    agree.to_csv(
        out_dir / "main_method_inter_judge_agreement.csv",
        index=False,
        encoding="utf-8-sig",
    )

    # ========= supporting_method (optional) =========
    gen_sum_sup = pd.DataFrame()
    if support_dir and support_dir.is_dir():
        sup_paths = sorted(
            [p for p in support_dir.iterdir() if p.suffix.lower() == ".json"]
        )
        sup_records: List[pd.DataFrame] = []

        for p in sup_paths:
            fn = p.name
            obj = load_json(p)
            v = validate_eval_json(obj, p, strict=args.strict)
            if not v.ok:
                invalid.append((fn, v.reasons))
                continue

            # Infer model name from filename: self_judge_chatgpt.json -> chatgpt
            base = p.stem.lower()
            base = base.replace("self_judge_", "").replace("self-judge_", "")
            base = base.replace("selfjudge_", "").replace("selfjudge-", "")

            # For self-judging, judge == generator
            df = eval_to_df(obj, judge=base, generator=base)
            sup_records.append(df)

        if sup_records:
            df_sup = pd.concat(sup_records, ignore_index=True)
            df_sup.to_csv(
                out_dir / "supporting_method_by_row.csv",
                index=False,
                encoding="utf-8-sig",
            )

            gen_sum_sup = summarize_generator(df_sup)
            gen_sum_sup.to_csv(
                out_dir / "supporting_method_by_generator.csv",
                index=False,
                encoding="utf-8-sig",
            )

            summarize_slices(df_sup, out_dir, "supporting_method")

    # ========= merged summary =========
    if not gen_sum_main.empty:
        gen_sum_main2 = gen_sum_main.copy()
        gen_sum_main2.insert(0, "method", "main_method")
    else:
        gen_sum_main2 = pd.DataFrame()

    if not gen_sum_sup.empty:
        gen_sum_sup2 = gen_sum_sup.copy()
        gen_sum_sup2.insert(0, "method", "supporting_method")
    else:
        gen_sum_sup2 = pd.DataFrame()

    merged = pd.concat([gen_sum_main2, gen_sum_sup2], ignore_index=True)
    if not merged.empty:
        merged.to_csv(out_dir / "summary.csv", index=False, encoding="utf-8-sig")

    # ========= invalid report =========
    if invalid:
        rep_path = out_dir / "invalid_report.md"
        with open(rep_path, "w", encoding="utf-8") as f:
            f.write("# invalid_report\n\n")
            for fn, reasons in invalid:
                f.write(f"## {fn}\n")
                for r in reasons[:80]:
                    f.write(f"- {r}\n")
                f.write("\n")

    print(f"\nDONE. CSV written to: {out_dir}")
    print(f"Found judges in main_method: {found_judges}")
    print(f"Found generators in main_method: {found_gens}")

    _print_gen_summary(df_main_valid, "MAIN_METHOD (cross-model)")

    if support_dir and support_dir.is_dir() and (
        out_dir / "supporting_method_by_generator.csv"
    ).exists():
        df_sup_show = pd.read_csv(
            out_dir / "supporting_method_by_row.csv", encoding="utf-8-sig"
        )
        _print_gen_summary(df_sup_show, "SUPPORTING_METHOD (self-eval)")


if __name__ == "__main__":
    main()
