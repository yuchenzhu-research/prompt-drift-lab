# 04 Results — Invalid Evaluation Report

## Scope

This report documents **invalid evaluation records** identified during the evaluation phase. All referenced paths are **relative to the repository root**. The report is intended for **audit and inspection only**.

Invalid evaluations are **excluded from all quantitative aggregation and summary tables**. This document does **not** redefine evaluation rules, scoring rubrics, or inclusion criteria.

---

## Overview

- **Location**: `supplement/04_results/02_cross_model_evaluation/invalid_evaluations/`
- **Purpose**: to summarize evaluation records that fail **protocol-level validity checks** and therefore cannot be reliably aggregated
- **Role**: descriptive and diagnostic; not normative

---

## What Counts as “Invalid”

An evaluation record is classified as **invalid** when the judge fails to execute the evaluation contract in a way that is **structurally auditable**.

Invalid evaluations are **not low-scoring results**. Low scores (including `0`) correspond to valid evaluations under the protocol. An invalid evaluation is one that cannot be parsed, aligned, or verified under the evaluation contract, regardless of apparent answer quality.

---

## Relation to Failure Flags

Each invalid record in this directory is marked using one or more **failure flags** recorded in the evaluation bundle (e.g., `PROTOCOL_VIOLATION`, `UNPARSABLE_OUTPUT`).

These flags are defined in:

- `supplement/03_evaluation_rules/failure_taxonomy.md`

Failure flags **do not replace scoring dimensions**. They explain *why* an evaluation record is excluded from aggregation.

---

## Invalid Case Taxonomy

For reporting and inspection, invalid records are grouped into the following **narrative categories**. These categories are *descriptive* and may map to multiple failure flags.

### A. Schema / Format Violation

- Missing required JSON fields
- Incorrect data types (e.g., string instead of number)
- Extra free-form text outside the JSON object
- Broken or non-parseable JSON

**Common flags**: `UNPARSABLE_OUTPUT`

---

### B. Instruction Deviation

- Output does not follow the specified evaluation contract
- Required dimensions are skipped, merged, or replaced
- The judge reframes the task into advice, critique, or meta-level discussion

**Common flags**: `PROTOCOL_VIOLATION`

---

### C. Semantic or Internal Inconsistency

- Assigned scores contradict the accompanying rationale
- Rationale does not correspond to the evaluated content
- Internally inconsistent or self-contradictory judgments

**Common flags**: `INTERNAL_INCONSISTENCY`, `CONTEXT_MISALIGNMENT`

---

### D. Partial Output or Truncation

- Output terminates before completion
- Only a subset of required dimensions is returned

**Common flags**: `INCOMPLETE_COVERAGE`

---

### E. File-Level Corruption

- Empty files
- Encoding errors (e.g., not decodable as UTF-8)
- Files that are not valid JSON

**Common flags**: *(reserved; rarely observed)*

---

## Documented Invalid Cases

The cases below are **illustrative summaries** rather than an exhaustive listing of individual files.

### Case 01 — Protocol Violation via Role Drift

- Narrative category: B
- Failure flag(s): `PROTOCOL_VIOLATION`
- Location: `supplementent/04_results/02_cross_model_evalutaion/invalid_evaluations/main_method_cross_model/`
- Description: the judge response reframes the evaluation task into advisory or diagnostic commentary, replacing the required evaluation structure.

### Case 02 — Partial Output / Truncation

- Narrative category: D
- Failure flag(s): `INCOMPLETE_COVERAGE`
- Location: `supplementent/04_results/02_cross_model_evalutaion/invalid_evaluations/supporting_method_self_eval/`
- Description: the output terminates before all required dimensions are evaluated, resulting in incomplete records.

### Case 03 — Instruction Deviation with Inconsistency

- Narrative category: B, C
- Failure flag(s): `PROTOCOL_VIOLATION`, `INTERNAL_INCONSISTENCY`
- Location: `supplementent/04_results/02_cross_model_evalutaion/invalid_evaluations/main_method_cross_model/`
- Description: scores are present, but rationales do not align with the evaluated content or violate the evaluation contract.

---

## Handling Policy

- Invalid evaluations are **excluded from aggregate scoring** and summary tables.
- Counts of invalid records are reported separately for transparency.
- No manual correction, reinterpretation, or reclassification is applied.

---

## Reproducibility Notes

- This report references **directories and categories**, not individual filenames.
- No absolute paths or environment-specific assumptions are used.
- The document supports auditability of exclusion decisions rather than completeness.

---

## Limitations

- This report does not attempt to attribute root causes beyond protocol-level classification.
- Narrative categories may overlap across cases.
- The set of invalid records may grow as additional evaluations are run.