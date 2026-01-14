# A/B Comparative Rationale

## Scope

This document defines the methodological rationale for introducing Prompt Family A and Prompt Family B in the experimental design. Its primary purpose is to motivate the separation between exploratory exposure and protocolized measurement, and to clarify how each family contributes to failure analysis and quantitative evaluation.

This document does **not** introduce evaluation rules and does **not** modify scoring criteria. All observations referenced here are grounded in artifacts produced under the fixed execution protocol defined elsewhere.

---

## Definition of Prompt Families

### Prompt Family A: Exploratory Failure Surface

Prompt Family A is introduced to deliberately expand the observable failure surface under minimal structural constraints. Its role is **diagnostic rather than comparative**.

Characteristics:
- Loosely structured prompt format
- High degrees of freedom in generation
- Intentionally weak or implicit constraint signaling

Family A is designed to expose failure modes that are otherwise suppressed under strict protocolization, including:
- Structural collapse and format instability
- Instruction omission or substitution
- Uncontrolled semantic drift and task rewriting

Outputs from Prompt Family A are logged and inspected qualitatively. They are **not merged into quantitative comparisons** unless explicitly stated, and they do not serve as performance baselines.

---

### Prompt Family B: Protocolized Measurement Anchor

Prompt Family B serves as the **measurement anchor** for all quantitative analysis. It defines a stable and auditable interface between generation and evaluation.

Characteristics:
- Fixed three-section output structure
- Explicit constraint specification
- Stable field boundaries suitable for automated scoring

Family B establishes the reference condition against which controlled perturbations are evaluated. All reported quantitative results and aggregate statistics are derived exclusively from Prompt Family B and its variants.

---

## Comparison Boundaries

Comparisons are conducted under the following constraints:

- Quantitative statistics are computed exclusively within Prompt Family B
- Prompt Family A is not treated as a competing baseline
- No cross-family normalization, ranking, or aggregation is performed

Cross-family observations are reported only as **qualitative evidence** to contextualize observed failure patterns and to motivate protocolized evaluation.

---

## Interpretation Constraints

Comparative observations are interpreted under strict constraints:

- Differences are attributed only when a single factor is modified under an otherwise fixed protocol
- Observations without minimal ablation are recorded as descriptive rather than causal
- Family A observations do not support performance or robustness claims

These constraints prevent exploratory variance from contaminating quantitative conclusions.

---

## Role in Failure Analysis

The A/B separation is central to the failure-oriented design of the study. Prompt Family A broadens the space of observable breakdowns, revealing classes of failures that inform taxonomy construction and diagnostic discussion. Prompt Family B, by contrast, constrains generation sufficiently to make such failures measurable, comparable, and aggregatable.

This division allows failure cases to be treated as first-class empirical observations while preserving the integrity of quantitative evaluation.

---

## Rationale Summary

The A/B design decouples **failure discovery** from **failure measurement**. Prompt Family A functions as an exploratory instrument that surfaces latent failure modes, while Prompt Family B provides a protocolized substrate for controlled analysis. This separation is essential for interpreting drift phenomena without conflating exploratory variance with evaluative signal.