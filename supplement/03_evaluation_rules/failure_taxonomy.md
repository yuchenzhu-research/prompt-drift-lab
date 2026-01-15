# failure taxonomy — contract-violation types (labels only)

This file defines **failure labels** as a **classification table of contract violations**.

- Each label answers only: **which contract clause was violated**.
- Labels MUST be assigned based on observable violations.
- Labels MUST NOT describe causes, consequences, mitigation, stability, drift, or any trend.
- Labels MUST NOT reference score values.
- Multiple labels MAY be assigned to the same record. Label definitions MUST NOT overlap.

---

## 1) label set (exhaustive, non-overlapping)

All labels in this file map to INVALID conditions in `validity_criteria.md`.

### table

| Label | Definition (contract violation) | Contract source |
|---|---|---|
| `NOT_STRICT_JSON` | Violates **strict JSON** requirement (output is not a single JSON object). | `validity_criteria.md` §2.1; `eval_protocol.md` §4.1, §5 |
| `SCHEMA_VALIDATION_FAILURE` | Violates JSON schema validation against `schema/eval_record.schema.json` (missing required fields and/or type mismatch). | `validity_criteria.md` §2.2; `eval_protocol.md` §4.1, §5 |
| `PER_FILE_MAPPING_VIOLATION` | Violates the **one evaluated file → one `per_file_scores` entry** mapping requirement. | `validity_criteria.md` §2.3; `eval_protocol.md` §4.2 |
| `FILE_NAME_NOT_VERBATIM` | Violates **file name preservation** requirement (not preserved character-for-character). | `validity_criteria.md` §2.4; `eval_protocol.md` §4.3 |
| `SNAPSHOT_BLOCK_MALFORMED` | Violates Snapshot block **required order/count** (must start with exactly one Snapshot block; must contain exactly one header line and one body paragraph). | `validity_criteria.md` §2.5; `snapshot_contracts.md` §1 |
| `SNAPSHOT_HEADER_MISMATCH` | Violates Snapshot header token requirement (header is not exactly one of the permitted strings). | `validity_criteria.md` §2.6; `snapshot_contracts.md` §1.2 |
| `SNAPSHOT_BODY_SHAPE_VIOLATION` | Violates Snapshot body **shape** requirement (not one paragraph and/or contains list markers/headings and/or starts a new top-level section). | `validity_criteria.md` §2.7; `snapshot_contracts.md` §1.3, §3.2 |
| `SNAPSHOT_WORD_LIMIT_VIOLATION` | Violates Snapshot **word limit** requirement of the active `snapshot_contract_id`. | `validity_criteria.md` §2.8; `snapshot_contracts.md` §3.1 |
| `SNAPSHOT_PROHIBITED_CONTENT_TYPE` | Violates Snapshot **content-type** requirement of the active `snapshot_contract_id` (contains a forbidden content type). | `validity_criteria.md` §2.9; `snapshot_contracts.md` §2 |
| `EXTRA_TOP_LEVEL_CONTENT` | Violates **no extra top-level content** requirement (preamble, appendix, trailing paragraphs, or extra top-level section outside the required three sections). | `validity_criteria.md` §2.10; `eval_protocol.md` §3.2, §4.1 |

---

## 2) assignment rules (deterministic)

- A label MUST be assigned if and only if its definition in Section 1 is satisfied.
- If multiple definitions are satisfied, multiple labels MUST be assigned.
- No label in this file SHALL be used as a catch-all.

---

## 3) recording format (recommended)

When storing failure labels in a judge record:
- store labels as an array of strings (e.g., `flags: ["SNAPSHOT_WORD_LIMIT_VIOLATION", "EXTRA_TOP_LEVEL_CONTENT"]`)
- if evidence is stored, it SHALL include a short excerpt that directly shows the violating text span or missing structure