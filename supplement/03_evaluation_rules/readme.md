# 03 evaluation rules

This directory defines the evaluation-side contract for the project:
what the judge must output, what counts as valid, and how scores are interpreted.

This is rule documentation. It is not where results are produced.

---

## where to start

1. `eval_protocol.md` — how evaluation records are screened and used
2. `judge_prompt.md` — what the judge is asked to do and what JSON it must return
3. `schema/` — the JSON schema enforced for judge outputs
4. `snapshot_contracts.md` — the Snapshot contract variants (50 vs 150, extension policy)
5. `scoring_dimensions.md` — what each score dimension means
6. `validity_criteria.md` — a binary structural screen (pass/fail)
7. `failure_taxonomy.md` — why an evaluation record is treated as invalid

---

## what each file is for

- `eval_protocol.md`
  - evaluation flow and validity screening
  - references `snapshot_contracts.md` for Snapshot rules

- `judge_prompt.md`
  - judge instructions and strict JSON-only output requirement
  - defers field definitions to the schema

- `schema/`
  - machine-enforced structure for judge outputs

- `snapshot_contracts.md`
  - Snapshot contract matrix used in this repo
  - binds prompt variants and judge runs to a contract id

- `scoring_dimensions.md`
  - definitions for A–E (what each dimension measures)

- `validity_criteria.md`
  - a fast pass/fail screen for structural validity
  - Snapshot is checked against the contract declared for the run

- `failure_taxonomy.md`
  - failure labels used to make invalid cases countable and auditable

---

## about score aggregation

- `compute_scores.py` and `compute_scores.md` are kept for inspection only.
- the processed tables used by the paper are already stored as fixed files under:

```
supplement/04_results/03_processed_evaluations/
```

If you want to trace how valid records are collected and aggregated, follow the reproduction entry point:

```
supplement/tools/reproduce_valid_evaluations.py
```

---

## note on conflicts

- JSON structure questions: follow `schema/`.
- Snapshot wording differences: follow `snapshot_contracts.md`.
- validity vs scoring: `validity_criteria.md` is pass/fail, `scoring_dimensions.md` explains A–E.