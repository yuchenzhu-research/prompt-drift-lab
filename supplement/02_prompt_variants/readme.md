# 02 Prompt Variants

This directory contains the **generator-side prompt variants** used in the prompt drift experiments.
All executable prompts are written in **Chinese** and are used verbatim during experimental execution.
English content in this file is provided solely for reviewer comprehension and does not constitute executable prompt artifacts.

This directory does **not** include judge prompts, judging logic, or evaluation definitions.
All judge-side components are defined under `supplement/03_evaluation_rules/`.

---

## Prompt Language and Authority

- All `.txt` prompt files in this directory are authored in **Chinese**.
- These Chinese prompt files are the **only authoritative inputs** used during experimental execution.
- English descriptions below are **semantic paraphrases** (not line-by-line translations) provided for reviewer readability only.

---

## Prompt Variants (English Paraphrases)

The following sections summarize the role of each prompt variant. They are not executable instructions and should not be interpreted as alternative prompt definitions.

### 1. Baseline (A — pilot)

A minimal instruction that specifies the required three-section output interface.
This file is used for early pipeline sanity checks and qualitative reference.
It is excluded from quantitative summary tables (see `prompt_manifest.md`).

### 2. Structured Baseline (B — primary)

A fully specified prompt that defines the three-section output interface using explicit cues.
This variant serves as the **primary experimental anchor** for quantitative evaluation and cross-variant comparison.

### 3. Conflict

A perturbation of the structured baseline that introduces competing requirements while keeping the same three-section interface.

### 4. Long

A length-inflated variant of the structured baseline that adds redundant background and repeated guidance to increase input length.

### 5. Weak

A variant where constraint wording is softened while keeping the same task and interface.

---

## Manifest Authority and Auditability

- `prompt_manifest.md` is the **single source of truth** for the prompt inventory and variant roles.
- Prompt files listed in the manifest are treated as **preserved execution assets** and must not be modified in place.
- Result directories may snapshot the exact manifest used for a run to support traceability.

---

## Directory Structure

```
02_prompt_variants/
  readme.md
  prompt_manifest.md
  *.txt
```

Only files that physically exist in the directory are listed here. The authoritative inventory of prompt files and variants is maintained in `prompt_manifest.md`.

---

## Versioning and Modification Rules

- Do not overwrite existing prompt files when comparability is required.
- To introduce a new variant:
  1. Add a new `.txt` file.
  2. Register the variant in `prompt_manifest.md`.
- Keep prompt identifiers stable across variants to support aggregation and comparison.

---

## Relation to Other Components

- **Experimental design and schemas**  
  Defined in `supplement/01_experiment_design/`, including the execution protocol and output schema.

- **Evaluation rules and judging contracts**  
  Specified independently in `supplement/03_evaluation_rules/`, covering the judging procedure and definitions.

- **Results and analyses**  
  Stored under `supplement/04_results/`, including raw outputs, judged records, and aggregated tables.

- **Methodological addenda and controls**  
  Documented in `supplement/05_methodological_addenda_and_controls/`.

- **Tools and utilities**  
  Located in `supplement/tools/`, containing inspection and maintenance helpers.