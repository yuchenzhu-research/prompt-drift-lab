# 03 Results Analysis

## Scope

This document defines the analysis procedures applied to the evaluation results. It specifies how result files are grouped, aggregated, and interpreted, and clarifies which analyses are considered authoritative.

This document does not introduce new evaluation rules and does not reinterpret scoring criteria. All analysis steps are derived directly from artifacts produced under the evaluation protocol.

---

## Input Artifacts

Analysis operates exclusively on the following artifacts:

- Aggregated judge outputs under `supplement/04_results/02_cross_model_evaluation/`
- Files marked as `valid` according to the evaluation protocol

Artifacts classified as `invalid` are excluded from all quantitative summaries and are retained only for diagnostic inspection.

---

## Analysis Units and Grouping

Results are grouped by the following dimensions:

- `model`
- `prompt_variant`
- `question_id`
- `trigger_type`

Each analysis unit corresponds to a fixed combination of these fields. Units are not merged across prompt families or evaluation modes.

---

## Aggregation Rules

For each analysis unit:

- Per-file scores are aggregated into summary statistics
- Aggregation is performed only over `valid` records
- No cross-unit normalization or reweighting is applied

Aggregated values must be traceable to the underlying per-file records.

---

## Failure Taxonomy

Observed failures are classified into the following categories:

- **A. Schema / format violations**
- **B. Instruction deviation**
- **C. Semantic drift**
- **D. Stability and variance issues**
- **E. Evaluation gaming or rubric exploitation**

Each failure instance is logged with a concrete evidence span extracted verbatim from the corresponding output.

---

## Attribution and Ablation

For each failure category, attribution follows a fixed sequence:

1. Identify the failure category or categories
2. State the hypothesized mechanism
3. Define a minimal ablation that alters a single factor
4. Compare outcomes under identical evaluation settings

Attribution is recorded only when a minimal ablation produces an observable change.

---

## Reproducibility Constraints

All analysis steps satisfy the following constraints:

- Each reported value can be recomputed from stored artifacts
- No manual correction or post-hoc filtering is applied
- All grouping keys are recorded explicitly in result tables

---

## Output Products

The analysis produces:

- Per-model and per-variant summary tables
- Failure frequency breakdowns by category
- Diagnostic logs for invalid and excluded records

All derived outputs are stored under `supplement/04_results/analysis/`.