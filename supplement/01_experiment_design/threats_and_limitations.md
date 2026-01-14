# Threats to Validity and Limitations

This document specifies the scope boundaries and known limitations of the current experimental design and evaluation protocol. All items listed below describe identified constraints of the study rather than speculative risks.

---

## 1. Construct Validity

### 1.1 Operational Scope of Drift

In this project, prompt drift is operationalized through observable behaviors including instruction-following degradation, structural or format breakdown, and semantic deviation from the specified task. These behaviors may co-occur and are evaluated independently by rubric dimensions. The protocol does not attempt unique causal attribution in overlapping cases.

### 1.2 Rubric Resolution

Evaluation uses a discrete 0–2 scale across dimensions such as structural compliance, snapshot constraints, actionability, completeness, and drift-related failures. This resolution supports relative comparison across conditions rather than fine-grained measurement. Dimension correlations are recorded descriptively without assuming statistical independence.

### 1.3 Invalid Outputs

The invalid label is reserved for unscorable outputs (e.g., explicit refusal, empty output, severe truncation, or indeterminate structure). Low-quality but structurally scorable outputs are not classified as invalid. Borderline cases are resolved by rubric criteria rather than ad hoc judgment.

---

## 2. Internal Validity

### 2.1 System-Level Factors

Model outputs may be affected by system-level factors beyond prompt variation, including backend updates, safety enforcement, truncation, and session initialization. Each sample is generated in an independent session with recorded visible parameters. Unobservable system factors are treated as part of the execution environment.

### 2.2 Multi-Factor Prompt Variants

Defined prompt variants (baseline, long, weak, conflict) simultaneously modify multiple attributes such as length, constraint strength, and conflict degree. Results are interpreted as associations across conditions rather than isolated causal effects.

### 2.3 Scoring Bias

Scoring follows a single fixed rubric and process, which may introduce systematic bias or rater effects. Raw outputs and scoring records are preserved to enable auditability. The protocol does not claim elimination of such effects.

---

## 3. External Validity

### 3.1 Task Coverage

The evaluated tasks focus on structured-output and template-following scenarios. Findings do not generalize to open-ended question answering, code generation, or long-form writing.

### 3.2 Model and Time Dependence

Observed behaviors depend on specific model versions and execution windows. While model identifiers and timestamps are recorded, the protocol does not perform systematic cross-time consistency testing.

### 3.3 Language Scope

The evaluation primarily uses Chinese-language questions. Language-specific conventions may influence formatting preferences and instruction interpretation. Conclusions are not generalized across languages.

---

## 4. Conclusion Validity

### 4.1 Replication Limits

Each experimental condition currently produces a single output. Variance estimation and confidence intervals are therefore not reported, and findings represent individual realizations rather than distributional properties.

### 4.2 Multi-Dimensional Comparison

Comparisons across questions, models, and scoring dimensions are descriptive. No significance testing or multiple-comparison correction is applied.

---

## 5. Reproducibility and Auditability

### 5.1 Artifact Alignment

A single execution protocol, unified naming conventions, and frozen evaluation bundles are used to support reproducibility and auditability.

### 5.2 Raw Output Preservation

All model outputs are stored in their original form without manual modification. Scoring is performed directly on raw outputs to maintain an intact evidence chain.