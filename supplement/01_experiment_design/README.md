# 01 Experiment Design

This folder defines the **experimental inputs and design artifacts** of the project:
- the evaluation set
- the expected output schema
- the run-level configuration template
- terminology alignment and known threats/limitations

> **Important scope note**
> This folder **does not** define scoring or judging rules.
> Scoring and evaluation rules are defined exclusively in:
> `supplement/03_evaluation_rules/`.
>
> **Authoritative evaluation protocol:**
> `supplement/03_evaluation_rules/EVAL_PROTOCOL_ZH.md`.
>
> English evaluation documents are provided for reviewer readability only and are **non-authoritative**.

---

## 0) 30-second start

- **Modify the evaluation set**
  → `eval_questions_ZH.jsonl` (authoritative)
  → `eval_questions_EN.jsonl` (non-authoritative reference)

- **Check the expected output format**
  → `output_schema_ZH.md` (authoritative)
  → `output_schema.md` (non-authoritative reference)

- **Use or adjust a run configuration template**
  → `experiment_protocol_ZH.yaml` (authoritative)
  → `experiment_protocol.yaml` (non-authoritative reference)

- **Read the compact experimental design rationale**
  → `design_five_step.md`
  
  *(This document is written in English for reviewer readability and reflects the authoritative design decisions.)*

- **Check terminology consistency across the repository**
  → `terminology_alignment_ZH.md` (authoritative)

- **Review known threats and limitations**
  → `threats_and_limitations_ZH.md` (authoritative)
  → `threats_and_limitations.md` (non-authoritative reference)

---

## 1) What belongs here

### Belongs in `01_experiment_design/`
- **Evaluation set**: question content and stable identifiers
- **Output schema**: generator output format contract
- **Experiment protocol template**: run-level settings to be recorded
- **Design rationale**: experimental setup rationale (no results)
- **Terminology alignment**: canonical names used throughout the project
- **Threats & limitations**: known risks and boundaries of the design

### Does NOT belong here
- **Scoring / judging rules** → `supplement/03_evaluation_rules/`
- **Prompt variants / prompt text** → `supplement/02_prompt_variants/`
- **Results, tables, or analysis** → `supplement/04_results/`

---

## 2) Directory map

```
01_experiment_design/
  README.md
  README_ZH.md
  eval_questions_ZH.jsonl
  eval_questions_EN.jsonl
  output_schema_ZH.md
  output_schema.md
  experiment_protocol_ZH.yaml
  experiment_protocol.yaml
  design_five_step.md
  terminology_alignment_ZH.md
  threats_and_limitations_ZH.md
  threats_and_limitations.md
```

---

## 3) Versioning conventions

- Files suffixed with `_ZH` are **authoritative** and define experimental semantics.
- English files are provided as **non-authoritative references** and do not introduce new rules or definitions.
- Question identifiers must remain **stable** across all variants to preserve result comparability.

---

## 4) Connections to the rest of the repository

- **Prompt variants** → `supplement/02_prompt_variants/`
- **Evaluation rules** → `supplement/03_evaluation_rules/`
- **Results** → `supplement/04_results/`

