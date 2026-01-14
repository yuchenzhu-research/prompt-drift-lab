# Tools

## Scope

This directory contains **analysis- and reproduction-level utilities** only.  
No script in this directory executes, simulates, or invokes any LLM.

The tools operate exclusively on **already-generated artifacts** (PDFs or
structured JSON) and are designed to support a **deterministic, post-hoc
analysis and reproduction pipeline**.

---

## Authoritative Reproduction Entry

### `reproduce_valid_evaluations.py`

This is the **only authoritative executable entry point** in this directory.

It provides a deterministic, offline execution path to regenerate:

```
supplement/04_results/02_cross_model_evaluation/valid_evaluations/
```

from stored raw PDF outputs under:

```
supplement/04_results/01_raw_model_outputs/
```

**Key properties**
- No external APIs or LLM calls
- Deterministic execution
- Intended solely for artifact executability and auditability

The script regenerates:
- `main_method_cross_model/` (primary evaluation results)
- `supporting_method_self_eval/` (offline structural placeholders)

Files under `supporting_method_self_eval/` are explicitly marked as offline
placeholders and **do not correspond to rerunning self-judging with generator
models**.

---

## Relation to Evaluation Rules (`03_evaluation_rules/`)

The executable reproduction script in this directory is **downstream of** the
formal evaluation contract defined under:

```
supplement/03_evaluation_rules/
```

In particular:
- Evaluation authority is defined by rule documents and schema files in
  `03_evaluation_rules/`
- `03_evaluation_rules/compute_scores.py` provides a **reference
  implementation** of scoring logic
- That reference script is **non-executable for reproduction** and is included
  for transparency and auditability only

`reproduce_valid_evaluations.py` **does not reimplement or override** evaluation
rules; it only applies those rules in a fixed, deterministic manner to
pre-generated artifacts.

---

## Utility and Historical Scripts

The remaining scripts are retained for transparency and inspection. They were
used during development or analysis but are **not required** to reproduce the
main evaluation results:

- `analysis_utils/drift_analyzer.py`  
  Utilities for inspecting prompt-drift and failure patterns.

- `scoring_utils/rubric_scorer.py`  
  Rubric-aligned scoring helpers used during development.

- `validation_utils/schema_checker.py`  
  Schema validation utilities for checking output conformity.

---

## Examples

The `examples/` directory contains illustrative input/output examples only.

These files are **not** used in the reproduction pipeline and are provided
solely for reference and documentation purposes.

---

## Reproducibility Statement

Given identical stored artifacts, all outputs produced by
`reproduce_valid_evaluations.py` are reproducible.

This directory does **not** claim execution-level reproducibility of original
model generations, which were collected via external web-based interfaces.

---

## PDF Parsing Notes

Some raw model outputs are stored as **Chinese-language PDFs**. During offline
text extraction (via `pdfplumber` / `pdfminer`), the following warnings may
appear:

```
Could not get FontBBox from font descriptor because None cannot be parsed as 4 floats
```

These warnings originate from font metadata irregularities in certain PDF
encodings and **do not indicate a failure of text extraction**.

They are benign, non-fatal messages and **do not affect**:
- the extracted textual content used for evaluation
- the structure of regenerated evaluation records
- the determinism or completeness of the reproduction pipeline