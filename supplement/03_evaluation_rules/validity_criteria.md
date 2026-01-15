# validity criteria — valid / invalid adjudication (contract-only)

This file defines a **binary** adjudication: **VALID** or **INVALID**.

- INVALID conditions in this file are limited to **format violations** or **contract violations**.
- Each INVALID condition SHALL be traceable to either:
  - `eval_protocol.md`, or
  - `snapshot_contracts.md`.

This file MUST NOT classify outputs as invalid based on score values, perceived reasonableness, or any result anomaly.

---

## 1. decision rule

An output is **VALID** if it triggers **none** of the INVALID conditions listed in Section 2.

An output is **INVALID** if it triggers **any** INVALID condition listed in Section 2.

---

## 2. INVALID conditions (exhaustive)

### 2.1 invalid — not strict JSON (eval_protocol.md §4.1, §5)
The output is INVALID if it is not a single strict JSON object.

### 2.2 invalid — JSON schema validation failure (eval_protocol.md §4.1, §5)
The output is INVALID if it fails validation against `schema/eval_record.schema.json`, including any of the following:
- required field missing
- field type mismatch
- `per_file_scores` missing or not an array
- any `per_file_scores` entry missing required fields

### 2.3 invalid — `per_file_scores` mapping violation (eval_protocol.md §4.2)
The output is INVALID if any of the following holds:
- an evaluated file maps to more than one `per_file_scores` entry
- a `per_file_scores` entry does not specify exactly one `file`

### 2.4 invalid — file name not preserved verbatim (eval_protocol.md §4.3)
The output is INVALID if any `per_file_scores[i].file` is not preserved character-for-character.

### 2.5 invalid — missing or malformed Snapshot block (snapshot_contracts.md §1)
The output is INVALID if the Snapshot block violates any hard Snapshot format requirement, including any of the following:
- the output does not start with exactly one Snapshot block
- the Snapshot block does not contain exactly one header line and exactly one body paragraph

### 2.6 invalid — Snapshot header mismatch (snapshot_contracts.md §1.2)
The output is INVALID if the Snapshot header line is not exactly one of:
- `1. [事实快照]`
- `1. [Snapshot]`

### 2.7 invalid — Snapshot body shape violation (snapshot_contracts.md §1.3)
The output is INVALID if the Snapshot body violates any of the following:
- body is not exactly one paragraph
- body contains any list markers or headings
- body contains any section marker that starts a new top-level section

### 2.8 invalid — Snapshot word limit violation (snapshot_contracts.md §3.1)
The output is INVALID if the Snapshot body exceeds the active contract `word_limit`.

Word counting SHALL split on whitespace.

### 2.9 invalid — Snapshot prohibited content type present (snapshot_contracts.md §2)
The output is INVALID if the Snapshot body contains any content type that the active `snapshot_contract_id` forbids.

### 2.10 invalid — out-of-protocol extra content present (eval_protocol.md §3.2, §4.1)
The output is INVALID if it contains any top-level material outside the required three-section output, including any of the following:
- any preamble before the Snapshot header
- any appendix, postscript, or trailing paragraphs after the final required section
- any additional top-level section beyond the required three

---

## 3. traceability table

| INVALID condition | Contract source |
|---|---|
| 2.1 not strict JSON | `eval_protocol.md` §4.1, §5 |
| 2.2 schema validation failure | `eval_protocol.md` §4.1, §5 |
| 2.3 per-file mapping violation | `eval_protocol.md` §4.2 |
| 2.4 file name not verbatim | `eval_protocol.md` §4.3 |
| 2.5 Snapshot block malformed | `snapshot_contracts.md` §1 |
| 2.6 Snapshot header mismatch | `snapshot_contracts.md` §1.2 |
| 2.7 Snapshot body shape violation | `snapshot_contracts.md` §1.3, §3.2 |
| 2.8 Snapshot word limit violation | `snapshot_contracts.md` §3.1 |
| 2.9 Snapshot prohibited content type | `snapshot_contracts.md` §2 |
| 2.10 extra top-level content | `eval_protocol.md` §3.2, §4.1 |