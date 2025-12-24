# Summary and Outlook (Prompt Drift Lab)

> This document summarizes the completed experimental findings, clarifies the methodological boundaries of the current version, and outlines **future research directions without exceeding existing evidence**.
>
> **Important clarification**: The current version of this project **does not implement any automated perturbation generator or large-scale prompt scanning**. All content below is strictly aligned with **experiments that have been completed and fully materialized in the repository**, and does not include any unimplemented methods or tools.

---

## 1. What This Project Has Accomplished

This project investigates **Prompt Drift**—systematic deviations in large language model behavior that arise when, *holding the task constant*, prompts undergo minor changes in structure, phrasing, or constraint formulation. Such drift manifests in **instruction-following behavior, output structure stability, and semantic fidelity**.

Concretely, the project establishes a **minimal yet fully reproducible experimental loop**:

- **Input side (Prompt Design)**: Under fixed tasks and question sets, a small number of manually designed, interpretable prompt variants are constructed to deliberately expose failures in instruction following and structural stability.
- **Output side (Model Outputs)**: Raw outputs produced by different models under different prompt conditions are preserved in full (PDF), and aggregated into structured result summaries (CSV).
- **Evaluation side (Evaluation)**: Cross-model judging is adopted as the primary evaluation method, with self-judging used only as an auxiliary control. Both are governed by explicit evaluation protocols and judge prompts (see `03_evaluation/`).

> **Boundary statement**: All prompt drift phenomena reported in this project arise solely from **manually designed prompt variants**. The current version does not rely on automated perturbations, random transformations, or large-scale prompt enumeration.

---

## 2. Scope of the Main Experiment and Methodological Choices

To avoid misinterpretation, the repository clearly distinguishes between different experimental roles:

- **Main experiment (reproducible)**: Systematic evaluation and statistical aggregation are conducted using `Prompt B` and its manually constructed variants (`long`, `weak`, `conflict`).
- **Pilot exploration**: `Prompt A` is used only for early-stage exploration and failure discovery, and is explicitly excluded from all quantitative comparisons.

**Rationale for this choice**: Selecting `Prompt B` as the main experimental baseline is not arbitrary. It follows from pilot comparisons showing superior **executability, structural stability, and auditability** relative to Prompt A. The supporting evidence and decision trail are documented in the `06_` directory.

---

## 3. Key Observations Supported by Completed Experiments

Based on `summary.csv` and grouped evaluation results, the current version of the project supports the following observations, **without extending beyond the available evidence**:

1. **Even a very small number of manually designed prompt variations can induce substantial changes in instruction following and structural stability**.
2. **Longer or more detailed prompts do not guarantee higher stability**; in some cases, they instead dilute constraints or trigger fallback behaviors.
3. **Weakening constraint language (e.g., replacing *must* with *should*) significantly increases the likelihood of drift**.
4. **Prompt variants containing internal tension or conflicting instructions more readily expose implicit priority-selection behaviors in models**.

---

## 4. Role of External Research (Interpretive Context Only)

This section serves solely to align the observed phenomena with concepts discussed in existing literature, and **does not imply that the present project implements, reproduces, or compares against those methods**:

- prompt brittleness / prompt sensitivity
- instruction-following stability
- format robustness

Such work provides interpretive context for why LLM outputs may exhibit pronounced behavioral shifts under minimal prompt changes, even when input semantics remain nearly constant.

---

## 5. Methodological Limitations and Future Work (Strictly Separated)

### 5.1 Explicit Limitations of the Current Version

- Prompt variations are entirely manually designed, covering a limited portion of the prompt space.
- No automated perturbation, randomization, or systematic scanning mechanisms are included.
- Conclusions are valid only within the current prompt space and evaluation protocol.

### 5.2 Possible Directions for Future Extensions (Not Implemented)

> The following items are **potential future research directions only** and are not part of the current project implementation:

- Any introduction of automated perturbation generators or large-scale prompt scans should be treated as a **separate version or independent experimental report**, and must not be mixed with the quantitative conclusions of the current version.

---

## 6. Project Positioning Summary

The core contribution of this project lies in:

- **Treating prompt variation as an experimental variable rather than a tuning trick**;
- **Demonstrating the existence and types of prompt drift through a small number of interpretable controlled comparisons**;
- **Ensuring that all claims are auditable and reproducible through a disciplined file structure and explicit protocols**.

Accordingly, Prompt Drift Lab is not intended as a comprehensive benchmark, but as a **minimal research artifact with clearly defined boundaries and evidence-responsible claims**.