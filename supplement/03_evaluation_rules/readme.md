# 03 evaluation rules

**Authority:** `eval_protocol.md` is the only normative protocol in this directory; all other files are subordinate references.

This directory defines evaluation **contracts** only.

- It contains **no experimental results**.
- It has **no dependency** on `tools/` or `supplement/04_results/`.

---

## start here

1) `eval_protocol.md` — protocol entry point and precedence.

---

## file index

- `eval_protocol.md` — protocol entry point and precedence.
- `judge_prompt.md` — contract-instantiating prompt for producing one eval record.
- `schema/eval_record.schema.json` — machine-checkable JSON structure and types for an eval record.
- `snapshot_contracts.md` — Snapshot block contract definitions.
- `scoring_dimensions.md` — meanings of score fields used in each per-file score entry.
- `validity_criteria.md` — binary valid/invalid adjudication conditions (contract-only).
- `failure_taxonomy.md` — labels for contract-violation types.
- `compute_scores.md` — documentation of the scoring utility mapping behavior.
- `compute_scores.py` — scoring utility script.