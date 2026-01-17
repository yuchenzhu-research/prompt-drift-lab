# 05 Methodological Addenda and Controls

This directory contains **supplemental, non-normative methodological notes** provided **for transparency only**.
It clarifies already-frozen design rationale, control assumptions, and comparison boundaries.

**Scope guardrails (read first):**
- **No new experiments, runs, prompts, variables, or evaluation dimensions** are introduced here.
- These notes are **not used to compute, select, or modify** any reported results, scores, or aggregates.
- These notes **do not change** the frozen execution protocol, evaluation rules, or output schemas defined elsewhere.
- If any wording here appears inconsistent with the frozen protocol/results, the frozen protocol/results **take precedence**.

The notes are kept separate so the **measurement interface remains unchanged**, while the study’s design intent and comparison boundaries are made explicit.

---

## Role in the Paper

Materials in this directory serve three limited purposes:

1. **Clarify** design choices that are mentioned but not expanded in the main text.
2. **Describe** the intended separation (e.g., exploratory failure discovery vs. protocolized quantitative measurement) without making additional claims.
3. **List** what comparisons are and are not supported by the frozen setup, to reduce over-interpretation.

These notes are **descriptive** and **non-conclusive**; they aim to improve auditability and reading clarity.

---

## Contents

- `a_b_comparative_rationale.md`

  Describes the intended methodological roles of Prompt Family A and Prompt Family B **as defined in the frozen study setup**.
  It summarizes the comparison boundaries, exclusion criteria, and interpretation constraints.

---

## Language and Authority

- Files in this directory are written in English for reviewer convenience.
- This directory is **supplemental and non-authoritative**. It does **not** override or redefine any frozen protocol, rules, or results.

---

## Relation to Other Components (pointers only)

The following paths are listed for navigation. Their contents are outside the scope of this directory:

- Core experimental protocol and schemas: `supplement/01_experiment_design/`
- Prompt definitions and variants: `supplement/02_prompt_variants/`
- Evaluation rules and failure taxonomy: `supplement/03_evaluation_rules/`
- Results and failure analyses: `supplement/04_results/`