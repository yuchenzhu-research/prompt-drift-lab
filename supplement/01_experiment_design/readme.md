# Experiment Design

This directory defines the experimental inputs and setup documentation for Prompt Drift Lab. It records how experiments are configured, executed, and logged, without defining or interpreting any evaluation or judging rules.

---

## Hard Boundary

- This directory does not define, modify, or interpret any evaluation rules, including scoring scales, validity criteria, failure definitions, or judgment procedures.
- The sole authority for evaluation and judging is `supplement/03_evaluation_rules/`.

The purpose of this directory is to make experimental execution traceable and reproducible: what inputs were used, what output structure was requested, and how runs were produced and recorded.

---

## What This Directory Defines

- Evaluation question files and their fixed partition (development vs. held-out evaluation)
- The output structural layout requested during generation (section names and order only)
- The execution protocol template, including run configuration and output file naming
- Design-level workflow documentation
- Known threats to validity and design limitations

---

## What This Directory Explicitly Does Not Define

- Any scoring or judging rules (see `supplement/03_evaluation_rules/`)
- Any interpretation of output quality, validity, or failure categories
- Any post-hoc relabeling of results or metrics
- Any results, summary tables, or analysis (see `supplement/04_results/`)

---

## Evaluation Set and Partitioning

The benchmark consists of four questions with a fixed split:

- **Q1–Q2**: development-only prompts for iteration and sanity checks
- **Q3–Q4**: held-out evaluation set used for all reported analyses
- No quantitative results from Q1–Q2 are reported or aggregated

This separation is used to reduce development–evaluation leakage and to keep reported behaviors tied to prompt perturbations rather than task adaptation.

---

## Failure-Oriented Design Rationale

This project preserves all generated outputs as experimental observations, including cases that deviate from the requested output structure.

- Raw outputs are stored without manual edits.
- Downstream evaluation determines how such cases are handled according to the fixed evaluation protocol.

This file does not enumerate failure criteria or scoring logic.

---

## Quick Navigation

- Evaluation questions: `eval_questions_ZH.jsonl` (authoritative), `eval_questions_EN.jsonl` (reference translation)
- Output layout (structure only): `output_schema.md`
- Execution protocol (setup only): `experiment_protocol.yaml`
- Experimental workflow description (design-level): `design_five_step.md`
- Threats and limitations (design-level): `threats_and_limitations.md`

---

## Directory Scope

### Included

- Question definitions and the dev/eval split
- Structural output layout specification
- Execution protocol template and naming conventions
- Workflow documentation at the design level
- Design-level threats and limitations

### Excluded

- Evaluation and judging rules: `supplement/03_evaluation_rules/`
- Prompt text and perturbation definitions: `supplement/02_prompt_variants/`
- Results, summary tables, and analysis: `supplement/04_results/`

---

## Repository Connections

- Prompt variants and perturbations: `supplement/02_prompt_variants/`
- Evaluation protocol (single authority): `supplement/03_evaluation_rules/`
- Results and analysis outputs: `supplement/04_results/`

Additional methodological checks and controls are treated as addenda and do not alter the held-out evaluation setup or the fixed evaluation protocol.