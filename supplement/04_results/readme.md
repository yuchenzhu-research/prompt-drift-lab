# supplement/04_results — Evaluation results and derived artifacts

This directory contains all **evaluation evidence and derived results** used in the paper.  
It is organized to support **direct inspection**, **deterministic regeneration**, and **one-way traceability** from summary tables back to raw artifacts.

---

## Directory overview

- `01_raw_model_outputs/`  
  Frozen model outputs evaluated in this study (PDF files). These files are not modified or re-parsed.

- `02_raw_judge_evaluations/`  
  Preserved judge outputs (JSON bundles) produced directly from evaluating the raw model outputs.

- `03_processed_evaluations/`  
  Deterministic, derived artifacts generated from raw judge bundles, including:
  - per-file audit records (`record_*.json`)
  - paper-cited summary tables (`scores_long.csv`, `scores_grouped.csv`)

- `04_results_analysis.md`  
  Aggregated observations and analysis notes derived strictly from the summary tables.

---

## One-way data flow

```
01_raw_model_outputs (PDF)
        ↓
02_raw_judge_evaluations (JSON bundles)
        ↓
03_processed_evaluations (records + summary_tables)
        ↓
04_results_analysis.md
```

This flow is strictly one-directional. No later stage feeds back into an earlier stage.

---

## Scope and guarantees

- All artifacts under this directory are frozen and versioned.
- No evaluation rules are defined here (see `/supplement/03_evaluation_rules/`).
- All reported results in the paper cite files under `03_processed_evaluations/<judge_version>/summary_tables/`.
- Reproduction scripts are provided in `/supplement/tools/`, but execution is **not required** to audit the results.
- Processed evaluation records are regenerated only when input artifacts or validity conditions change; otherwise, previously validated records are preserved.

This structure ensures that reviewers can verify reported numbers without executing code.