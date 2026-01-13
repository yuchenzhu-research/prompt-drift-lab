# A/B Comparative Rationale

## Scope

This document defines the methodological rationale for introducing Prompt Family A and Prompt Family B in the experimental design. It specifies the roles of each family, the comparison boundaries, and the constraints under which comparative observations are interpreted.

This document does not introduce evaluation rules and does not modify scoring criteria. All observations described here are grounded in artifacts produced under the fixed evaluation protocol.

---

## Definition of Prompt Families

### Prompt Family A: Exploratory Baseline

Prompt Family A is used as an exploratory baseline to expose a wide range of failure modes under minimal structural constraints.

Characteristics:
- Loosely structured prompt format
- High degrees of freedom in generation
- Suitable for early-stage observation of format instability, instruction omission, and uncontrolled semantic drift

Family A outputs are logged and inspected qualitatively. They are not merged into quantitative comparisons unless explicitly stated.

---

### Prompt Family B: Protocolized Anchor

Prompt Family B serves as the protocolized anchor for all quantitative analysis.

Characteristics:
- Fixed three-section structure
- Explicit constraint specification
- Stable field boundaries suitable for automated evaluation

Family B is used to establish a reproducible baseline against which controlled perturbations are evaluated.

---

## Comparison Boundaries

Comparisons are conducted under the following constraints:

- Quantitative statistics are computed exclusively within Prompt Family B
- Prompt Family A is not treated as a competing baseline
- No cross-family normalization or ranking is performed

Cross-family observations are reported only as qualitative evidence of failure patterns.

---

## Interpretation Constraints

Comparative observations are interpreted under strict constraints:

- Differences observed across prompt variants are attributed only when a single factor is modified
- Observations without a minimal ablation are recorded as descriptive, not causal
- Family A observations do not support performance claims

---

## Rationale Summary

The A/B design separates exploratory exposure from protocolized measurement. Prompt Family A expands the observable failure surface, while Prompt Family B provides a stable reference for controlled analysis. This separation prevents uncontrolled variance from contaminating quantitative conclusions.

