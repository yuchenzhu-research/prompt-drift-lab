# Artifact Overview for Reviewers

## Language Authority and Translation Policy

**Authoritative Language (Single Source of Truth)**

All experimental designs, task definitions, data schemas, evaluation rules, and reported results in this artifact are **authoritatively defined in Chinese**.  
`*_ZH` files are authoritative for experiment definitions and evaluation rules; English files are non-authoritative references provided for reviewer readability.

Files under `supplement/02_prompt_variants/*.txt` are preserved prompt assets used in actual execution and are **not constrained by the _ZH authority rule**.

---

**Role of English Materials**

All English-language files **without** the `_ZH` suffix are provided **solely to assist non-Chinese reviewers** in understanding the structure, intent, and inspection workflow of the artifact. These English files:

- Do **not** define independent experiments, configurations, or evaluation rules
- Do **not** introduce alternative parameter settings or result interpretations
- Do **not** carry legal, methodological, or engineering authority

---

**Conflict Resolution Rule**

In the event of any inconsistency, omission, or difference in level of detail between Chinese (`*_ZH`) and English files, **the Chinese version is definitive**.  
English materials are not guaranteed to be line-by-line translations and may be simplified for readability. Such differences **do not imply multiple experimental tracks or variant implementations**.

---

## Scope of This Artifact

This repository contains the complete artifact accompanying the workshop submission.  
It is intentionally scoped to **analysis-level reproducibility**.

No end-to-end re-execution of model inference (prompt → model output) is claimed or required.

---

## Authoritative Result Set

All quantitative results, analyses, and comparisons reported in the paper are derived **exclusively from the fixed result files located in**:

- `supplement/04_results/02_cross_model_evaluation/valid_evaluations/`

The JSON files in this directory constitute the **complete and closed result set** used for evaluation, aggregation, and table generation.

No results outside this directory are selected, filtered, excluded, or incorporated.  
The paper does **not** rely on any subset selection, post-hoc exclusion, or cherry-picking of outcomes.

Reviewers may verify completeness by inspecting the full set of JSON files in this directory and checking their consistency with the evaluation rules and summary tables.

---

## Reproducibility Definition

This artifact distinguishes two layers of reproducibility:

1. **Model inference (prompt → model output)**

   Model outputs were collected via web-based LLM interfaces. Due to the lack of deterministic decoding controls (e.g., fixed seeds or API-level access), **model inference itself is not reproducible**.

2. **Evaluation, aggregation, and analysis (output → scores → tables)**

   All quantitative results reported in the paper are derived from **fixed model outputs** stored under:

   - `supplement/04_results/`

   The evaluation contracts, aggregation logic, and summary tables are fully inspectable and logically reproducible from these fixed artifacts.

Accordingly, this submission supports **analysis-level reproducibility**, rather than re-execution of model inference.

---

## Repository Structure

The artifact is organized as follows:

- `supplement/01_experiment_design/`  
  Experiment tasks, schemas, and protocols.

- `supplement/02_prompt_variants/`  
  Prompt variants and prompt manifests.

- `supplement/03_evaluation_rules/`  
  Evaluation contracts, rubrics, and scoring logic.

- `supplement/04_results/`  
  Fixed model outputs, judged records, and summary tables.

- `supplement/05_methodological_addenda_and_controls/`  
  Additional controls and methodological notes.

---

## How Reviewers Can Inspect the Artifact

Reviewers are **not expected to run any scripts**.

Suggested inspection flow (≈3–5 minutes):

1. Inspect evaluation rules and rubrics in `supplement/03_evaluation_rules/`.
2. Inspect fixed model outputs and judged records in `supplement/04_results/`.
3. Verify that summary tables under:

   - `supplement/04_results/02_cross_model_evaluation/valid_evaluations/summary_tables/`

   are consistent with the provided rules and records.

All scripts included in the repository serve to make the analysis logic explicit and auditable; they are **not required** for reproduction.

---

## Notes on Execution and Dependencies

- No script in this repository is designated as a required execution entry point.
- No API keys, external services, or model interfaces are needed to inspect the artifact.
- All quantitative claims in the paper are supported by pre-computed artifacts included in this package.

---

## Note on English Question Set

`eval_questions_EN.jsonl` is provided as a **non-authoritative English reference** for reviewer readability.

The authoritative evaluation questions used in all experiments are defined exclusively in:

- `supplement/01_experiment_design/eval_questions_ZH.jsonl`

The English question set may be abbreviated or simplified and **does not define an independent or alternative experimental task**.
