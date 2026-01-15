# scoring dimensions

This file defines the meanings of the **five** scoring fields in each `per_file_scores.scores` record.

- Field names in this file MUST match the JSON fields **character-for-character**.
- Each dimension MUST be judged **independently** from the others.
- This file MUST NOT define scoring aggregation, validity gates, or any run-level rules.

---

## fields (exact)

The judge record MUST use exactly the following five score fields:

- `A_structure`
- `B_snapshot_constraint`
- `C_actionability`
- `D_completeness`
- `E_drift_failure`

Each field MUST be scored on `{0,1,2}`.

---

## A_structure — three-section structure compliance

**Judged object:** the presence and order of the required three sections.

### observable requirements
The output MUST contain exactly three top-level sections, in this order:
1) the Snapshot section
2) the ChatGPT web-search instruction section
3) the Gemini deep-research instruction section

Section identity MUST be determined by the required section headers defined by the active rules.

### score mapping
- **2**: All three required section headers are present, appear in the required order, and each section has non-empty content.
- **1**: The output contains at least two required section headers, but at least one of the following holds: one required header is missing; order is not the required order; or at least one required section is empty.
- **0**: Fewer than two required section headers are present.

---

## B_snapshot_constraint — snapshot contract compliance

**Judged object:** the Snapshot section only.

### observable requirements
The Snapshot section MUST satisfy the active Snapshot contract referenced by run metadata (e.g., `snapshot_contract_id`).

Contract checks MUST include (when applicable):
- required Snapshot header token
- required body shape (single paragraph; no lists/headings)
- word limit
- allowed / forbidden content types stated by the contract

### score mapping
- **2**: All contract checks pass.
- **1**: The Snapshot violates **at most one** contract check and the violation is bounded (e.g., small word-limit overage or one minor formatting token).
- **0**: The Snapshot violates **two or more** contract checks, or violates any hard contract check that is marked as a format requirement.

---

## C_actionability — ChatGPT web-search instruction executability

**Judged object:** the ChatGPT web-search instruction section only.

### observable requirements
The section MUST be an instruction (not an answer) and MUST include all of the following components:
1) **search target**: at least one explicit query string or keyword set to search for
2) **constraints**: at least one verifiable constraint (e.g., time window, source type/domain constraint, required count, inclusion/exclusion rule)
3) **deliverable**: at least one explicit output requirement (e.g., required fields, required format, required number of items)

### score mapping
- **2**: All three components (1–3) are present.
- **1**: Exactly two of the three components (1–3) are present.
- **0**: Zero or one of the three components (1–3) is present, or the section is missing.

---

## D_completeness — Gemini deep-research instruction requirements coverage

**Judged object:** the Gemini deep-research instruction section only.

### observable requirements
The section MUST contain **both** of the following requirement types:
1) **evidence requirements**: at least one requirement about sources (e.g., links, citations, timestamps, source types)
2) **structured-output requirements**: at least one requirement that the output be structured (e.g., table, taxonomy, comparison, checklist, decision tree)

### score mapping
- **2**: Both requirement types (1 and 2) are present.
- **1**: Exactly one of the two requirement types (1 or 2) is present.
- **0**: Neither requirement type is present, or the section is missing.

---

## E_drift_failure — out-of-protocol extra content presence

**Judged object:** text that appears **outside** the three required sections.

### observable requirements
The output MUST NOT contain additional top-level material outside the three required sections.

Out-of-protocol material includes (non-exhaustive):
- any preamble before the first required section header
- any appendix, postscript, or trailing paragraphs after the third required section
- any additional top-level section beyond the required three

### score mapping
- **2**: No out-of-protocol material is present (whitespace-only outside sections is allowed).
- **1**: A single minor out-of-protocol fragment is present (e.g., one short line before the first header or one short trailing line after the third section).
- **0**: More than one out-of-protocol fragment is present, or any multi-paragraph appendix / additional section is present.