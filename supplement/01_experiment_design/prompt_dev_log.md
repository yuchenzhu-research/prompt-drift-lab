# Prompt Development Log

This document records the **prompt development process** used in this project.
It serves as an **audit log** for how the base prompt evolved prior to evaluation.

The purpose of this log is to make the development process **explicit, bounded, and inspectable**,
not to report performance improvements or quantitative results.

---

## Scope and Usage

- This log documents **prompt construction and revision only**.
- All observations in this file are based on the **development set (Q1–Q2)**.
- **No quantitative results from this stage are reported or aggregated** in the paper.
- All reported experimental results are derived exclusively from the **held-out evaluation set (Q3–Q4)**.

---

## Base Prompt Versions

- **Base A**: initial prompt version, used prior to development-stage revisions.
- **Base B**: revised prompt version obtained after development-stage repairs.

The transition from Base A to Base B is treated as a **failure-driven repair process**,
not as performance tuning or optimization.

---

## Observed Failure Patterns (Development Stage)

The following failure patterns were observed when applying **Base A** to the development set (Q1–Q2).
These observations are qualitative and are not used for scoring or comparison.

1. **Structural omission**  
   Required output sections were missing or merged, breaking the expected three-part structure.

2. **Uncontrolled verbosity**  
   The fact snapshot frequently exceeded the intended length or included explanatory content.

3. **Instruction ambiguity**  
   In cases of multiple constraints, the model did not reliably resolve instruction priority.

---

## Repair Actions Applied

Each repair below corresponds directly to one or more observed failure patterns.

1. **Explicit structural ordering**  
   The required output sections were explicitly ordered and named in the prompt.

2. **Hard constraint on snapshot length**  
   A strict upper bound was imposed on the fact snapshot, along with a prohibition on explanatory language.

3. **Constraint priority clarification**  
   The prompt was revised to clarify the precedence among structural, formatting, and content constraints.

These changes were applied conservatively and are limited to addressing observed failures.

---

## Non-Goals and Exclusions

- No prompt variants were evaluated or selected based on quantitative performance at this stage.
- No comparisons between Base A and Base B are reported.
- No evaluation rules or scoring criteria were modified during prompt development.

---

## Relation to Evaluation Stage

- **Base B** is treated as a fixed input for all evaluation experiments.
- All prompt variants and ablations are derived from Base B and evaluated only on Q3–Q4.
- The development stage does not influence evaluation-stage aggregation or conclusions.

This separation is enforced to prevent development–evaluation leakage and to preserve the interpretability of evaluation results.

