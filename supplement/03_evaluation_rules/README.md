# 03 Evaluation Rules

This folder defines the **evaluation-side contract** of the project:
- what counts as valid / invalid output
- how scoring dimensions are defined and applied
- what the judge must output (machine-aggregatable JSON)

> **Single source of truth (EN):** `03_evaluation_rules/EVAL_PROTOCOL.md`  
> If any file conflicts with the protocol, **the protocol wins**.

---

## 0) 30-second start

- Want to understand / change evaluation rules?  
  → Read / edit: `EVAL_PROTOCOL.md`

- Want to see how the judge is instructed (I/O + constraints)?  
  → Read: `JUDGE_PROMPT.md`

- Want dimension explanations (not rules)?  
  → Read: `02_scoring_dimensions.md`

- Want validity criteria explanation?  
  → Read: `01_validity_criteria.md`

- Want to compute summary scores from judged JSON?  
  → Run: `compute_scores.py`

---

## 1) File responsibilities (do not mix roles)

### Authoritative protocol (only place to change rules)
- `EVAL_PROTOCOL.md` — **authoritative evaluation specification (EN)**
- `EVAL_PROTOCOL_ZH.md` — authoritative evaluation specification (ZH)

### Explanations (must not override the protocol)
- `01_validity_criteria.md` / `01_validity_criteria_ZH.md` — explain validity gates
- `02_scoring_dimensions.md` / `02_scoring_dimensions_ZH.md` — explain scoring dimensions

### Judge I/O contract (must follow the protocol)
- `JUDGE_PROMPT.md` / `JUDGE_PROMPT_ZH.md` — A/B-blind, rubric-only, JSON-only output contract

### Aggregation (mechanical, no new rules)
- `compute_scores.py` / `compute_scores_ZH.py` — compute aggregated tables from judged outputs

### Optional / legacy notes
- `00_evaluation_protocol.md` / `00_evaluation_protocol_ZH.md` — background notes (if present).  
  Treat as explanatory; they must not contradict `EVAL_PROTOCOL(.md|_ZH).md`.

### Schema (if used)
- `schema/` — JSON schema and/or related structured specs.

---

## 2) Where results live
This folder is rules & scoring logic only. Results and artifacts live in:
- `04_results/` (raw outputs, judged JSON, and CSV summaries)
