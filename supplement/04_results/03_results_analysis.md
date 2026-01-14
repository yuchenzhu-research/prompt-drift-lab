# 04 Results — Analysis

## Scope

This directory contains **analysis artifacts derived from evaluation results**.
It defines how evaluation records are grouped, aggregated, and interpreted for reporting.

This directory **does not introduce or modify evaluation rules**.
All analysis steps are derived strictly from artifacts produced under the evaluation protocol.

---

## Input Artifacts

Analysis operates exclusively on the following inputs:

- Aggregated judge outputs under:
  - `supplement/04_results/02_cross_model_evaluation/`
- Evaluation records classified as **valid** according to the evaluation protocol

Records classified as **invalid** are excluded from all quantitative aggregation and are retained only for diagnostic inspection.

---

## Analysis Units and Grouping

Results are grouped by the following dimensions:

- `model`
- `prompt_variant`
- `question_id`
- `trigger_type`

Each analysis unit corresponds to a fixed combination of these fields.
Units are not merged across prompt families or evaluation modes.

---

## Aggregation Rules

For each analysis unit:

- Per-file scores are aggregated into summary statistics
- Aggregation is performed **only over valid records**
- No cross-unit normalization, reweighting, or manual adjustment is applied

All aggregated values must be traceable to the underlying per-file records.

---

## Failure Attribution and Taxonomy

Analysis distinguishes between:

- **Scoring outcomes** (quantitative performance under the rubric), and
- **Protocol-level failures** that render records non-auditable.

Protocol-level failures are identified using **failure flags** (e.g., `PROTOCOL_VIOLATION`, `UNPARSABLE_OUTPUT`) as defined in:

- `supplement/03_evaluation_rules/failure_taxonomy.md`

Narrative groupings (e.g., schema violations, instruction deviation) are used for descriptive reporting only and do not redefine failure labels.

---

## Attribution and Ablation

When attribution is performed, it follows a fixed sequence:

1. Identify the failure flag(s) present
2. State a hypothesized mechanism
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

This directory may contain:

- Per-model and per-variant summary tables
- Failure frequency breakdowns by failure flag
- Diagnostic logs for invalid and excluded records

All derived outputs are stored under this directory and are traceable to upstream artifacts.