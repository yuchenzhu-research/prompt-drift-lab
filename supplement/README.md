# Supplement (Prompt Drift Lab)

This `supplement/` directory contains the full, auditable artifact set referenced by the paper:
- **Experiment design** (tasks, schema, protocol): `01_experiment_design/`
- **Prompt variants** (generation prompts + manifest): `02_prompt_variants/`
- **Evaluation rules** (judge contract, rubric, protocol): `03_evaluation_rules/`
- **Results** (raw outputs, judged records, summary tables, analysis): `04_results/`
- **Controls / methodological addenda**: `05_methodological_addenda_and_controls/`

## Fast path
If you are a reviewer, start at the repository root:
- `README_FOR_REVIEWERS.md`

## Reproducing summary tables
From `supplement/`:
```bash
bash tools/reproduce_summary.sh
```
This regenerates CSV tables under:
- `04_results/02_cross_model_evaluation/valid_evaluations/summary_tables_reproduced/`

Precomputed tables are also provided for direct inspection:
- `04_results/02_cross_model_evaluation/valid_evaluations/summary_tables/`