# Supplement README

## Language Authority

All experimental definitions, evaluation rules, data schemas, and result interpretations within this `supplement/` directory are authoritatively defined in Chinese.

Files with the `_ZH` suffix constitute the single source of truth.

English files without the `_ZH` suffix are provided solely for reviewer readability and structural guidance. They do not introduce independent experiments, alternative configurations, or binding interpretations.

In the event of any inconsistency between Chinese and English files, the Chinese version is definitive.

For a complete statement of language authority and reproducibility scope, see `../README_FOR_REVIEWERS.md`.

---

## Scope of This Directory

This `supplement/` directory contains the complete, auditable artifact set referenced by the paper.

It is designed for analysis-level reproducibility and structured inspection, rather than end-to-end re-execution of model inference.

No script in this directory is required to be executed by reviewers.

---

## Directory Overview

- **Experiment design** (tasks, schemas, protocols):  
  `01_experiment_design/`

- **Prompt variants** (generation prompts and manifests):  
  `02_prompt_variants/`

- **Evaluation rules** (judge contracts, rubrics, scoring protocols):  
  `03_evaluation_rules/`

- **Results** (fixed model outputs, judged records, summary tables):  
  `04_results/`

- **Methodological addenda and controls**:  
  `05_methodological_addenda_and_controls/`

- **Inspection utilities (non-required)**:  
  `tools/`

---

## Reviewer Inspection Flow

Reviewers are not expected to run any scripts.

Suggested inspection order:

1. Task definitions and schemas in `01_experiment_design/`.
2. Prompt variants and manifests in `02_prompt_variants/`.
3. Evaluation contracts and scoring logic in `03_evaluation_rules/`.
4. Fixed outputs, judged records, and summary tables in `04_results/`.

All scripts under `tools/` exist solely to make evaluation logic explicit and auditable.

---

## Authoritative Result Location

All quantitative results reported in the paper are derived exclusively from the fixed artifacts under:

- `04_results/02_cross_model_evaluation/valid_evaluations/`

No result outside this directory is selected, filtered, excluded, or incorporated.

---

## Notes

- No API keys, external services, or model interfaces are required to inspect this artifact.
- API-dependent re-execution is intentionally avoided to prevent nondeterministic reproduction paths.