# Tools

## Scope

This directory contains **offline reproduction and audit utilities**.

- No script in this directory calls external APIs or invokes any LLM.
- All scripts operate only on **stored judge JSON artifacts**.
- No script re-parses or recomputes results from raw model-output PDFs.

---

## Authoritative reproduction entry

### `reproduce_valid_evaluations.py`
This is the **primary reproduction entry point** used to regenerate the reported result tables from stored judge JSON artifacts.

**Inputs (read-only):**
```
supplement/04_results/02_raw_judge_evaluations/
```

**Outputs (materialized):**
```
supplement/04_results/03_processed_evaluations/
```

**Guarantees**
- Deterministic execution (same inputs → same outputs)
- Consumes judge JSON bundles / records only
- File names are preserved verbatim as identifiers; any parsing (if present) is used **only** to materialize grouping keys and **never** affects validity or scoring

**Materialized products**
- Per-file evaluation records under `*/valid_evaluations/`
- Aggregated tables under `*/summary_tables/` (e.g., `scores_long.csv`, `scores_grouped.csv`)

---

## Relation to evaluation rules (`supplement/03_evaluation_rules/`)

Evaluation authority is defined **upstream** under:

```
supplement/03_evaluation_rules/
```

- Rule documents and schemas define validity, structure, and scoring fields.
- This `tools/` directory does **not** define or override evaluation rules.

---

## Non-authoritative utilities

The remaining scripts are retained for inspection and local diagnostics only.
They are **not part of the authoritative reproduction path** and are **not required**
to reproduce the reported result tables.

- `validation_utils/schema_checker.py` — auxiliary schema validation utility
  (offline; **non-authoritative and not invoked by the reproduction script**)
- `scoring_utils/rubric_scorer.py` — failure-label → rubric-score mapper
  (offline; **non-authoritative and not invoked by the reproduction script**)
- `analysis_utils/drift_analyzer.py` — derived, descriptive analysis helpers
  (offline; **non-authoritative and not invoked by the reproduction script**)
- `examples/` contains illustrative input/output examples only
  (**example-only, non-authoritative, and not used in reproduction or scoring**).
- `legacy/` contains archived scripts retained for historical reference only
  (**non-authoritative and not used in the current reproduction path**). In particular,
  `legacy/reproduce_from_pdfs_legacy.py` is an archived script and requires an explicit
  acknowledgement flag to run.

---

## Reproducibility statement

Given identical stored judge JSON artifacts under `supplement/04_results/02_raw_judge_evaluations/`, running `reproduce_valid_evaluations.py` reproduces the processed records and summary tables under `supplement/04_results/03_processed_evaluations/` deterministically.