# 04_results — Artifact Map (no rules, no code)

This directory is a **data map** of realized artifacts produced by the evaluation pipeline.
It is an index of files and their roles.

- **No evaluation rules** are defined here.
- **No processing code** is stored here.

---

## One-way data flow (3 layers)

1) **Raw model outputs** → `01_raw_model_outputs/` (`*.pdf`)
2) **Raw judge evaluations** → `02_raw_judge_evaluations/` (judge bundles + prompt text + `run_meta.json`)
3) **Processed evaluations** → `03_processed_evaluations/` (per-record JSON + summary tables)

This pipeline is **one-way**: raw artifacts are preserved, and downstream artifacts remain traceable to upstream files.

---

## diagnostic vs final (raw judge evaluations)

`02_raw_judge_evaluations/` is split by label:

- `diagnostic/`: exploratory runs retained **only for diagnostic reference** (not used for final claims)
- `final/`: runs used for reported results and downstream aggregation

Judge-run directories (examples):

- `diagnostic/v0_baseline_judge/`
- `final/v1_paraphrase_judge/`
- `final/v2_schema_strict_judge/`

---

## Non-scope (what is NOT defined here)

- **Evaluation rules / validity definitions** live in `supplement/03_evaluation_rules/`.
- **Deterministic processing scripts** live under `tools/`.

---

## Entry points (where to start)

**Processed summary tables (CSV) — primary reporting inputs**
- `03_processed_evaluations/*/summary_tables/scores_grouped.csv`
- `03_processed_evaluations/*/summary_tables/scores_long.csv`
- `03_processed_evaluations/*/summary_tables/run_meta.json`
- `03_processed_evaluations/v2_schema_strict_judge/summary_tables/excluded_records.jsonl`

**Processed per-record JSON — audit trail**
- `03_processed_evaluations/*/valid_evaluations/**/record_*.json`

**Raw judge bundles — preserved inputs to processing**
- `02_raw_judge_evaluations/{diagnostic|final}/*/judge_*_bundle_*.json`

**Raw model outputs (PDF) — immutable generation snapshot**
- `01_raw_model_outputs/<generator_model>/*.pdf`

**Analysis note**
- `03_results_analysis.md` (describes grouping/aggregation rules; does not define evaluation rules)

---

## Directory map (shape only)

```
04_results/
├── 01_raw_model_outputs/
│   ├── anthropic_claude-sonnet-4.5_extended-thinking/   (*.pdf)
│   ├── google_gemini-3-pro/                             (*.pdf)
│   └── openai_gpt-5.2_extended-thinking/                (*.pdf)
│
├── 02_raw_judge_evaluations/
│   ├── diagnostic/
│   │   └── v0_baseline_judge/                           (judge bundles + prompt text + run_meta.json)
│   └── final/
│       ├── v1_paraphrase_judge/                         (judge bundles + prompt text + run_meta.json)
│       └── v2_schema_strict_judge/                      (judge bundles + prompt text + run_meta.json)
│
├── 03_processed_evaluations/
│   ├── v0_baseline_judge/                               (diagnostic outputs)
│   ├── v1_paraphrase_judge/                             (final outputs)
│   └── v2_schema_strict_judge/                          (final outputs)
│
├── 03_results_analysis.md
└── readme.md
```