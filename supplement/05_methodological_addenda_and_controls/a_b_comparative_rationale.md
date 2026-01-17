# A/B Comparative Rationale

## Scope

This document **describes** the methodological roles of Prompt Family A and Prompt Family B **as used in the frozen study setup**.
Its purpose is to **clarify the separation** between exploratory exposure and protocolized measurement, and to state the **comparison boundaries** that apply when reading any examples.

**Scope guardrails:**
- **No new experiments, runs, prompts, variables, or evaluation dimensions** are introduced here.
- This document **does not modify** evaluation rules, scoring criteria, or any frozen protocol.
- Any examples mentioned here are **illustrative and non-conclusive** and are **not used** to compute, select, or modify reported results.

---

## Definition of Prompt Families

### Prompt Family A: Exploratory Failure Surface (Illustrative Only)

Prompt Family A is used to expand the observable failure surface under minimal structural constraints.
Its role is **diagnostic and illustrative**, not a competitive baseline.

Characteristics:
- Loosely structured prompt format
- Higher degrees of freedom in generation
- Weaker or implicit constraint signaling

Family A is used to surface failure modes that are harder to observe under stricter protocolized prompting, such as:
- Structural collapse and format instability
- Instruction omission or substitution
- Semantic drift and task rewriting

Outputs from Prompt Family A are logged and inspected qualitatively.
They are **not used** in any reported quantitative results, aggregates, rankings, or cross-model comparisons.

---

### Prompt Family B: Protocolized Measurement Anchor

Prompt Family B serves as the measurement anchor for the study’s **reported quantitative analysis**.
It defines a stable and auditable interface between generation and evaluation.

Characteristics:
- Fixed three-section output structure
- Explicit constraint specification
- Stable field boundaries suitable for automated scoring

All reported quantitative results and aggregate statistics are derived exclusively from Prompt Family B and its frozen variants.

---

## Comparison Boundaries

Comparisons are conducted under the following constraints:

- Quantitative statistics are computed exclusively within Prompt Family B
- Prompt Family A is not treated as a competing baseline
- No cross-family normalization, ranking, or aggregation is performed

Cross-family notes are included only as illustrative examples (non-conclusive) to describe observable failure patterns.
They are **not used** to support or strengthen any reported results.

---

## Interpretation Constraints

When interpreting any comparative observations:

- Differences are attributed only when a single factor is modified under an otherwise fixed protocol
- Observations without minimal ablation are recorded as **descriptive**, not causal
- Family A observations do not support performance, robustness, or generalization claims

These constraints keep exploratory variance **separate from** quantitative reporting.

---

## Role in Failure Analysis

The A/B separation is a design choice used to keep exploratory inspection and protocolized measurement distinct.
Prompt Family A broadens the space of observable breakdowns for **qualitative description**, while Prompt Family B constrains generation so that failures can be **measured and aggregated** under a fixed interface.

---

## Rationale Summary

The A/B design decouples **failure discovery** from **failure measurement**.
Prompt Family A functions as an exploratory instrument that surfaces failure modes for qualitative inspection, while Prompt Family B provides a protocolized substrate for controlled quantitative analysis.
This separation is intended to reduce over-interpretation of exploratory examples as evaluative signal.