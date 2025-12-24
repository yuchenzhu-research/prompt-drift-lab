# 03 Evaluation Rules (Index)

**You are here:** `03_evaluation_rules/README.md`  
**Upstream:** `01_experiment_design/` → `02_prompt_variants/`  
**Downstream:** `04_results/` (evidence) → `05_summary_and_outlook/` (claims)  
**Sidecar:** `06_methodological_addenda_and_controls/` (controls & rationale)

## Purpose
This folder defines **how evaluation is performed** on existing artifacts (no re-generation):
- what counts as **valid/invalid** evaluation output,
- what the **scoring dimensions** mean,
- what the **judge prompt** is,
- how we **aggregate** judge JSON into CSV tables.

> This README is an **index + boundary contract** (who owns what).  
> It does **not** interpret results. For interpretation and attribution, see: `04_results/03_results_analysis.md`.

---

## Language policy (project-wide)
- Files **without** `_ZH` are **English**.
- Files with `_ZH` are **Chinese**.
- Note: the collected artifacts and many PDFs are **Chinese**, so English readers may not be able to read raw content directly.

---

## Source-of-truth and division of labor (do not mix responsibilities)

### 1) Protocol (process + constraints)
- `EVAL_PROTOCOL.md` / `EVAL_PROTOCOL_ZH.md`  
  Owns: evaluation scope, A/B-blind constraint, allowed metadata keys, what must be traceable.

### 2) Bundle contract & operational rules (what the scripts actually consume)
- `00_evaluation_protocol*.md`  
  Owns: bundle unit (e.g., 16 PDFs), file naming expectations, invalid conditions checklist.

> ⚠️ Naming note: in the current repo, two filenames may contain a trailing space:
> `00_evaluation_protocol.md ` and `01_validity_criteria.md `. Fix them with `git mv` to avoid broken references.

### 3) Validity (binary screening)
- `01_validity_criteria.md` / `01_validity_criteria_ZH.md`  
  Owns: hard fail / strict pass boundaries and invalid flags.

### 4) Scoring dimensions (A–E meaning)
- `02_scoring_dimensions.md` / `02_scoring_dimensions_ZH.md`  
  Owns: dimension intent, bands, common failure patterns, and the “structure-first” rule.

### 5) Judge prompt (exact text used for judging)
- `JUDGE_PROMPT.md` / `JUDGE_PROMPT_ZH.md`  
  Owns: the fixed judge prompt text and strict JSON-only output requirement.
  If conflict exists, **protocol docs take precedence**.

### 6) Aggregation (no re-judging)
- `compute_scores.py` / `compute_scores_ZH.py`  
  Owns: validation checks + aggregation into CSV. Does **not** assign scores.

### 7) Schema (optional)
- `schema/`  
  Optional machine schema(s). Current aggregation primarily relies on `compute_scores.py` checks.

---

## Where judged JSON and CSV tables live (results folder pointers)
This folder defines rules; the **outputs** are stored under:
- Valid evaluations:
  - `04_results/02_cross_model_evaluation/valid_evaluations/main_method_cross_model/`
  - `04_results/02_cross_model_evaluation/valid_evaluations/supporting_method_self_eval/`
- Invalid evaluations:
  - `04_results/02_cross_model_evaluation/invalid_evaluations/`
- Aggregated tables:
  - `04_results/02_cross_model_evaluation/valid_evaluations/summary_tables/`

---

## Non-goals (to prevent README overlap)
- Do not put result interpretation here → use `04_results/03_results_analysis.md`.
- Do not restate experiment design here → use `01_experiment_design/README.md`.
- Do not justify “why Prompt B” here → use `06_methodological_addenda_and_controls/README.md`.
