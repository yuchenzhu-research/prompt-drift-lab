# eval protocol

## 0. authority and precedence

This file (**`eval_protocol.md`**) is the **only normative authority** for evaluation rules in `supplement/03_evaluation_rules/`.

- If any other document (including `snapshot_contracts.md`, `scoring_dimensions.md`, `failure_taxonomy.md`, `judge_prompt.md`, `readme.md`) conflicts with this file, **this file MUST be followed**.
- `schema/eval_record.schema.json` defines the **mechanical JSON shape** only. It MUST be used for validation, but it MUST NOT be treated as an alternative source of evaluation rules.
- Other documents are **subordinate references**. They may describe or list items, but they MUST NOT introduce parallel definitions.

---

## 1. scope

This protocol defines:
- what the judge receives as input
- what the judge MUST produce as output
- what counts as a valid/invalid judge record
- the atomic unit for aggregation (`per_file_scores`)
- phase rules (Phase 0 / 1 / 2)

This protocol does **not** define research claims, effect sizes, or performance conclusions.

---

## 2. terms

### 2.1 evaluated file
An **evaluated file** is one artifact produced by a model run.

- In this repo, an evaluated file is stored as a **PDF** that contains a model output.
- The PDF is treated as an **opaque container** whose visible content is the only material the judge may use.

### 2.2 bundle
A **bundle** is a fixed set of evaluated files grouped for convenience (e.g., a directory listing).

- Bundle membership MAY be logged for traceability.
- Bundle membership MUST NOT be used as a scoring prior.

### 2.3 judge record
A **judge record** is a single JSON object produced by the judge.

- It MUST conform to `schema/eval_record.schema.json`.
- It MUST contain `per_file_scores` entries as specified in Section 4.

---

## 3. judge input and prohibited behaviors

### 3.1 judge input (what the judge receives)
For each evaluated file, the judge input MUST be:
1) the evaluated file content (PDF)
2) the active evaluation rules (this protocol + any referenced subordinate lists)
3) the active scoring scale definitions (as referenced, without redefining precedence)

No other inputs are permitted.

### 3.2 prohibited behaviors (semantic constraints)
The judge MUST NOT:
- **re-parse** or reconstruct the PDF into a new representation (e.g., OCR, reflowing, converting to markdown, extracting metadata) beyond reading the visible content as provided
- **manually reinterpret** the task by injecting unstated assumptions
- **infer semantics** from file paths, file names, directory names, model names, or bundle composition
- use any external knowledge of this repo structure as a scoring shortcut

The evaluated file name MAY be included in the record for alignment and traceability (Section 4.2), but it MUST NOT affect scoring.

---

## 4. evaluation output and atomic unit

### 4.1 output (what the judge produces)
Each evaluation run MUST produce **one** judge record (one JSON object).

- The record MUST be strict JSON.
- The record MUST validate against `schema/eval_record.schema.json`.

### 4.2 `per_file_scores` is the core atomic unit
`per_file_scores` is the **only atomic unit** used for aggregation.

Rules:
- **One evaluated file MUST map to exactly one `per_file_scores` entry.**
- **All aggregation and summary statistics MUST be computed only from `per_file_scores` entries** that pass validity screening (Section 5).
- Any additional fields (bundle metadata, run metadata, notes) MUST NOT be used as an alternative scoring base.

### 4.3 file name preservation without semantic use
For each `per_file_scores` entry:
- the `file` field MUST preserve the file name **character-for-character** (no normalization, no path rewriting)
- the `file` field MUST be used for **alignment only** (mapping outputs back to artifacts)
- the judge MUST NOT use the `file` field to infer intent, difficulty, or expected content

---

## 5. validity screening (what counts as valid)

A judge record MUST be marked invalid if any of the following holds:
- the output is not strict JSON
- JSON schema validation fails (missing fields, wrong types, extra structure violations)
- any required evidence field is missing, empty, or not verbatim when verbatim is required by the referenced rule text
- any structural constraint required by the active phase (Section 6) is violated

Invalid records:
- MUST be kept for protocol compliance analysis
- MUST NOT be included in primary aggregation

---

## 6. phases (Phase 0 / 1 / 2)

This repo defines three phases. Phases differ only by **judge mode** and **structural constraints**.

### 6.1 Phase 0 (v0): diagnostic
Phase 0 is **diagnostic only**.

- Phase 0 records MUST be labeled as Phase 0 in run metadata.
- Phase 0 outputs MUST NOT be used for final claims.
- Phase 0 MAY relax constraints compared to Phase 1/2, but any relaxations MUST be explicitly stated in the Phase 0 judge prompt.

### 6.2 Phase 1 (v1): primary judging
Phase 1 is the primary mode used for aggregation.

- Phase 1 MUST enforce the active structural constraints stated in the judge prompt and referenced rule lists.
- Phase 1 validity MUST follow Section 5.

### 6.3 Phase 2 (v2): strict structure enforcement
Phase 2 is a stricter structure mode.

- Phase 2 MUST enforce all Phase 1 requirements.
- Phase 2 MUST additionally enforce any extra structural constraints stated for Phase 2 in the judge prompt.

Notes:
- Phase identifiers MUST be recorded in run metadata.
- A run MUST NOT mix multiple phases within a single judge record.

---

## 7. cross-model judging and self-judging

### 7.1 cross-model judging
Cross-model judging is when the judge model evaluates artifacts produced by a different model.

- Each evaluated file MUST be scored independently.
- Cross-model records that pass validity screening (Section 5) MAY be aggregated.

### 7.2 self-judging
Self-judging is when the generator model judges its own outputs.

- Self-judging records MAY be generated.
- Self-judging records MUST be labeled as self-judging in metadata.
- Self-judging records MUST NOT be the sole basis of aggregated results.

---

## 8. references (subordinate, non-parallel)

The following documents are subordinate references. They MUST NOT override this protocol.

- `snapshot_contracts.md`: lists snapshot constraints used by judge prompts
- `scoring_dimensions.md`: lists scoring dimensions and rubric text
- `failure_taxonomy.md`: defines failure labels (labels only)
- `judge_prompt.md`: the active judge instruction text used to elicit records
- `schema/eval_record.schema.json`: mechanical JSON validation schema

---

## 9. change control

- Any change to this protocol MUST be versioned by commit.
- Runs MUST record the protocol version identifier used (e.g., commit hash or protocol tag) in run metadata.