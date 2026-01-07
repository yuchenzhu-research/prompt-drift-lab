#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
invalid_to_taxonomy.py

Generate:
  - invalid_report.md
  - taxonomy_table.csv
  - taxonomy_bundles.csv

from an invalid_evaluations/ directory.

Deterministic: only reads JSON artifacts and writes derived summaries.
"""
import argparse
import json
import os
import re
from pathlib import Path
from datetime import datetime

import pandas as pd

FLAG_TO_TAX = {
    "SELF_JUDGING_BIAS": "E_eval_pollution",
    "INTERNAL_INCONSISTENCY": "D_robustness",
    "UNPARSABLE_OUTPUT": "A_schema_format",
    "INCOMPLETE_COVERAGE": "A_schema_format",
    "PROTOCOL_VIOLATION": "B_instruction_deviation",
    "CONTEXT_MISALIGNMENT": "B_instruction_deviation",
    "JUDGE_REFUSAL_OR_EVASION": "B_instruction_deviation",
}

TAX_PRECEDENCE = ["E_eval_pollution", "D_robustness", "A_schema_format", "B_instruction_deviation", "C_semantic_drift"]


def taxonomy_from_flags(flags):
    flags = flags or []
    mapped = [FLAG_TO_TAX.get(f) for f in flags if FLAG_TO_TAX.get(f)]
    if not mapped:
        return None
    for t in TAX_PRECEDENCE:
        if t in mapped:
            return t
    return mapped[0]


def secondary_tax_from_note(note: str):
    text = (note or "").strip()
    if re.search(r"(答非所问|偏题|语义|幻觉|矛盾|事实错误)", text):
        return "C_semantic_drift"
    if re.search(r"(结构|格式|三段|schema|字段|markdown)", text, re.I):
        return "A_schema_format"
    if re.search(r"(不遵循|未按|未做|没有|忽略|必须|约束|违反|回退)", text):
        return "B_instruction_deviation"
    if re.search(r"(不一致|自相矛盾|前后冲突|inconsisten)", text, re.I):
        return "D_robustness"
    if re.search(r"(偏差|自评|bias|污染|投机|迎合)", text, re.I):
        return "E_eval_pollution"
    return None


def note_tags(note: str) -> str:
    text = note or ""
    tags = []
    if re.search(r"(三段|结构|格式|标题|段落)", text):
        tags.append("structure")
    if re.search(r"(快照|50字|字数)", text):
        tags.append("snapshot_len")
    if re.search(r"(机制|原理|分析|诊断|解释)", text):
        tags.append("analysis_leak")
    if re.search(r"(普通回答|常规回答|问答|评论)", text):
        tags.append("drift_to_generic")
    if re.search(r"(覆盖|缺少|不完整|漏|缺失)", text):
        tags.append("coverage")
    if re.search(r"(自评|bias|偏差)", text, re.I):
        tags.append("self_bias")
    return "|".join(tags)


def df_to_md_table(df: pd.DataFrame) -> str:
    """Minimal markdown table renderer (no external deps)."""
    if df.empty:
        return "_(empty)_\n"
    cols = list(df.columns)
    # stringify
    rows = [[("" if pd.isna(v) else str(v)) for v in df.iloc[i].tolist()] for i in range(len(df))]
    # compute widths
    widths = [len(c) for c in cols]
    for r in rows:
        for j, v in enumerate(r):
            widths[j] = max(widths[j], len(v))
    def fmt_row(vals):
        return "| " + " | ".join(v.ljust(widths[i]) for i, v in enumerate(vals)) + " |"
    header = fmt_row(cols)
    sep = "| " + " | ".join(("-" * widths[i]) for i in range(len(cols))) + " |"
    body = "\n".join(fmt_row(r) for r in rows)
    return header + "\n" + sep + "\n" + body + "\n"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--invalid_dir", required=True, help="Path to invalid_evaluations/ directory")
    args = ap.parse_args()

    invalid_dir = Path(args.invalid_dir)
    if not invalid_dir.exists():
        raise SystemExit(f"[ERR] invalid_dir not found: {invalid_dir}")

    json_paths = [p for p in invalid_dir.rglob("*.json")]
    if not json_paths:
        raise SystemExit(f"[ERR] No .json found under: {invalid_dir}")

    rows = []
    bundle_rows = []

    for path in sorted(json_paths):
        with path.open("r", encoding="utf-8") as f:
            d = json.load(f)
        meta = d.get("meta", {})
        flags = d.get("flags", [])
        primary = taxonomy_from_flags(flags) or "B_instruction_deviation"

        rel_bundle_path = str(path.relative_to(invalid_dir.parent.parent.parent)) if "04_results" in str(path) else str(path)

        bundle_rows.append({
            "bundle_file": path.name,
            "bundle_path": rel_bundle_path,
            "method": meta.get("method"),
            "judge_model": meta.get("judge_model"),
            "target_model": meta.get("target_model"),
            "judge_prompt_id": meta.get("judge_prompt_id"),
            "flags": "|".join(flags) if flags else "",
            "taxonomy_primary": primary,
            "n_files": len(d.get("per_file_scores", []))
        })

        for it in d.get("per_file_scores", []):
            note = it.get("notes", "")
            sec = secondary_tax_from_note(note) or ""
            tags = note_tags(note)
            evidence = it.get("evidence", {}) if isinstance(it.get("evidence", {}), dict) else {}
            scores = it.get("scores", {}) if isinstance(it.get("scores", {}), dict) else {}

            rows.append({
                "bundle_file": path.name,
                "bundle_path": rel_bundle_path,
                "method": meta.get("method"),
                "judge_model": meta.get("judge_model"),
                "target_model": meta.get("target_model"),
                "judge_prompt_id": meta.get("judge_prompt_id"),
                "bundle_flags": "|".join(flags) if flags else "",
                "taxonomy_primary": primary,
                "taxonomy_secondary": sec,
                "note_tags": tags,
                "eval_file": it.get("file"),
                "total_score": it.get("total"),
                "A_structure": scores.get("A_structure"),
                "B_snapshot_constraint": scores.get("B_snapshot_constraint"),
                "C_actionability": scores.get("C_actionability"),
                "D_completeness": scores.get("D_completeness"),
                "E_drift_failure": scores.get("E_drift_failure"),
                "note": note,
                "evidence_E_drift_failure": evidence.get("E_drift_failure", ""),
                "evidence_A_structure": evidence.get("A_structure", ""),
            })

    df = pd.DataFrame(rows)
    bundle_df = pd.DataFrame(bundle_rows)

    out_csv = invalid_dir / "taxonomy_table.csv"
    out_bundle_csv = invalid_dir / "taxonomy_bundles.csv"
    out_md = invalid_dir / "invalid_report.md"

    df.to_csv(out_csv, index=False, encoding="utf-8-sig")
    bundle_df.to_csv(out_bundle_csv, index=False, encoding="utf-8-sig")

    # stats
    total_bundles = len(bundle_df)
    total_records = len(df)
    flag_counts = bundle_df["flags"].value_counts().rename_axis("invalid_flag").reset_index(name="bundles")
    tax_bundle_counts = bundle_df["taxonomy_primary"].value_counts().rename_axis("taxonomy").reset_index(name="bundles")
    tax_record_counts = df["taxonomy_primary"].value_counts().rename_axis("taxonomy").reset_index(name="records")
    bundle_list = bundle_df[["bundle_file","method","judge_model","target_model","flags","taxonomy_primary","n_files"]].sort_values(["method","judge_model","target_model"])

    # tag counts
    def split_tags(s):
        if s is None:
            return []
        s = str(s).strip()
        if not s:
            return []
        return [t for t in s.split("|") if t]
    tag_df = df[["taxonomy_primary","note_tags"]].copy()
    tag_df["tag_list"] = tag_df["note_tags"].apply(split_tags)
    tag_exploded = tag_df.explode("tag_list")
    tag_exploded = tag_exploded[tag_exploded["tag_list"].notna() & (tag_exploded["tag_list"]!="")]
    tag_counts = (tag_exploded.groupby(["taxonomy_primary","tag_list"]).size()
                  .reset_index(name="count").sort_values(["taxonomy_primary","count"], ascending=[True,False]))

    # examples by flag
    examples_blocks = []
    for flag in flag_counts["invalid_flag"].tolist():
        sub = df[df["bundle_flags"] == flag].drop_duplicates(subset=["note"])
        sub = sub[["bundle_file","eval_file","note","note_tags","taxonomy_primary"]].head(3)
        examples_blocks.append(f"### {flag}\n\n" + df_to_md_table(sub) + "\n")

    gen_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    md = []
    md.append("# invalid → taxonomy 报告（auto-generated）\n")
    md.append(f"- Generated at: **{gen_time}**\n")
    md.append(f"- Input dir: `{invalid_dir}`\n")
    md.append(f"- Outputs:\n  - `taxonomy_table.csv`\n  - `taxonomy_bundles.csv`\n\n---\n")

    md.append("## 0. 目的\n\n本报告从 `invalid_evaluations/` 目录自动汇总 **哪些评测不可信**，并将每条无效评测映射到项目 Failure Taxonomy（A–E），用于后续“归因/修复/消融”闭环。\n\n")

    md.append("## 1. Taxonomy 映射规则（A–E）\n\n"
              "- **A_schema_format**：输出结构/格式不可解析、字段缺失、样本覆盖不全（例如 `UNPARSABLE_OUTPUT`, `INCOMPLETE_COVERAGE`）。\n"
              "- **B_instruction_deviation**：评测未按协议/上下文执行（例如 `PROTOCOL_VIOLATION`, `CONTEXT_MISALIGNMENT`）。\n"
              "- **C_semantic_drift**：语义层面答非所问/关键事实冲突（本次 invalid 中较少出现，主要靠 notes 触发）。\n"
              "- **D_robustness**：内部不一致/高方差导致结论不可复用（例如 `INTERNAL_INCONSISTENCY`）。\n"
              "- **E_eval_pollution**：评测污染/偏差（例如 `SELF_JUDGING_BIAS`）。\n\n")

    md.append("## 2. 总览统计\n\n")
    md.append(f"- 无效 bundle 数：**{total_bundles}**\n")
    md.append(f"- 文件级记录数（bundle×样本数）：**{total_records}**\n\n")
    md.append("### 2.1 按 invalid flag（bundle 级）\n\n" + df_to_md_table(flag_counts) + "\n")
    md.append("### 2.2 按 taxonomy（bundle 级）\n\n" + df_to_md_table(tax_bundle_counts) + "\n")
    md.append("### 2.3 按 taxonomy（文件级记录）\n\n" + df_to_md_table(tax_record_counts) + "\n")

    md.append("## 3. 无效 bundle 清单\n\n" + df_to_md_table(bundle_list) + "\n")

    # top tags
    md.append("## 4. Notes 模式（辅助线索，不作为“无效判定”主因）\n\n")
    for tax in sorted(df["taxonomy_primary"].unique()):
        sub = tag_counts[tag_counts["taxonomy_primary"] == tax].head(4)
        parts = [f"{r.tag_list}({int(r['count'])})" for _, r in sub.iterrows()]
        md.append(f"- **{tax}**: " + (", ".join(parts) if parts else "_(none)_") + "\n")
    md.append("\n> 说明：`note_tags` 仅从 `notes` 文本做正则提取，用于快速找模式；真正的无效原因以 `bundle_flags` 为准。\n\n")

    md.append("## 5. 代表性样例（每类 flag 取 3 条不同 notes）\n\n")
    md.extend(examples_blocks)

    md.append("## 6. 如何复现生成（deterministic）\n\n"
              "在 repo 根目录运行：\n\n"
              "```bash\n"
              "python tools/invalid_to_taxonomy.py \\\n"
              "  --invalid_dir 04_results/02_cross_model_evaluation/invalid_evaluations\n"
              "```\n\n"
              "生成：\n"
              "- `invalid_evaluations/invalid_report.md`\n"
              "- `invalid_evaluations/taxonomy_table.csv`\n"
              "- `invalid_evaluations/taxonomy_bundles.csv`\n")

    out_md.write_text("".join(md), encoding="utf-8")
    print(f"[OK] wrote: {out_csv}")
    print(f"[OK] wrote: {out_bundle_csv}")
    print(f"[OK] wrote: {out_md}")


if __name__ == "__main__":
    main()
