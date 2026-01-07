# README (for Reviewers)

This package contains a 4-page workshop-style paper and a minimal, self-contained supplement bundle with auditable artifacts (prompt variants, evaluation rules, raw outputs, judge bundles, and derived tables).

## Package layout (top-level)
- `paper/paper.pdf` : main text
- `supplement/supplement_min.zip` : minimal artifact bundle (prompts, rules, results, scripts)
- `ANONYMIZATION_CHECKLIST.md` : anonymization notes
- `CHECKSUMS.sha256` : integrity hashes for the top-level files

## Quick start (recommended)
From the repository root:

```bash
# 1) Extract the minimal supplement bundle
unzip -q supplement/supplement_min.zip -d supplement/supplement_min

# 2) Enter the extracted bundle (working directory for the scripts below)
cd supplement/supplement_min
```

## Reproduce the main summary table
From `supplement/supplement_min/`, run:

```bash
bash tools/reproduce_summary.sh
```

Expected output (root-relative path after extraction):
- `supplement/supplement_min/04_results/02_cross_model_evaluation/valid_evaluations/summary_tables/summary.csv`

## Reproduce invalid → taxonomy report
From `supplement/supplement_min/`, run:

```bash
python tools/invalid_to_taxonomy.py \
  --input_dir 04_results/02_cross_model_evaluation/invalid_evaluations \
  --out_dir 04_results/02_cross_model_evaluation/invalid_evaluations
```

Expected outputs (root-relative paths after extraction):
- `supplement/supplement_min/04_results/02_cross_model_evaluation/invalid_evaluations/invalid_report.md`
- `supplement/supplement_min/04_results/02_cross_model_evaluation/invalid_evaluations/taxonomy_table.csv`

## If you prefer not to run scripts
After extracting `supplement_min.zip`, you can directly inspect:
- `supplement/supplement_min/04_results/02_cross_model_evaluation/valid_evaluations/summary_tables/summary.csv`
- `supplement/supplement_min/04_results/02_cross_model_evaluation/invalid_evaluations/invalid_report.md`

## Integrity check (optional)
From the repository root:

```bash
sha256sum -c CHECKSUMS.sha256
# (macOS) shasum -a 256 -c CHECKSUMS.sha256
```
