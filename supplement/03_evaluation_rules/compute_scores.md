# compute scores — explanatory note

## file role and scope

This file explains the scoring and aggregation logic at a conceptual level.

- It is not executable.
- It is not an entry point for evaluation or aggregation.
- It does not define, override, or reinterpret any evaluation rules or JSON contracts.

All quantitative results referenced by the paper and supplements are pre-computed and stored under:

```
supplement/04_results/03_processed_evaluations/
```

Reviewers are not expected to run any scripts to audit this artifact.

---

## how this relates to the pipeline

- `tools/reproduce_valid_evaluations.py`
  - The only script used in the reproducible processing pipeline
  - Performs schema validation, validity screening, and aggregation

- `compute_scores.py`
  - Deprecated
  - Kept for inspection of legacy logic only
  - Not used to produce the final result tables

This file exists to make the aggregation logic easier to read without treating it as a second specification.

If there is any mismatch between this note and the code path used for reproduction, follow:

- `tools/reproduce_valid_evaluations.py`

---

## what gets aggregated

Inputs:
- schema-valid evaluation records
- the scoring dimensions defined in `scoring_dimensions.md`
- the protocol constraints defined in `eval_protocol.md`

Processing steps (conceptual):
1. validate JSON schema conformance
2. apply binary validity screening (see `validity_criteria.md`)
3. aggregate per-record scores according to the rubric
4. write fixed summary tables under:
   `supplement/04_results/03_processed_evaluations/`

This note intentionally avoids implementation details.

---

## boundary statements

- This file does not provide runnable code.
- It does not claim to reproduce model generations.
- It should not be used to regenerate or modify any reported results.

All reported results originate from the fixed files under:

```
supplement/04_results/03_processed_evaluations/
```

---

## reviewer reading guide

To audit the evaluation logic:
1. read `eval_protocol.md`
2. read `scoring_dimensions.md`
3. inspect the fixed result files in `supplement/04_results/`

No script execution is required for consistency checks.

---

## closing note

This file is here to reduce reading overhead.
It is a short design note, not a component of the experiment.