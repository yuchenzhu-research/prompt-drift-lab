# 03 Evaluation Rules README

This directory defines the **evaluation-side contract** of the project. It specifies:

- what constitutes valid and invalid outputs
- how scoring dimensions are defined and applied
- the required judge output format (machine-aggregatable JSON)

---

## Authority Contract

The English-language files in this directory constitute the **sole authoritative evaluation contract**.

Each component document defines a specific aspect of the evaluation rules under this authority:

- `eval_protocol.md` defines the overall evaluation flow and rule composition
- `validity_criteria.md` defines binary structural validity boundaries
- `scoring_dimensions.md` defines scoring dimensions and scales
- `judge_prompt.md` defines the judge input/output format
- `schema/` defines the machine-enforceable JSON schema

No other documents define or override evaluation authority.

---

## 0 Quick navigation

- Evaluation protocol
  - `eval_protocol.md`

- Judge contract
  - `judge_prompt.md`

- Validity criteria
  - `validity_criteria.md`

- Scoring dimensions
  - `scoring_dimensions.md`

- Failure taxonomy
  - `failure_taxonomy.md`

- Score aggregation
  - `compute_scores.py`
  - `compute_scores.md`

---

## 1 File responsibilities

### Evaluation protocol

- `eval_protocol.md`

### Validity criteria

- `validity_criteria.md`

### Scoring dimensions

- `scoring_dimensions.md`

### Judge contract

- `judge_prompt.md`

### Failure handling

- `failure_taxonomy.md`

### Aggregation

- `compute_scores.py`
- `compute_scores.md`

### Schema

- `schema/`

---

## 2 Results location

This directory defines evaluation rules and scoring logic only.

All results and execution artifacts are stored under:

- `supplement/04_results/`