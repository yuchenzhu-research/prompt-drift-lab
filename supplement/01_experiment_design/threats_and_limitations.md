# Threats to Validity & Limitations

This section discusses the major threats and limitations of Prompt Drift Lab at its
current stage. The goal is to clarify the scope of applicability of the conclusions
and to outline directions for future experimental extensions.

---

## 1. Construct Validity

### 1.1 Boundary of the "Drift" Definition

In this project, *prompt drift* is primarily operationalized as three observable
phenomena: **instruction-following degradation, structural or format breakdown, and
semantic drift (task rewriting, boundary violation, or topic deviation)**. However,
these phenomena are not mutually exclusive. For example, structural breakdown may
result from verbosity overflow rather than a genuine shift in task understanding.

The current approach attempts to distinguish these effects via rubric dimensions,
but classification ambiguity may still arise in edge cases.

### 1.2 Subjectivity of Rubric Dimensions and Scales

The rubric uses a discrete 0–2 scale to evaluate dimensions such as structural
compliance, snapshot constraints, actionability, completeness, and drift failure.
This coarse granularity introduces subjectivity, and correlations may exist between
dimensions (e.g., structural breakdown often coincides with reduced completeness),
which can lead to double-counting or masking of certain failure modes.

Future work should reduce ambiguity through more fine-grained definitions,
illustrative examples, and reporting of inter-dimension correlations and
consistency metrics.

### 1.3 Impact of the Invalid-Sample Definition

In this project, the `invalid` label is strictly reserved for **unscorable outputs**
(e.g., explicit refusal, empty output, severe truncation, or structurally
indeterminate responses), rather than poor performance. While this policy improves
data hygiene, boundary cases may still lead to disagreement in a small number of
samples, affecting the invalid rate and overall distributions.

Future iterations should include more explicit invalid-case examples in the rubric.

---

## 2. Internal Validity

### 2.1 Confounding Factors Beyond Prompt Variations

Even with fixed prompt versions, outputs may still be influenced by factors such as:
conversation context not being fully reset, default system prompts in the UI,
backend model updates, rate-limit–induced truncation, or invisible generation
policies (e.g., hidden safety constraints). The current protocol requires a new
conversation per sample and records visible parameters, but complete isolation of
system-level variation is not achievable.

### 2.2 Prompt Variants Are Not Pure Single-Factor Perturbations

Although the experimental intent is minimal perturbation, prompt variants
(`baseline`, `long`, `weak`, `conflict`) may simultaneously alter multiple aspects
such as length, tone, constraint strength, and degree of conflict. Modifying
multiple dimensions at once weakens causal attribution.

Future work should incorporate finer-grained ablations (e.g., single-sentence or
single-token changes) to improve interpretability.

### 2.3 Rater Bias and Backfilling Bias

When scoring is performed by a single rater or a single judge model, systematic
bias may arise (e.g., consistent leniency or strictness toward certain formats).
Knowledge of the evaluated condition (prompt version or model) may further bias
judgment.

Future mitigation strategies include:
- Blind scoring with hidden version/model labels
- Dual raters with arbitration
- Cross-evaluation using multiple judge models under the same rubric

---

## 3. External Validity

### 3.1 Limited Question Set and Task Coverage

The current question set is small (e.g., four questions, with some runs using only
Q3 and Q4), limiting task and domain coverage. Conclusions may therefore apply
primarily to **structured-output and template-following tasks**, rather than open-
ended QA, code generation, or long-form writing.

Future extensions should expand across:
- Different structure types (tables, JSON, mixed formats, hierarchical templates)
- Different task types (retrieval instruction generation, planning, reasoning,
  constraint conflict)
- Different input lengths and noise levels

### 3.2 Model and Version Transferability

Findings may depend on specific model families, versions, and time windows. In
particular, commercial models undergo continuous updates, which may alter behavior
over time even under identical prompts.

While the protocol encourages recording model versions and time windows, systematic
tests of cross-time consistency are currently lacking. Future work should include:
- Temporal replicates of the same evaluation bundle
- Reference runs using fixed-version APIs or open-source models

### 3.3 Language and Cultural Effects

If evaluation questions and prompts are primarily in Chinese or English, findings
may not fully generalize across languages. Different languages may introduce
varying formatting conventions, perceptions of instruction strength, and safety
policy triggers.

Future work should include bilingual question sets and prompt variants to evaluate
cross-lingual transfer effects.

---

## 4. Conclusion Validity

### 4.1 Sample Size and Uncertainty

With only a single output per condition (`replicate = 1`), variance cannot be
estimated, and it is difficult to distinguish random fluctuation from systematic
drift. More robust comparisons (e.g., `long` vs. `baseline`) require multiple
replicates per cell (recommended N ≥ 3), with reporting of central tendency and
dispersion (e.g., standard deviation, confidence intervals, or quantiles).

### 4.2 Aggregation Metrics and Multiple-Comparison Risk

Comparing multiple dimensions, questions, and models simultaneously increases the
risk of spurious differences. While the current stage is exploratory, stronger
claims will require clearly specified comparison hypotheses and controls for
multiple testing (e.g., pre-registered comparisons or restricted primary analyses).

---

## 5. Reproducibility & Auditability

### 5.1 Alignment Between Records and Artifacts

Inconsistent file naming, missing runtime parameters, or absent question/rubric
version tags can hinder reproducibility and auditability. The current design
addresses this through:
- `experiment_protocol.yaml` as a single source of truth
- Unified file naming conventions
- Eval bundle JSON files that freeze scoring results

Future improvements may include:
- Checksums (e.g., SHA-256) for question sets, rubrics, and protocol files
- Preservation of raw prompt texts and generation environment metadata

### 5.2 Human Intervention and Post-processing

Manual modification of model outputs (e.g., fixing formatting or trimming sections)
contaminates the evidence chain and distorts scoring. The current protocol requires
raw output PDFs to be preserved as primary evidence. Future iterations should
further specify that any cleaning or extraction must retain the original version
and document the transformation rules.

---

## 6. Mitigation Roadmap

To reduce the above threats, the following priorities are recommended:

1) **Increase replicates**: N ≥ 3 per condition, with dispersion reported
2) **Blind and consistency-aware scoring**: dual raters or judge-model cross-evaluation
3) **Finer-grained ablations**: move from coarse variants to sentence- or token-level perturbations
4) **Expanded question coverage**: structure types, task types, and bilingual settings
5) **Cross-time re-evaluation**: rerun fixed bundles across different dates

---

## Current Scope of Conclusions

At the current stage, conclusions primarily apply to:
- Structured-output and template-following tasks
- Exploratory observations on a limited question set and model pool
- Mixed qualitative–quantitative evaluation centered on rubric-based scoring

Until question coverage is expanded, replicate counts are increased, and scoring
consistency is strengthened, results should not be generalized as statements about
overall model capability or definitive model-to-model superiority.

