# Prompt Drift Lab

> **Reviewer entry:** start from `README_FOR_REVIEWERS.md`.

## Overview

This repository is a frozen artifact pack for studying **prompt drift** in large language models: how small, localized changes in prompt structure, wording, or formatting can lead to failures in instruction following, output schema compliance, and semantic alignment.

The focus is audit-oriented: failures are made explicit, traceable, and inspectable under controlled prompt variations.

---

## Evidence chain (one-way, auditable)

**inputs → raw outputs (PDF) → judge artifacts (JSON) → summary tables (CSV)**

All numbers reported in the CSV tables are traceable to stored per-file record JSON and the original raw PDF outputs.

---

## Quickstart (2–5 minutes)

### 1) Fix the judge version (single source)

Judge versions live under:
- `supplement/04_results/03_processed_evaluations/`

This artifact pack includes:
- `v0_baseline_judge/`
- `v1_paraphrase_judge/`
- `v2_schema_strict_judge/`

Set `<judge_version>` to the version referenced by the submission and keep it fixed when citing tables.

Example:
- `supplement/04_results/03_processed_evaluations/v1_paraphrase_judge/summary_tables/`

### 2) Open the cited result tables

- `supplement/04_results/03_processed_evaluations/<judge_version>/summary_tables/scores_grouped.csv`
- `supplement/04_results/03_processed_evaluations/<judge_version>/summary_tables/scores_long.csv`

### 3) Open the normative evaluation protocol

- `supplement/03_evaluation_rules/eval_protocol.md`

---

## Repository structure

- `supplement/01_experiment_design/` — questions, splits, execution notes
- `supplement/02_prompt_variants/` — prompt variants and manifests
- `supplement/03_evaluation_rules/` — evaluation contracts (protocol, schema, scoring, validity)
- `supplement/04_results/` — frozen evidence and derived outputs (PDF/JSON/CSV)
- `supplement/05_methodological_addenda_and_controls/` — boundaries, controls, notes
- `tools/` — optional offline utilities (not required for audit)

---

## One-way data flow

```
supplement/01_experiment_design/      →  supplement/02_prompt_variants/
                                     →  supplement/04_results/01_raw_model_outputs/      (PDF)
                                     →  supplement/04_results/02_raw_judge_evaluations/  (JSON bundles)
                                     →  supplement/04_results/03_processed_evaluations/  (record_*.json + summary_tables/*.csv)
```

---

## Traceability recipe (csv → json → pdf)

Target chain:

**scores_grouped.csv → scores_long.csv → record_*.json → raw PDF**

1) Choose a row in:
- `supplement/04_results/03_processed_evaluations/<judge_version>/summary_tables/scores_grouped.csv`

2) Locate its supporting per-file row(s) in:
- `supplement/04_results/03_processed_evaluations/<judge_version>/summary_tables/scores_long.csv`

3) From the selected `scores_long.csv` row, copy:
- `file`
- `generator_model`
- `prompt_variant`

4) Locate the corresponding `record_*.json` under:
- `supplement/04_results/03_processed_evaluations/<judge_version>/valid_evaluations/`

Option A: `jq`
```bash
FILE="...from scores_long.csv..."
MODEL="...from scores_long.csv..."
VARIANT="...from scores_long.csv..."

BASE="./supplement/04_results/03_processed_evaluations/<judge_version>/valid_evaluations"
find "$BASE" -type f -name 'record_*.json' -print0 \
  | xargs -0 jq -r --arg file "$FILE" --arg model "$MODEL" --arg variant "$VARIANT" \
    'select(.file==$file and .generator_model==$model and .prompt_variant==$variant) | input_filename'
```

Option B: `grep` fallback
```bash
FILE="...from scores_long.csv..."
MODEL="...from scores_long.csv..."
VARIANT="...from scores_long.csv..."

BASE="./supplement/04_results/03_processed_evaluations/<judge_version>/valid_evaluations"

find "$BASE" -type f -name 'record_*.json' -print0 \
  | xargs -0 grep -l "\"file\": \"$FILE\"" \
  | xargs grep -l "\"generator_model\": \"$MODEL\"" \
  | xargs grep -l "\"prompt_variant\": \"$VARIANT\""
```

5) Open the raw PDF using the `file` field from the matched record:
- `supplement/04_results/01_raw_model_outputs/<record.file>`

---

## Reproducibility scope

Two layers of reproducibility are distinguished:

- **Model generation** (prompt → output), which is inherently non-deterministic under web-based interfaces.
- **Evaluation and analysis** (output → scores → tables), which is fully inspectable and logically reproducible from stored artifacts.

Accordingly, this repository supports analysis-level reproducibility rather than end-to-end re-execution of model inference.

This pack is self-contained for audit: cited CSV tables are backed by stored per-file record JSON and raw PDFs. Exact reproduction of LLM judging by re-running a judge model is not claimed.