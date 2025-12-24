# 01 Experiment Design

This folder defines the **experimental inputs and versioned design artifacts** of the repo:
- the evaluation set (questions)
- the expected output schema
- the run-level configuration template (protocol)
- terminology alignment and known threats/limitations

> This folder **does not** define scoring rules.
> Scoring rules live in: `03_evaluation_rules/` (authoritative: `EVAL_PROTOCOL.md`).
> Results live in: `04_results/`.

---

## 0) 30-second start

- Want to change the evaluation set (questions)?
  → `eval_questions_EN.jsonl` (EN) / `eval_questions_ZH.jsonl` (ZH)

- Want to understand the expected output format?
  → `output_schema.md` / `output_schema_ZH.md`

- Want a run configuration template (models, sampling params, etc.)?
  → `experiment_protocol.yaml` / `experiment_protocol_ZH.yaml`

- Want a compact “design rationale” document?
  → `design_five_step.md` / `design_five_step_ZH.md`

- Want terminology consistency across the repo?
  → `terminology_alignment.md` / `terminology_alignment_ZH.md`

- Want known threats/limitations (for writeup)?
  → `threats_and_limitations.md` / `threats_and_limitations_ZH.md`

---

## 1) What belongs here (and what does not)

### Belongs in `01_experiment_design/`
- **Eval set**: question content + stable ids
- **Output schema**: what generators must output (format contract)
- **Experiment protocol template**: run-level settings to be recorded
- **Design rationale**: why this setup (high-level, not results)
- **Terminology alignment**: canonical names used throughout
- **Threats & limitations**: known risks and boundaries

### Does NOT belong here
- **Scoring / judging rules** → `03_evaluation_rules/`
- **Prompt variants / prompt text** → `02_prompt_variants/`
- **Results, tables, analysis** → `04_results/`

---

## 2) Directory map (design artifacts)

```
01_experiment_design/
  README.md
  README_ZH.md
  eval_questions_EN.jsonl
  eval_questions_ZH.jsonl
  output_schema.md
  output_schema_ZH.md
  experiment_protocol.yaml
  experiment_protocol_ZH.yaml
  design_five_step.md
  design_five_step_ZH.md
  terminology_alignment.md
  terminology_alignment_ZH.md
  threats_and_limitations.md
  threats_and_limitations_ZH.md
```

---

## 3) Versioning conventions (recommended)

- Eval set files are versioned by filename or by a `eval_set_version` field recorded at runtime.
- Question ids should be **stable** (e.g., `q1`, `q2`...) so results remain comparable across runs.
- Any change that affects comparability should be documented in:
  - `design_five_step(.md|_ZH)` and/or release notes / commit message.

---

## 4) How this connects to the rest of the repo

- **Prompt variants** are defined in: `02_prompt_variants/`
- **Evaluation rules** are defined in: `03_evaluation_rules/`
- **Results** (raw outputs, judged JSON, summary CSV) are stored in: `04_results/`