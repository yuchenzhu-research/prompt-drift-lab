# Prompt Drift Lab — Minimal Artifact Bundle

This bundle is intentionally minimal: it contains the **prompt variants**, **evaluation rules**, **raw model outputs**, and **derived tables/reports** referenced by the paper.

## Directory map

```
02_prompt_variants/      # prompt variants + manifests
03_evaluation_rules/     # evaluation protocol + judge prompt + scoring scripts
04_results/              # raw outputs + valid/invalid evals + summary tables
tools/                   # helper scripts (reproduce / taxonomy)
paper_assets/            # assets used to generate paper figures/tables (not a duplicate of the paper)
VERSION_MAP.md           # version + integrity mapping for canonical artifacts
```

Note: the numbering starts at `02_` because this is a **minimal** excerpted bundle; base task definitions are fixed and folded into the prompt-variant manifests.

## Quick pointers

- Prompt manifests:
  - `02_prompt_variants/PROMPT_MANIFEST.md`
  - `02_prompt_variants/PROMPT_MANIFEST_ZH.md`
- Evaluation protocol:
  - `03_evaluation_rules/EVAL_PROTOCOL.md`
- Judge prompt:
  - `03_evaluation_rules/JUDGE_PROMPT.md`
- Raw model outputs:
  - `04_results/01_raw_model_outputs/`
- Main summary table:
  - `04_results/02_cross_model_evaluation/valid_evaluations/summary_tables/summary.csv`
- Invalid taxonomy report:
  - `04_results/02_cross_model_evaluation/invalid_evaluations/invalid_report.md`

## Reproduce (optional)

From this bundle root:

```bash
bash tools/reproduce_summary.sh
python tools/invalid_to_taxonomy.py \
  --input_dir 04_results/02_cross_model_evaluation/invalid_evaluations \
  --out_dir 04_results/02_cross_model_evaluation/invalid_evaluations
```
