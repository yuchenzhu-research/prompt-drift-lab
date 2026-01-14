# 03 Evaluation Rules

This directory defines the **evaluation-side contract** of the project.
It specifies **what is evaluated**, **how validity is determined**, and **how scores are defined and aggregated**.

This directory is **rule-defining only**. It is **not** an execution or reproduction entry point.

---

## Authority Contract

The English-language files in this directory constitute the **sole authoritative evaluation contract**.

Each component document defines a distinct, non-overlapping aspect of the evaluation rules:

- `eval_protocol.md` — overall evaluation flow and rule composition
- `validity_criteria.md` — binary structural validity boundaries
- `scoring_dimensions.md` — scoring dimensions and scales
- `judge_prompt.md` — judge input/output contract
- `failure_taxonomy.md` — classification of evaluation failures
- `schema/` — machine-enforceable JSON schema for judge outputs

No other documents define, override, or extend evaluation authority.

---

## Reference Implementation (Non-executable)

### `compute_scores.py`

`compute_scores.py` provides a **reference implementation** of the scoring and aggregation logic
specified by the evaluation rules in this directory.

It is included **for transparency and auditability only**.

**Important clarifications:**
- This file is **not** an executable reproduction script
- Reviewers are **not expected** to run this script
- Numerical results are **not regenerated** from this file

The authoritative definitions are given by the rule documents and schema listed above.

### `compute_scores.md`

This document provides a **human-readable explanation** of the aggregation logic
implemented in `compute_scores.py`.

It serves as the primary reference for understanding how per-item scores are
combined and summarized.

---

## File Responsibilities

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

### Score aggregation (reference only)
- `compute_scores.py`
- `compute_scores.md`

### Schema (authoritative)
- `schema/`

---

## Results and Execution Artifacts

This directory defines **rules and reference logic only**.

All execution artifacts and fixed results are stored under:

```
supplement/04_results/
```

Executable reproduction is provided separately under:

```
supplement/tools/reproduce_valid_evaluations.py
```