# EVAL_PROTOCOL

> **Authoritative Evaluation Specification (EN)**  
> This document is the **single source of truth** for evaluation rules used in this repository.

---

## 0. Scope & Authority
- This file **defines** all official evaluation rules, dimensions, scoring bands, and validity requirements.
- In case of any inconsistency, **this file takes precedence**.

### Related (Non-authoritative) Documents
The following documents **do not modify** the rules defined here:
- `01_validity_criteria.md` — explains pass/fail validity gates.
- `02_scoring_dimensions.md` — explains the intent of each scoring dimension.
- `JUDGE_PROMPT.md` — defines the judge I/O contract and constraints.
- `compute_scores.py` — aggregates scores mechanically.

---

## 1. Evaluation Inputs
- `question`
- `model_output`
- `rubric` (dimensions, definitions, bands)
- `meta` (recording only; must not influence scoring)

---

## 2. Validity Gates
- Outputs failing **hard validity** checks may be marked invalid before scoring.
- Validity criteria are **defined here** and **explained** in `01_validity_criteria.md`.

---

## 3. Scoring Rules
- All scores **must** follow the dimensions and bands specified in this protocol.
- Judges **must not** add, remove, or redefine dimensions.

---

## 4. Blindness & Independence
- Evaluation is **A/B-blind**: prompt content and prompt variants are not visible to judges.
- No cross-sample comparison is allowed.

---

## 5. Output Contract
- Judge outputs **must** conform to the JSON schema defined by this protocol.
- Top-level keys are fixed and machine-aggregatable.

---

## 6. Change Policy
- Any change to evaluation rules **must be made in this file**.
- Explanatory documents may be updated for clarity but **cannot override** this protocol.
