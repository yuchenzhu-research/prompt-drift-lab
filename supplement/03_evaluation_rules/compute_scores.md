# Compute Scores — Explanatory Note

## File Role and Scope

This file provides a **conceptual explanation** of the scoring and aggregation logic
originally implemented in `compute_scores.py`.

- This document is **not executable**
- It is **not** an entry point for evaluation or aggregation
- It does **not** define or modify any evaluation rules or JSON contracts

All quantitative results reported in the paper and supplements are **pre-computed and fixed** in:

```
supplement/04_results/03_processed_evaluations/
```

Reviewers are **not expected** to run any scoring scripts to audit the artifact.

---

## Relationship to the Execution Pipeline

- **`tools/reproduce_valid_evaluations.py`**
  - The **only authoritative execution entry point** for evaluation processing
  - Performs schema validation, validity filtering, and score aggregation

- **`compute_scores.py`**
  - **Deprecated**
  - Retained solely for archival inspection of legacy scoring logic
  - Not invoked by the final reproducible pipeline

- **`compute_scores.md` (this file)**
  - A **human-readable explanation** of the scoring design and intent
  - Introduces **no alternative execution paths**

In case of any discrepancy, the behavior of **`tools/reproduce_valid_evaluations.py`** takes precedence.

---

## Design Principles

The scoring logic follows three guiding principles:

1. **Analysis-level reproducibility**  
   Fixed result files, scoring rules, and summary tables are mutually consistent.

2. **Determinism**  
   No external APIs, online services, or non-deterministic components are involved.

3. **Auditability over executability**  
   Scripts exist to support transparency and inspection, not to reproduce experiments.

---

## Conceptual Scoring Flow

At a high level, the scoring and aggregation process consists of:

1. **Inputs**  
   - Schema-valid evaluation records  
   - A fixed scoring rubric defined by the evaluation rules

2. **Validation**  
   - Schema conformance checks  
   - Presence and completeness checks for required fields

3. **Aggregation**  
   - Per-record aggregation according to the rubric  
   - Collapsing multiple judge scores into a single aggregated score per evaluated output

4. **Outputs**  
   - Structured summary files stored under:
     ```
     supplement/04_results/03_processed_evaluations/
     ```

This document intentionally avoids implementation details to prevent
any interpretation as a secondary execution specification.

---

## Safety and Boundary Statements

- This document does **not** provide runnable code
- It does **not** claim end-to-end reproducibility
- It must **not** be used to generate or modify experimental results

All reported results originate exclusively from:

```
supplement/04_results/03_processed_evaluations/
```

---

## Reviewer Reading Guide

To audit the evaluation logic, reviewers may:

1. Read `eval_protocol.md`
2. Read `scoring_dimensions.md`
3. Inspect the fixed result files in `supplement/04_results/`

No script execution is required for consistency or validity checks.

---

## Closing Note

The purpose of this file is to **reduce cognitive overhead**, not to define behavior.

It functions as:
- Design rationale
- Audit annotation
- Engineering commentary

and **not** as an experimental component.