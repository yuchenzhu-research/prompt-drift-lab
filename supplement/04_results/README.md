# 04 Results — Overview

This directory contains **all concrete experiment artifacts** produced by executing the evaluation pipeline.
It serves as the **single authoritative index** of result files used for analysis and reporting.

**Data flow:**

raw model outputs → structured evaluations → aggregated analysis

Raw model outputs are collected under `01_raw_model_outputs/`, evaluated into structured judgment records under `02_cross_model_evaluation/`, and summarized via aggregated tables derived **exclusively from valid evaluations**.

---

## Scope and Guarantees

- This directory contains **only realized artifacts** produced by the experiment.
- No results are inferred, reconstructed, or implied beyond the files present here.
- All reported statistics in the paper trace back to files listed in this directory.

Invalid evaluations are retained for **auditability and diagnostic purposes only** and are excluded from all quantitative aggregation.

---

## File Naming Conventions

Files and subdirectories under `04_results/` follow fixed, rule-based **naming conventions**.

In explanatory text, schematic expressions such as `{model}`, `{judge}`, or `<generator_model>` are used **only to describe variable components** of these naming patterns. They do **not** refer to literal filenames or directories that must exist verbatim.

All concrete result files are explicitly present in the directory tree below.

---

## 0) 30-second navigation

### 1) Top-line summary (CSV)

- `04_results/02_cross_model_evaluation/valid_evaluations/summary_tables/summary.csv`

This file is the **single entry point** for all quantitative results reported in the paper.

---

### 2) Breakdown tables (CSV)

**Main method (cross-model judging):**
- `04_results/02_cross_model_evaluation/valid_evaluations/summary_tables/main_method_by_generator.csv`
- `04_results/02_cross_model_evaluation/valid_evaluations/summary_tables/main_method_by_variant.csv`
- `04_results/02_cross_model_evaluation/valid_evaluations/summary_tables/main_method_by_question.csv`
- `04_results/02_cross_model_evaluation/valid_evaluations/summary_tables/main_method_by_question_variant.csv`
- `04_results/02_cross_model_evaluation/valid_evaluations/summary_tables/main_method_inter_judge_agreement.csv`

**Supporting method (self-evaluation sanity check):**
- `04_results/02_cross_model_evaluation/valid_evaluations/summary_tables/supporting_method_by_generator.csv`
- `04_results/02_cross_model_evaluation/valid_evaluations/summary_tables/supporting_method_by_variant.csv`
- `04_results/02_cross_model_evaluation/valid_evaluations/summary_tables/supporting_method_by_question.csv`
- `04_results/02_cross_model_evaluation/valid_evaluations/summary_tables/supporting_method_by_question_variant.csv`

---

### 3) Judged evaluation records (JSON)

**Valid evaluations (used for all aggregation):**
- Main method (cross-model judging):
  - `04_results/02_cross_model_evaluation/valid_evaluations/main_method_cross_model/`
- Supporting method (self-evaluation sanity check):
  - `04_results/02_cross_model_evaluation/valid_evaluations/supporting_method_self_eval/`

**Invalid evaluations (excluded from all statistics):**
- `04_results/02_cross_model_evaluation/invalid_evaluations/`

Invalid evaluations are preserved **only for auditability and failure-mode diagnosis**.

---

### 4) Raw model outputs (PDF)

- `04_results/01_raw_model_outputs/<generator_model>/`

Here, `<generator_model>` denotes the generator model name as part of the directory naming convention, not a literal placeholder.

---

## Directory map

```
04_results/
├── 01_raw_model_outputs/
│   ├── anthropic_claude-sonnet-4.5_extended-thinking/
│   │   └── *.pdf
│   ├── google_gemini-3-pro/
│   │   └── *.pdf
│   └── openai_gpt-5.2_extended-thinking/
│       └── *.pdf
│
├── 02_cross_model_evaluation/
│   ├── valid_evaluations/
│   │   ├── main_method_cross_model/
│   │   ├── supporting_method_self_eval/
│   │   └── summary_tables/
│   │
│   └── invalid_evaluations/
│       ├── case_study_implicit_role_drift.md
│       ├── README.md
│       ├── invalid_report.md
│       ├── main_method_cross_model/
│       └── supporting_method_self_eval/
│
├── 03_results_analysis.md
└── README.md
```

Angle-bracketed or brace-delimited terms indicate naming conventions rather than literal file or directory names.