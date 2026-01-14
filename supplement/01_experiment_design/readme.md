# Experiment Design

This directory defines the experimental inputs and design contracts of Prompt Drift Lab. It specifies what is evaluated, how outputs are structured, and how execution is constrained. No results or scoring logic are defined here.

The design is intentionally minimal and failure-oriented: the goal is to make prompt-induced breakdowns observable, traceable, and analyzable under controlled conditions.

---

## What This Directory Defines

- The evaluation question set and its fixed partition
- The required output structure enforced during generation
- The execution protocol used to record experimental runs
- The methodological workflow used to surface drift and failure cases
- Terminology alignment and known threats to validity

All scoring rules and judgment criteria are defined outside this directory.

---

## Evaluation Set and Partitioning

The benchmark consists of four evaluation questions with a fixed split:

- **Q1–Q2** are used exclusively for prompt construction and iteration.
- **Q3–Q4** form a held-out evaluation set used for all reported analyses.
- No quantitative results from Q1–Q2 are reported or aggregated.

This separation is enforced to prevent development–evaluation leakage and to ensure that observed behaviors reflect prompt perturbations rather than task adaptation.

---

## Failure-Oriented Design Rationale

Prompt Drift Lab treats non-compliant outputs as first-class experimental observations rather than noise. The design explicitly preserves and analyzes failure cases, including structural collapse, instruction substitution, constraint violations, and task rewrites.

Failure patterns are used to characterize prompt drift and to compare the robustness of prompt variants under minimal perturbations. This perspective is central to the methodological contribution of the project.

---

## Quick Navigation

- Evaluation questions: `eval_questions_ZH.jsonl` (authoritative), `eval_questions_EN.jsonl` (reference translation)
- Output structure contract: `output_schema.md`
- Execution protocol: `experiment_protocol.yaml`
- Experimental workflow and failure analysis: `design_five_step.md`
- Terminology alignment: `terminology_alignment.md`
- Threats and limitations: `threats_and_limitations.md`

---

## Directory Scope

### Included

- Evaluation question definitions
- Output structure schema
- Execution protocol template
- Experimental workflow documentation
- Terminology alignment
- Known threats and limitations

### Excluded

- Scoring and judging rules (`03_evaluation_rules/`)
- Prompt text and variants (`02_prompt_variants/`)
- Results, tables, or analysis (`04_results/`)

---

## Repository Connections

- Prompt variants and perturbations: `02_prompt_variants/`
- Scoring rules and evaluation rubrics: `03_evaluation_rules/`
- Results, tables, and analysis: `04_results/`

## Methodological Addenda and Controls

Additional methodological checks, controls, and robustness analyses are documented in:

- `05_methodological_addenda_and_controls/`

These materials extend the core protocol without altering the primary evaluation setup or reported results.

## Tools and Utilities

Utility scripts and inspection helpers used for data handling and artifact management are located in:

- `tools/`

These tools do not define experimental logic, scoring rules, or evaluation criteria, and are not required to interpret reported results.