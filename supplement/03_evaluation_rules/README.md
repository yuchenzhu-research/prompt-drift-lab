# 03 Evaluation Rules

This directory defines the **evaluation-side contract** of the project. It specifies:

- what constitutes valid and invalid outputs
- how scoring dimensions are defined and applied
- the required judge output format (machine-aggregatable JSON)

Files suffixed with `_ZH` define the **only authoritative evaluation semantics**.
English files are provided strictly as **non-authoritative references** for
reviewer readability.

**Authoritative source of truth**

- `03_evaluation_rules/EVAL_PROTOCOL_ZH.md`

---

## 0 Quick navigation

- Authoritative evaluation rules
  - `EVAL_PROTOCOL_ZH.md`

- English reference of the protocol
  - `EVAL_PROTOCOL.md`

- Judge input/output contract
  - `JUDGE_PROMPT.md`

- Scoring dimension explanations
  - `02_scoring_dimensions.md`

- Validity criteria explanations
  - `01_validity_criteria.md`

- Score aggregation script
  - `compute_scores.py`

---

## 1 File responsibilities

### Authoritative protocol

- `EVAL_PROTOCOL_ZH.md` — the only authoritative and executable evaluation specification

### Reference documents

- `EVAL_PROTOCOL.md` — English reference of the protocol
- `01_validity_criteria.md` / `01_validity_criteria_ZH.md`
- `02_scoring_dimensions.md` / `02_scoring_dimensions_ZH.md`

### Judge contract

- `JUDGE_PROMPT.md` / `JUDGE_PROMPT_ZH.md`

### Aggregation

- `compute_scores.py` — computes aggregated tables from judged outputs

### Schema

- `schema/`

---

## 2 Results location

This directory defines evaluation rules and scoring logic only.

All results and execution artifacts are stored under:

- `supplement/04_results/`