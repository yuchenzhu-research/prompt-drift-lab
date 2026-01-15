# Failure Taxonomy — Evaluation Failure Categories

> Scope
> - This taxonomy concerns **evaluation execution** and **judge behavior**, not model “quality”.
> - **Invalid is not the same as a low score**. Low scores can still be valid evaluations.
> - Scoring dimensions (`A_structure` … `E_drift_failure`) remain **unchanged** and are orthogonal to this taxonomy.

---

## 0) Why a separate taxonomy exists

The project uses two complementary layers:

1. **Scores (A–E)**: what the judge *scored* under the rubric.
2. **Failure labels (flags)**: why the evaluation is **not reliable / not auditable / not aligned to the protocol**.

Failure labels are used to prevent silent exclusions and to make invalid cases **countable**.

---

## 1) Canonical failure labels

The following labels appear in the current invalid-evaluation bundles and are treated as **canonical**.

### UNPARSABLE_OUTPUT
**Meaning**: The output cannot be reliably parsed or aligned to the expected structure.

**Typical signals**
- Missing required sections / headers
- Sections merged, reordered, or wrapped in extra dialogue that breaks alignment

**Common co-occurrence**
- `A_structure = 0`

---

### PROTOCOL_VIOLATION
**Meaning**: The judge does not execute the evaluation contract as specified.

**Typical signals**
- Role drift (judge turns into advisor / prompt critic / meta-analyst)
- Outputs content that is “helpful” but outside the required schema
- Ignores required constraints defined by the Snapshot contract (e.g., word limit or extension policy) while still producing an answer

**Common co-occurrence**
- High `E_drift_failure`

---

### CONTEXT_MISALIGNMENT
**Meaning**: The evaluation response is not aligned with the target file/task context (wrong target, wrong prompt variant, or mismatched interpretation).

**Typical signals**
- Evaluates a different task than the one defined in the file
- Responds to the prompt itself rather than evaluating the model output

---

### INTERNAL_INCONSISTENCY
**Meaning**: The record is internally contradictory and cannot be audited as a coherent evaluation.

**Typical signals**
- Notes/evidence contradict the assigned scores
- Claims compliance while evidence shows violation

---

### INCOMPLETE_COVERAGE
**Meaning**: The output is truncated or only partially addresses the required evaluation sections.

**Typical signals**
- Stops mid-output
- Only one section produced

---

### SELF_JUDGING_BIAS
**Meaning**: The judge evaluates its *own* model outputs (or is otherwise conflicted), making the result unsuitable for cross-model comparison.

**Notes**
- This is not a “format” failure; it is a **validity** failure.
- Keep the record for transparency, but exclude it from cross-model aggregate claims.

---

## 2) Relation to the “Invalid Case Taxonomy” in `invalid_report.md`

The illustrative report groups invalid cases into A–E categories. These categories are **narrative groupings**, while the labels above are **machine-countable flags**.

A practical mapping:

- Report **A. Schema / Format Violation** → `UNPARSABLE_OUTPUT`
- Report **B. Instruction Deviation** → `PROTOCOL_VIOLATION`
- Report **C. Semantic / Inconsistency** → `INTERNAL_INCONSISTENCY` or `CONTEXT_MISALIGNMENT`
- Report **D. Partial / Truncation** → `INCOMPLETE_COVERAGE`
- Report **E. File-Level Corruption** → *(reserved; only use if a file is corrupted on disk)*

---

## 3) How to record failures

### Where to store
- **Bundle-level**: `flags` (already used in the existing JSON bundles)
- **File-level**: include a short, standardized prefix in `notes`

Example (file-level `notes`):

- `Flags: [PROTOCOL_VIOLATION] — role drift into prompt critique; missing three-section structure.`

### Evidence expectation
If a failure label is assigned, include at least one short supporting excerpt in `evidence` (or reference the exact section) so the exclusion is auditable.

---

## 4) Reporting template

When summarizing a run (or a bundle), report failures separately from scores:

- Total evaluated: N
- Valid: N_valid
- Invalid: N_invalid
- Failure breakdown: {UNPARSABLE_OUTPUT: x, PROTOCOL_VIOLATION: y, …}

This is sufficient for reviewers to audit exclusion rules and understand brittleness patterns.