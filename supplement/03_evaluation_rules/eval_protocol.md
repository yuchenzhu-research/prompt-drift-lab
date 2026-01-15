# eval protocol

This document describes how we generate, screen, and interpret judge records in this repo.

It is intentionally narrow:
- it explains the evaluation flow and what counts as a valid record
- it does not redefine the JSON format

The JSON structure is defined by:
- `/supplement/03_evaluation_rules/schema/eval_record.schema.json`

---

## snapshot rules: what we follow when wording conflicts

Snapshot constraints are taken from `snapshot_contracts.md`.

If the judge prompt or other docs phrase Snapshot differently, we follow:
1) `snapshot_contracts.md`
2) the active judge prompt text
3) other notes and readmes

Each run records which Snapshot contract was used (see Section 5.1).

---

## 1. what gets evaluated

### 1.1 evaluated artifacts
- model outputs produced under controlled prompt conditions
- artifacts are be stored as pdf

### 1.2 input bundle
- a bundle is a fixed set of artifacts from a run
- bundle composition is logged for traceability
- composition is not used as a scoring prior

---

## 2. evaluation output

Each evaluation produces one JSON record.
That record must conform to:
- `schema/eval_record.schema.json`

Aggregation and verification operate only on schema-valid records.

---

## 3. judging setup

### 3.1 cross-model judging (primary)
- a judge model evaluates artifacts produced by another model
- artifacts are evaluated independently
- primary statistics are computed from schema-valid cross-model records

Records that break the schema or required evidence constraints are treated as invalid and excluded from primary statistics.

### 3.2 self-judging (secondary)
- a generator model may judge its own outputs under the same protocol
- self-judging is used for consistency checks only
- it is not the sole basis for conclusions

---

## 4. validity screening

A judge record is invalid if:
- it is not strict JSON
- it fails the JSON schema (missing fields, wrong types, etc.)
- required evidence fields are missing or not verbatim
- it violates structural constraints defined by the evaluation rules (including Snapshot constraints)

Invalid records are excluded from primary aggregation and kept for protocol compliance analysis.

---

## 5. recording and consistency

- judges are asked to score based on the artifact content and the stated contract
- metadata labels are used for grouping and logging, not as a scoring shortcut
- a run is defined by: the prompt variant, the judge prompt, the schema, and recorded metadata

### 5.1 required run metadata (snapshot)

Each run records:
- `snapshot_contract_id`
- `snapshot_word_limit`
- `snapshot_allow_extension`

Values are expected to match the chosen contract in `snapshot_contracts.md`.