# 04 Results — Analysis

## Scope

This directory contains **analysis artifacts derived from processed evaluation results**.
It specifies how evaluation records are grouped and aggregated for reporting.

This directory **does not introduce or modify evaluation rules**.
All analysis steps operate strictly on artifacts produced under the evaluation protocol.

---

## Authoritative Input Artifacts

Analysis operates exclusively on **processed evaluation records** located under:

```
supplement/04_results/03_processed_evaluations/
```

These records are generated deterministically from stored judge outputs under:

```
supplement/04_results/02_raw_judge_evaluations/
```

No analysis step reads from raw model outputs or PDF files.

---

## Validity and Record Selection

Only evaluation records that satisfy the structural and protocol-level validity criteria
specified in `supplement/03_evaluation_rules/` are included in quantitative aggregation.

Records flagged as invalid (e.g., `PROTOCOL_VIOLATION`, `UNPARSABLE_OUTPUT`) are excluded
from numeric summaries and retained solely for diagnostic inspection.

---

## Analysis Units and Grouping

Results are grouped by explicit record fields:

- `model`
- `prompt_variant`
- `question_id`
- `trigger_type`

Each analysis unit corresponds to a fixed combination of these fields.
Units are not merged across prompt families, judge versions, or evaluation modes.

---

## Aggregation Rules

For each analysis unit:

- Per-file scores are aggregated into summary statistics
- Aggregation is performed **only over valid records**
- No cross-unit normalization, reweighting, or manual adjustment is applied

All aggregated values remain traceable to underlying per-file evaluation records.

---

## Failure Attribution and Taxonomy

Analysis distinguishes between:

- **Scoring outcomes**, defined by rubric-based numeric fields, and
- **Protocol-level failures** that render records non-auditable.

Protocol-level failures are identified using failure flags defined in:

- `supplement/03_evaluation_rules/failure_taxonomy.md`

Narrative groupings (e.g., schema violations, instruction deviation) are used
for **descriptive reporting only** and do not redefine failure labels.

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

- Summary tables grouped by model, prompt variant, or question
- Failure frequency breakdowns by failure flag
- Diagnostic logs for invalid or excluded records

All derived outputs stored under this directory remain fully traceable to
processed evaluation artifacts upstream.