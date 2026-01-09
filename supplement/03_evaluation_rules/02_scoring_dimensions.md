# 02_Scoring Dimensions (Explanation of A–E)

## Purpose

This document explains the five scoring dimensions (A–E) defined in `EVAL_PROTOCOL.md`, helping readers understand **what each dimension is intended to measure**.

**Important Notes**
- Official scoring rules are defined exclusively in `03_evaluation_rules/EVAL_PROTOCOL.md`;
- This document introduces **no new metrics** and **does not modify thresholds**;
- In case of any inconsistency, `EVAL_PROTOCOL.md` takes precedence.

---

## Overview: What the Five Dimensions Represent

- **A_structure (Structural Compliance)**: Whether the three-section structure is actually produced and correctly ordered (i.e., whether the structure is established).
- **B_snapshot_constraint (Snapshot Constraint)**: Whether the first section is short and purely descriptive, without analysis.
- **C_actionability (Actionability of the ChatGPT Instruction)**: Whether the second section functions as an executable retrieval/production task rather than a vague suggestion.
- **D_completeness (Completeness of the Gemini Deep-Dive Instruction)**: Whether the third section simultaneously specifies source-related requirements and structured-output requirements.
- **E_drift_failure (Drift Control)**: Whether out-of-protocol content appears, such as extra body text, task rewrites, or meta-discussion.

> **Structure-First Principle**: If `A_structure == 0`, then `B/C/D/E` MUST all be 0, because when the structure fails, the remaining dimensions are not meaningfully comparable.

---

## A_structure: Structural Compliance

### What is evaluated

Whether the model **actually outputs**, in the correct order, the following three sections (as real output sections, not descriptions or teaching templates):

1. `[Fact Snapshot]`
2. `[ChatGPT Web Search Instruction]`
3. `[Gemini Deep Research Instruction]`

### How to interpret 0 / 1 / 2

- **2**: All three sections are present, correctly ordered, and contain substantive content.
- **1**: The structure is partially present or misordered, but still recognizable as a three-section attempt.
- **0**: The three-section structure is missing, or section headers appear only in explanations/templates without actual execution.

### Common failure patterns

- Treating the three-section structure as a suggested template without producing the actual sections
- Producing only one or two sections
- Heavily rewriting section headers such that the structure becomes unrecognizable

---

## B_snapshot_constraint: Fact Snapshot Constraint

### What is evaluated

Whether the first section (`[Fact Snapshot]`) satisfies the following constraints:

- Approximately **≤ 50 characters** (whitespace-stripped character count may be used as an approximation)
- **Purely descriptive**: states phenomena or conclusions without causes, mechanisms, or recommendations

### How to interpret 0 / 1 / 2

- **2**: Length is within range and the tone is purely descriptive, with no analytical expansion.
- **1**: Slightly exceeds the length limit or includes minor analytical/explanatory elements.
- **0**: The section is missing, or is clearly written as an analysis or long-form summary.

### Boundary reminder

- A “snapshot” is not an abstract or review section; it should not include multiple sources, citations, or reasoning chains.

---

## C_actionability: Actionability of the ChatGPT Web Search Instruction

### What is evaluated

Whether the second section functions as an **executable task**:

- Clearly specifies *what to search*, *how to search*, and *what to produce*
- Includes at least one **verifiable constraint** (e.g., time range, source type, quantity, or output format)

### How to interpret 0 / 1 / 2

- **2**: Clear steps with at least one hard constraint; the instruction can be copied and executed directly.
- **1**: Retrieval intent is present, but steps are vague or constraints are weak.
- **0**: The section is missing or is largely non-executable (e.g., generic advice).

### Common failure patterns

- Stating “please search for relevant information” without specifying queries, scope, or output structure
- Writing the second section as an answer or explanation rather than an instruction

---

## D_completeness: Completeness of the Gemini Deep Research Instruction

### What is evaluated

Whether the third section specifies **both** of the following requirement types:

- **Source-related requirements**: sources, links, timestamps, or source types (at least one)
- **Structured-output requirements**: tables, comparisons, taxonomies, lists, decision trees, diagrams, etc. (at least one)

### How to interpret 0 / 1 / 2

- **2**: Both source-related and structured-output requirements are present.
- **1**: Only one of the two requirement types is present.
- **0**: The section is missing, or neither requirement type is specified.

### Common failure patterns

- Requesting a “deep dive” without requiring evidence or sources
- Asking for conclusions only, without structured outputs

---

## E_drift_failure: Drift Control

### What is evaluated

Whether out-of-protocol content appears, such as:

- Appendices, large diagnostic sections, meta-discussion, or rewritten prompt templates outside the three sections
- Greetings, stances, or conclusion-style responses appearing before the first section

### How to interpret 0 / 1 / 2

- **2**: The output consists almost exclusively of the three sections, with no obvious boundary violations.
- **1**: Minor boundary violations (e.g., small amounts of extra text or brief preambles).
- **0**: Severe boundary violations where out-of-protocol content dominates and the three-section output is no longer primary (often co-occurring with `A_structure = 0`).

### Boundary reminder

- Dimension E evaluates *whether drift occurs*, not *whether the drifted content is useful*. Even helpful extra content reduces E.

---

## Relationship to Validity Criteria

- `01_validity_criteria_EN.md` provides **binary boundaries** (Strict Pass / Hard Fail) for rapid screening.
- This document provides **dimension-level explanations** to clarify the intent behind A–E.
- Neither document modifies the scoring rules defined in `EVAL_PROTOCOL.md`.

