# 04 Results

This folder contains **all experiment artifacts** produced by running the evaluation pipeline. It serves as the **only authoritative index** of concrete result files used in analysis.

**Data flow (single direction):** raw model outputs → structured evaluations → aggregated analysis.

Raw model outputs are first collected under `01_raw_model_outputs/`, then evaluated into structured judgment records under `02_cross_model_evaluation/` (with valid and invalid cases separated), and all reported statistics and analyses are derived **exclusively** from aggregated tables generated from **valid evaluations**.

Contents include:
- raw model outputs (PDFs),
- judged evaluation records (JSON),
- aggregated summary tables (CSV),
- and a short narrative analysis.

If you are looking for **interpretation** (A/B rationale, drift attribution, failure modes), read:
- `04_results/03_results_analysis.md`
- and, for methodological rationale / controls: `05_methodological_addenda_and_controls/`

---

## File Naming Conventions

Files and subdirectories under `04_results/` follow consistent, rule-based **naming conventions**.

In explanatory text, schematic expressions such as `{model}`, `{judge}`, or `<generator_model>` are used **only to describe variable components in these naming patterns**. They do **not** refer to literal filenames or directories that must exist verbatim in the artifact.

All concrete result files are explicitly present in the directories listed below. No additional result files are implied beyond those visible here.

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

**Valid evaluations (used for all aggregation and tables):**
- Main method (cross-model judging):  
  `04_results/02_cross_model_evaluation/valid_evaluations/main_method_cross_model/`
- Supporting method (self-evaluation sanity check):  
  `04_results/02_cross_model_evaluation/valid_evaluations/supporting_method_self_eval/`

**Invalid evaluations (excluded from all statistics):**
- `04_results/02_cross_model_evaluation/invalid_evaluations/`

Invalid evaluations are preserved **only for auditability and failure-mode diagnosis** and never enter quantitative analysis.

---

### 4) Raw model outputs (PDF)

- `04_results/01_raw_model_outputs/<generator_model>/`

Here, `<generator_model>` denotes the model that produced the raw output and is part of the directory naming convention, rather than a literal placeholder.

---

## 5) Directory map

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
│       ├── README.md
│       ├── invalid_report.md
│       ├── main_method_cross_model/
│       └── supporting_method_self_eval/
│
├── 03_results_analysis.md
└── README.md
```

Angle-bracketed or brace-delimited terms (e.g., `<generator_model>`, `{model}`) indicate naming conventions or schema components, not literal directory or file names.

