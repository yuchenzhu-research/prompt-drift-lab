# Prompt Drift Lab — Reproducible Evaluation Artifact Pack (ICLR 2026 Workshop)

Prompt Drift Lab is a frozen, inspection-friendly evaluation pack for observing **behavior drift under small prompt changes** (instruction-following drop, schema/format break, semantic drift).

This repository is organized around a one-way evidence chain:

**inputs → raw outputs → judged records → summary tables**

Reviewers can trace every reported number back to preserved artifacts without re-running model inference.

---

## Start here (2–5 minutes)

1. **Primary result tables (what the paper cites)**
   - `supplement/04_results/03_processed_evaluations/*/summary_tables/scores_grouped.csv`
   - `supplement/04_results/03_processed_evaluations/*/summary_tables/scores_long.csv`

2. **Evaluation authority (what “counts” as valid, how scoring fields are defined)**
   - `supplement/03_evaluation_rules/eval_protocol.md` (normative entry point)

3. **Trace one number end-to-end**
   - Follow the “Traceability recipe” section below.

---

## One-way data flow

```
01_experiment_design/ (questions, split, execution protocol template)
        │
        ▼
02_prompt_variants/ (generator prompts used to produce outputs)
        │
        ▼
04_results/01_raw_model_outputs/ (raw PDFs; immutable evidence)
        │
        ▼
04_results/02_raw_judge_evaluations/ (raw judge JSON bundles)
        │
        ▼
04_results/03_processed_evaluations/ (per-file records + summary_tables/*.csv)
        │
        ▼
04_results/04_results_analysis.md (how grouping/aggregation is done; no new rules)
```

Notes:
- Raw model outputs are preserved as **PDFs** and are not edited or cleaned.
- Processing and aggregation operate on **stored judge JSON artifacts** (not on PDFs).

---

## What is authoritative

### Execution inputs
- **Questions (authoritative):** `supplement/01_experiment_design/eval_questions_ZH.jsonl`
- **Questions (reference translation):** `supplement/01_experiment_design/eval_questions_EN.jsonl`
- **Prompt variants inventory (authoritative):** `supplement/02_prompt_variants/prompt_manifest.md`
- **Executable prompt files (Chinese, used verbatim):** `supplement/02_prompt_variants/*.txt`

### Evaluation contracts
- **Only normative evaluation protocol:** `supplement/03_evaluation_rules/eval_protocol.md`
- Judge instruction template: `supplement/03_evaluation_rules/judge_prompt.md`
- JSON shape validation schema: `supplement/03_evaluation_rules/schema/eval_record.schema.json`
- Scoring fields and meanings: `supplement/03_evaluation_rules/scoring_dimensions.md`
- Valid/invalid criteria: `supplement/03_evaluation_rules/validity_criteria.md`
- Failure labels: `supplement/03_evaluation_rules/failure_taxonomy.md`

### Reported numbers
- **Primary reporting inputs:**
  - `supplement/04_results/03_processed_evaluations/*/summary_tables/scores_grouped.csv`
  - `supplement/04_results/03_processed_evaluations/*/summary_tables/scores_long.csv`

---

## Development vs held-out evaluation

The benchmark contains four questions with a fixed split:
- **Q1–Q2:** development-only (prompt iteration / sanity checks)
- **Q3–Q4:** held-out evaluation set used for quantitative summaries

This split is specified under `supplement/01_experiment_design/`.

---

## Traceability recipe (how to audit a number)

Pick any row in a grouped table, for example:

- `supplement/04_results/03_processed_evaluations/<judge_version>/summary_tables/scores_grouped.csv`

Then:

1. Locate the corresponding **per-file rows** in:
   - `supplement/04_results/03_processed_evaluations/<judge_version>/summary_tables/scores_long.csv`

   Match on:
   - `judge_version`, `generator_model`, `question_id`, `prompt_variant`, `trigger_type`

2. For any `scores_long.csv` row, open the referenced **per-file record** (JSON):
   - `supplement/04_results/03_processed_evaluations/<judge_version>/valid_evaluations/**/record_*.json`

3. From that record, use `source_bundle` to open the **raw judge bundle**:
   - `supplement/04_results/02_raw_judge_evaluations/{diagnostic|final}/<judge_version>/<source_bundle>`

4. Use the `file` field to open the **raw model output PDF**:
   - `supplement/04_results/01_raw_model_outputs/<generator_model>/<file>`

This chain (grouped row → long row → record JSON → judge bundle → raw PDF) is the audit path.

---

## Repository map

- `supplement/01_experiment_design/` — inputs and execution setup (questions, split, output layout, protocol template)
- `supplement/02_prompt_variants/` — generator-side prompt variants (Chinese `.txt` prompts + manifest)
- `supplement/03_evaluation_rules/` — evaluation contracts only (protocol, schema, scoring dimensions, validity criteria)
- `supplement/04_results/` — frozen evidence and derived artifacts (raw PDFs, judge bundles, processed records, summary tables)
- `supplement/05_methodological_addenda_and_controls/` — non-normative notes for interpretation boundaries (no new experiments)
- `supplement/tools/` — offline utilities for inspection (no API calls; not required for reviewers)

---

## Language policy

- **Chinese is used for execution inputs** (questions and generator prompts).
- **English is used for evaluation contracts and documentation**.

For the exact authoritative inputs, see the paths listed under “What is authoritative”.

---

## What reviewers do not need to run

Reviewers are not expected to execute scripts.
- Raw evidence (PDFs) and processed results (CSV/JSON) are included.
- Tools under `supplement/tools/` are provided for optional offline inspection.