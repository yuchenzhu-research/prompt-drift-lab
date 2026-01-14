# Compute Scores — Explanatory Note

## File Role and Scope

This file provides a **conceptual explanation** of the scoring and aggregation logic
implemented in `compute_scores.py`.

- This document is **not executable**
- It is **not** an entry point for evaluation or aggregation
- It does **not** define or modify any evaluation rules or JSON contracts

All quantitative results reported in the paper and supplements are **pre-computed and fixed** in:

```
supplement/04_results/
```

Reviewers are **not expected** to run any scoring scripts to audit the artifact.

---

## Relationship to `compute_scores.py`

- **`compute_scores.py`**
  - The **only implementation** of scoring and aggregation logic
  - Consumes **schema-valid evaluation records** defined by:
    - `schema/eval_record.schema.json`

- **`compute_scores.md` (this file)**
  - A **human-readable explanation** of the above logic
  - Provides design intent and audit context only
  - Introduces **no alternative execution paths**

In case of any discrepancy, the behavior of **`compute_scores.py`** takes precedence.

---

## Design Principles

The scoring logic is designed around the following principles:

1. **Analysis-level reproducibility**
   - Guarantees consistency between fixed outputs, scoring rules, and summary tables

2. **No dependency on external APIs or non-deterministic execution**
   - Model inference and online services are out of scope

3. **Auditable, not runnable**
   - Scripts exist to support transparency and inspection, not to reproduce experiments

---

## Conceptual Scoring Flow

At a high level, the scoring and aggregation process follows these steps:

1. **Inputs**
   - A collection of **schema-valid evaluation records**
   - A fixed scoring rubric defined by the evaluation rules

2. **Validation**
   - Schema conformance checks
   - Presence and completeness checks for required fields

3. **Scoring and Aggregation**
   - Per-record aggregation according to the rubric
   - Construction of structured summary records

4. **Outputs**
   - Structured summary files used in `supplement/04_results/`

This document intentionally avoids implementation details to prevent
any interpretation as a secondary execution specification.

---

## Safety and Boundary Statements

- This document does **not** provide runnable code
- It does **not** claim end-to-end reproducibility
- It must **not** be used to generate or modify experimental results

All reported results originate exclusively from:

```
supplement/04_results/
```

---

## Reviewer Reading Guide

To understand the evaluation and aggregation logic, reviewers may:

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