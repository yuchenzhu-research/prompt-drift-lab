# README for Reviewers

This repository contains a 4-page workshop-style paper and a minimal, self-contained supplement with auditable artifacts (prompt variants, evaluation rules, raw outputs, judge bundles, and derived tables).

## Package layout (top-level)
- `paper/paper.pdf` : main text
- `supplement/` : minimal artifact bundle (prompts, rules, results, scripts)
- `ANONYMIZATION_CHECKLIST.md` : anonymization notes
- `CHECKSUMS.sha256` : integrity hashes for files in this repository

## Quick start (recommended)
After unzipping this package, all supplementary artifacts are available as plain files (no nested archives).

From the repository root:

```bash
cd supplement
```

> Note: All commands below are verified on macOS/Linux using `python3`.

## Tasks covered in this submission

This submission covers the following tasks. All reported CSV tables are derived
from the same set of valid evaluations and differ only by aggregation or slicing
dimension.

- **Q1 (Cross-model robustness)**: Robustness across different model generators.
  - Tables aggregated by generator (e.g., `*_by_generator.csv`) and overall summaries.

- **Q2 (Judge consistency)**: Agreement and consistency across independent judges
  under identical evaluation rules.
  - Tables reporting inter-judge agreement (e.g., `*_inter_judge_agreement.csv`).

- **Q3 (Prompt sensitivity)**: Sensitivity to prompt variants, wording, and
  constraint formulations.
  - Tables sliced by prompt variant, question variant, or row-level instances
    (e.g., `*_by_variant.csv`, `*_by_question_variant.csv`, `*_by_row.csv`).

- **Q4 (Invalid evaluations, qualitative only)**: Analysis of invalid evaluation
  cases for diagnostic and qualitative inspection.
  - Invalid cases are not included in any quantitative CSV tables.

No other tasks are claimed or evaluated.


## Reproduce the main summary table
From `supplement/`, run:

```bash
bash tools/reproduce_summary.sh
```

Expected output (root-relative path):
- `supplement/04_results/02_cross_model_evaluation/valid_evaluations/summary_tables_reproduced/main_method_by_generator.csv` (and related CSVs)

(For convenience, the same tables are also included as precomputed files under `.../summary_tables/`.)

> **Scope note:** No finalized quantitative taxonomy is reported or claimed in this submission.

## Invalid Evaluation Artifacts
Invalid evaluation cases are provided for qualitative inspection only. They are used to contextualize and diagnose observed behaviors and are **not** aggregated into any finalized quantitative taxonomy.

If you prefer not to run scripts, you can directly inspect the qualitative artifacts at:
- `supplement/04_results/02_cross_model_evaluation/invalid_evaluations/`

## If you prefer not to run scripts
You can directly inspect the derived quantitative artifacts at:
- `supplement/04_results/02_cross_model_evaluation/valid_evaluations/summary_tables/main_method_by_generator.csv` (and related CSVs)

(For convenience, the same tables are also included as precomputed files under `.../summary_tables/`.)

## Integrity check (optional)
From the repository root:

```bash
sha256sum -c CHECKSUMS.sha256
# (macOS) shasum -a 256 -c CHECKSUMS.sha256

# Note: CHECKSUMS.sha256 intentionally does not contain an entry for itself.
```

