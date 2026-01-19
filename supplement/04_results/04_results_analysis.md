# 04_results_analysis

This note defines how reported result tables are derived from stored evaluation artifacts.

- It does **not** define or modify evaluation rules.
- It reads only stored evaluation records and produces **derived** summary tables.

---

## Inputs

Primary aggregation inputs (per-file processed records):

- `/supplement/04_results/03_processed_evaluations/<judge_version>/valid_evaluations/**/record_*.json`

Upstream evidence (not recomputed here):

- `/supplement/04_results/02_raw_judge_evaluations/` (raw judge bundles)
- `/supplement/04_results/01_raw_model_outputs/` (raw generator PDFs)

---

## Record inclusion

Numeric aggregation includes only records that satisfy validity criteria defined under:

- `/supplement/03_evaluation_rules/`

Records flagged invalid are excluded from numeric summaries and preserved for inspection.

Excluded record listings are stored at:

- `/supplement/04_results/03_processed_evaluations/<judge_version>/summary_tables/excluded_records.jsonl`

Previously validated records are treated as **immutable inputs** to aggregation. Analyses assume a fixed set of validated records and do not modify or overwrite them.

---

## Grouping keys

Summary statistics are grouped by explicit record fields written in `scores_long.csv`, including:

- `generator_model`
- `prompt_variant`
- `question_id`
- `trigger_type`

All summary tables also carry `judge_version` to prevent merging across judge runs.

---

## Aggregation products

Per-file records are flattened into:

- `scores_long.csv` (one row per evaluated file)

and aggregated into:

- `scores_grouped.csv` (means over valid records per analysis unit)

The `total` column is a **derived** value computed as:

- `total = A_structure + B_snapshot_constraint + C_actionability + D_completeness + E_drift_failure`

No reweighting or manual adjustment is applied.

---

## Outputs (paper-cites location)

For each `<judge_version>`, derived outputs are written under:

- `/supplement/04_results/03_processed_evaluations/<judge_version>/summary_tables/`

This directory includes:

- `scores_long.csv`
- `scores_grouped.csv`
- `excluded_records.jsonl`
- `run_meta.json`

---

## Traceability

Every row in `scores_long.csv` is traceable to a concrete record JSON under:

- `/supplement/04_results/03_processed_evaluations/<judge_version>/valid_evaluations/`

Traceability to the preserved raw PDF is defined as follows:

1) **Primary join keys (canonical)**

- `generator_model`, `question_id`, `prompt_variant`, `trigger_type`

2) **Raw PDF location rule**

- Raw PDFs are stored under `/supplement/04_results/01_raw_model_outputs/<generator_model_dir>/`.
- File naming follows the generation template: `q{question_id}_{prompt_variant}_{trigger_type}.pdf`.

3) **`record.file` semantics by judge version (artifact snapshot)**

- **v0**: `record.file` is a preserved identifier from the raw judge bundle and is not required to be a repository path.
- **v1/v2**: `record.file` is stored as a repository-relative PDF pointer under `01_raw_model_outputs/`.

When `record.file` is not a repository-relative path (v0), the raw PDF is located using the primary join keys and the naming template above.

---

## Failure taxonomy and attribution

This artifact separates two layers:

- rubric score outcomes (A–E)
- protocol-level failures that make a record unusable for aggregation

Protocol-level failure flags follow:

- `/supplement/03_evaluation_rules/failure_taxonomy.md`

Narrative labels (e.g., “schema mismatch”, “instruction deviation”) are descriptive only and do not redefine failure flags.