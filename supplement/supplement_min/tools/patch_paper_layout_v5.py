#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Patch PDF layout safely:
- Move Appendix block to page 3 blank area
- Rebuild page 4 as References-only (keep footer area)
Requires: pip install pymupdf
Usage:
  cd /Users/yuchenzhu/Desktop/正式
  python3 supplement/supplement_min/tools/patch_paper_layout_v5.py paper/paper_v4_fixed.pdf paper/paper_v5_final.pdf
"""

import sys
import textwrap
import fitz  # PyMuPDF

def main(pdf_in: str, pdf_out: str):
    doc = fitz.open(pdf_in)

    x0 = 72
    width = 468
    footer_keep = 40

    # ---------- Page 4: rebuild References-only ----------
    p4 = doc[3]
    page_w, page_h = p4.rect.width, p4.rect.height

    # wipe everything except footer (keeps page number if present)
    wipe = fitz.Rect(0, 0, page_w, page_h - footer_keep)
    p4.add_redact_annot(wipe, fill=(1, 1, 1))
    p4.apply_redactions()

    p4.insert_text((x0, 88), "References", fontname="Times-Bold", fontsize=16, color=(0, 0, 0))
    refs_text = textwrap.dedent("""\
    [1] OpenReview. Formatting Instructions for ICLR 2026 Conference Submissions.
    [2] Pengfei Liu, Weizhe Yuan, Jinlan Fu, Zhengbao Jiang, Hiroaki Hayashi, Graham Neubig. Pre-train, Prompt, and Predict: A Systematic Survey of Prompting Methods in Natural Language Processing. ACM Computing Surveys, 2023.
    [3] Jiawei Gu, Xuhui Jiang, Zhichao Shi, et al. A Survey on LLM-as-a-Judge. arXiv:2411.15594, 2024.
    """).strip()

    refs_rect = fitz.Rect(x0, 112, x0 + width, page_h - footer_keep - 20)
    p4.insert_textbox(refs_rect, refs_text, fontname="Times-Roman", fontsize=10, color=(0, 0, 0), align=0)

    # ---------- Page 3: add Appendix into blank space ----------
    p3 = doc[2]
    anchor = p3.search_for("invalid taxonomy")
    y_start = (anchor[0].y1 + 22) if anchor else 360
    y_start = max(y_start, 330)
    max_y = page_h - footer_keep - 10

    p3.insert_text((x0, y_start), "Appendix:  audit artifact inventory", fontname="Times-Bold", fontsize=14, color=(0, 0, 0))
    p3.insert_text((x0, y_start + 20), "(supplement)", fontname="Times-Bold", fontsize=14, color=(0, 0, 0))

    body = textwrap.dedent("""\
    Versioned inputs. Prompt variants (02_prompt_variants/), evaluation protocol and judge-contract (03_evaluation_rules/), and task set (01_experiment_design/).

    Run artifacts. Each run directory stores: (1) config (model/decoding/prompt-set versions), (2) raw outputs, (3) judged records (per-dimension scores + evidence), and (4) summary tables. Invalid evaluations are stored under 04_results/02_cross_model_evaluation/invalid_evaluations/ and are included in the taxonomy analysis.

    Reproduce tables/figures. From supplement/supplement_min/:
    """)

    body_rect = fitz.Rect(x0, y_start + 40, x0 + width, min(y_start + 170, max_y))
    p3.insert_textbox(body_rect, body, fontname="Times-Roman", fontsize=10, color=(0, 0, 0), align=0)

    # NOTE: conservative paths aligned with the typical supplement_min layout
    code = "python 03_evaluation_rules/compute_scores.py\npython tools/invalid_to_taxonomy.py"
    code_rect = fitz.Rect(x0, y_start + 170, x0 + width, min(y_start + 205, max_y))
    p3.insert_textbox(code_rect, code, fontname="Courier", fontsize=9.5, color=(0, 0, 0), align=0)

    p3.insert_text((x0, y_start + 235), "Anonymization note.", fontname="Times-Bold", fontsize=10, color=(0, 0, 0))
    anon = (" For double-blind review, keep the public code link out of the main PDF; "
            "include either (a) an anonymized repository link or (b) a zipped supplement with code + artifacts.")
    anon_rect = fitz.Rect(x0 + 118, y_start + 227, x0 + width, min(y_start + 275, max_y))
    p3.insert_textbox(anon_rect, anon, fontname="Times-Roman", fontsize=10, color=(0, 0, 0), align=0)

    doc.save(pdf_out)
    doc.close()
    print(f"[OK] wrote: {pdf_out}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: patch_paper_layout_v5.py <pdf_in> <pdf_out>")
        sys.exit(1)
    main(sys.argv[1], sys.argv[2])
