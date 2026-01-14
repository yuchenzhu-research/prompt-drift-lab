# 02 Prompt Variants

This directory contains the **generator-side prompt variants** used in the prompt drift experiments. All executable prompts are written in **Chinese** and are used verbatim during experimental execution. English content in this file is provided solely for reviewer comprehension and does not constitute executable prompt artifacts.

This directory does **not** include judge prompts, scoring logic, or evaluation rules. All judge-side components are defined under `supplement/03_evaluation_rules/`.

---

## Prompt Language and Authority

- All `.txt` prompt files in this directory are authored in **Chinese**.
- These Chinese prompt files are the **only authoritative inputs** used during experimental execution.
- English descriptions below are **semantic paraphrases**, not line-by-line translations, and are provided for reviewer readability only.

---

## Prompt Variants (English Paraphrases)

The following sections summarize the intent and structural role of each prompt variant. They are not executable instructions and should not be interpreted as alternative prompt definitions.

### 1. Baseline (A — exploratory)

A minimal instruction that specifies the required three-section output format with concise structural constraints. This variant is primarily used for early pipeline validation and qualitative failure discovery. Unless explicitly stated, it is excluded from aggregated quantitative analysis.

### 2. Structured Baseline (B — primary)

A fully specified prompt that enforces the three-section output contract using explicit structural cues and constraint signaling. This variant serves as the **primary experimental anchor** for quantitative evaluation and cross-variant comparison.

### 3. Conflict

A perturbation of the structured baseline that introduces mutually competing or contradictory instructions. This variant probes the model’s ability to resolve instruction priority while maintaining structural compliance.

### 4. Long

A verbosity-inflated variant of the structured baseline that adds redundant explanations and extended guidance. This variant stresses attention allocation and constraint retention under increased prompt length.

### 5. Weak

A constraint-relaxed variant in which explicit structural signals are softened or partially removed. This variant tests sensitivity to under-specified instructions and reduced enforcement strength.

---

## Manifest Authority and Auditability

- `prompt_manifest.md` is the **single source of truth** for the prompt inventory and variant roles.
- Prompt files listed in the manifest are treated as **preserved execution assets** and must not be modified in place.
- Result directories may snapshot the exact manifest used for a run to support auditability and traceability.

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

- Do not silently overwrite existing prompt files if comparability is required.
- To introduce a new variant:
  1. Add a new `.txt` file.
  2. Register the variant in `prompt_manifest.md`.
- Keep prompt identifiers stable across variants to support aggregation and comparison.

---

## Relation to Other Components

- **Experimental design and schemas**  
  Defined in `supplement/01_experiment_design/`, including the execution protocol,
  output schema, and failure-oriented workflow description.

- **Evaluation rules and judging contracts**  
  Specified independently in `supplement/03_evaluation_rules/`, covering scoring
  dimensions, validity criteria, and failure taxonomy.

- **Results and analyses**  
  Stored under `supplement/04_results/`, including raw outputs, scored records,
  aggregated tables, and failure case analyses derived from the defined protocols.

- **Methodological addenda and controls**  
  Documented in `supplement/05_methodological_addenda_and_controls/`, providing
  supplementary checks, controls, and robustness analyses that extend but do not
  alter the primary evaluation setup.

- **Tools and utilities**  
  Located in `supplement/tools/`, containing inspection and maintenance helpers
  that do not define experimental logic, prompt content, or evaluation criteria.