# 05 Methodological Addenda and Controls

This directory contains **methodological addenda** that support the interpretation
of reported results by clarifying design rationale, control assumptions, and
comparison boundaries. These materials are intentionally separated from the main
experimental protocol to preserve a clean measurement interface while allowing
failure-oriented reasoning to be made explicit.

The documents in this directory do **not** introduce new experimental results and
do **not** modify evaluation protocols, scoring rules, or reported aggregates.
They provide methodological context that is necessary to correctly interpret
observed behaviors, particularly in the presence of systematic failures.

---

## Role in the Paper

Materials in this directory serve three primary purposes in the paper:

1. To motivate design choices that are summarized but not fully expanded in the
   main text.
2. To justify strict separation between exploratory failure discovery and
   protocolized quantitative measurement.
3. To constrain interpretation by explicitly stating what comparisons are and
   are not supported by the experimental setup.

These addenda are referenced to improve auditability and to prevent over- or
mis-interpretation of quantitative results.

---

## Contents

- `a_b_comparative_rationale.md`

  Defines the methodological roles of Prompt Family A and Prompt Family B.
  Prompt Family A is treated as an exploratory instrument for failure discovery,
  while Prompt Family B serves as the measurement anchor for quantitative
  evaluation. The document specifies comparison boundaries, exclusion criteria,
  and interpretation constraints.

Additional methodological notes may be added under the same scope if required
for clarification or control analysis.

---

## Authority and Scope Boundaries

- Files in this directory are written in English and constitute the authoritative
  methodological reference for the A/B separation and associated control logic.
- These materials extend the experimental narrative but do not alter the primary
  execution protocol defined elsewhere.

---

## Relation to Other Components

- Core experimental protocol and schemas: `supplement/01_experiment_design/`
- Prompt definitions and variants: `supplement/02_prompt_variants/`
- Evaluation rules and failure taxonomy: `supplement/03_evaluation_rules/`
- Results and failure analyses: `supplement/04_results/`