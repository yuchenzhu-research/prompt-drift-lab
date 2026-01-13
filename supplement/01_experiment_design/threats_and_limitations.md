# Threats to Validity and Limitations

This section defines the scope boundaries and known constraints of Prompt Drift Lab at its current stage. All items below describe **identified limitations** of the experimental design and evaluation protocol, rather than speculative risks or disclaimers.

---

## 1. Construct Validity

### 1.1 Operational Boundary of the "Drift" Definition

In this project, *prompt drift* is operationalized as three observable phenomena: **instruction-following degradation, structural or format breakdown, and semantic drift (task rewriting, boundary violation, or topic deviation)**. These phenomena are not mutually exclusive. For example, structural breakdown is sometimes triggered by verbosity overflow rather than a change in task understanding.

The current protocol distinguishes these behaviors using rubric dimensions. In boundary cases, a single sample may be recorded under multiple failure categories. The protocol does not enforce a unique causal attribution for such samples.

---

### 1.2 Rubric Resolution and Dimension Interdependence

The rubric uses a discrete 0–2 scale to evaluate dimensions including structural compliance, snapshot constraints, actionability, completeness, and drift-related failures. This resolution is designed for **relative comparison across conditions**, not fine-grained performance measurement.

Several dimensions are empirically correlated (e.g., structural breakdown frequently coincides with reduced completeness). The protocol records and aggregates dimensions independently and does not assume statistical independence or apply composite weighting.

---

### 1.3 Definition of Invalid Samples

The `invalid` label is strictly reserved for **unscorable outputs**, including explicit refusal, empty output, severe truncation, or structurally indeterminate responses. It is not used to represent low-quality but scorable outputs.

In boundary cases, the distinction between an invalid sample and an extremely low score is governed by rubric rules rather than subjective judgment. The protocol documents this distinction through explicit criteria and examples, without claiming full elimination of disagreement.

---

## 2. Internal Validity

### 2.1 System-Level Factors Beyond Prompt Variations

Even when prompt variants are fixed, model outputs are influenced by system-level factors such as conversation state resets, default system prompts, backend model updates, rate-limit–induced truncation, and safety-policy enforcement. The protocol requires each sample to be generated in an independent session and records all visible parameters.

System-level factors that are not externally observable remain outside experimental control and are treated as part of the operating environment.

---

### 2.2 Prompt Variants as Multi-Factor Perturbations

Although the design targets minimal perturbations, the defined prompt variants (`baseline`, `long`, `weak`, `conflict`) simultaneously alter multiple attributes, including length, tone, constraint strength, and conflict degree.

Accordingly, results are interpreted as **associations across experimental conditions**, not as estimates of isolated causal effects.

---

### 2.3 Scoring Bias and Rater Effects

Scoring is executed through a single fixed rubric and scoring process, which may introduce systematic bias (e.g., consistent strictness toward certain formats). Knowledge of the evaluated condition may further influence judgment.

The protocol treats the scoring process as part of the experimental configuration and preserves raw outputs and scoring records for auditability. It does not claim elimination of rater effects.

---

## 3. External Validity

### 3.1 Task Coverage and Question Set Size

The evaluated question set is limited in size and focuses primarily on structured-output and template-following tasks. Conclusions are restricted to this task category and do not extend to open-ended question answering, code generation, or long-form writing.

---

### 3.2 Model, Version, and Time Dependence

Observed behaviors depend on specific model families, versions, and execution time windows. Commercial models are subject to continuous updates, which may alter behavior under identical prompts.

The protocol records model identifiers and execution timestamps but does not provide systematic cross-time consistency testing.

---

### 3.3 Language and Cultural Scope

The current evaluation primarily uses Chinese-language prompts and questions. Language-specific conventions may influence formatting preferences, perceived instruction strength, and safety-policy triggers.

The protocol does not generalize conclusions across languages.

---

## 4. Conclusion Validity

### 4.1 Replicate Count and Variance Estimation

Each experimental condition currently generates a single output. As a result, the protocol does not estimate variance or confidence intervals, and findings represent single realizations rather than distributional properties.

---

### 4.2 Multi-Dimensional Comparison Limits

Comparisons across multiple dimensions, questions, and models are descriptive. The protocol does not apply significance testing or control for multiple comparisons.

---

## 5. Reproducibility and Auditability

### 5.1 Alignment Between Records and Artifacts

The protocol enforces a single source of truth through `experiment_protocol.yaml`, unified naming conventions, and frozen evaluation bundle records. These measures are intended to support reproducibility and auditability.

---

### 5.2 Raw Output Preservation

All model outputs are preserved in their original form without manual correction or formatting adjustments. Scoring is performed directly on raw outputs to maintain an intact evidence chain.

---

## Scope of Applicability

Conclusions from this project apply only to:

- Structured-output and template-following tasks
- Exploratory evaluations on a limited question set and model pool
- Rubric-centered qualitative–quantitative assessment

Results should not be interpreted as statements about overall model capability or comprehensive model-to-model comparison.
