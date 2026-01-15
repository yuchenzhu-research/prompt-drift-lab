# validity criteria — binary structural screening

## purpose

This file provides a simple pass/fail screen for structural validity.

- It helps filter obviously broken outputs for spot-checking.
- It is a reading aid aligned with `eval_protocol.md`.

It defines hard structural boundaries only.
It does not produce scores and it does not support statistical claims.

---

## A. strict pass

If SP1–SP5 are all satisfied, the output is treated as structurally valid.

### SP1. three-section structure is present and ordered

All three sections appear as actual output sections, in this order:

1. `[Fact Snapshot]`
2. `[ChatGPT Web Search Instruction]`
3. `[Gemini Deep Research Instruction]`

### SP2. fact snapshot follows the snapshot contract

The first section (`[Fact Snapshot]`) follows the Snapshot contract declared for the run.

The contract is identified by `snapshot_contract_id` and defined in `snapshot_contracts.md`.
At minimum, this check includes:

- staying within the contract word limit
- respecting the contract’s extension / analysis policy
- containing no sources, links, or citations

### SP3. the second section is an executable retrieval instruction

- Specifies what to search, how to search, and what to produce
- Includes at least one verifiable constraint
  (e.g., time range, source type, quantity, or output format)

### SP4. the third section includes deep-research completeness

It includes both of the following:

- at least one source-related requirement
  (e.g., sources, links, timestamps)
- at least one structured-output requirement
  (e.g., tables, comparisons, taxonomies, lists, decision trees, diagrams)

### SP5. no out-of-protocol content

- no greetings, closings, appendices, diagnoses, or prompt rewrites
  outside the three sections
- no preamble text before Section 1

---

## B. structural failure

If any of HF1–HF3 occurs, the output is classified as a structural failure.

In practice, this usually corresponds to `A_structure = 0`
or a very low `E_drift_failure`,
and other dimensions are not meaningfully comparable.

### HF1. three-section structure not executed

- The output discusses or teaches the format without producing it
- Section headers appear only as suggestions, templates, or repair text

### HF2. task reinterpretation

- The three-section task is rewritten as answering the question directly,
  writing an essay, or diagnosing prompts
- Long opinions or summaries override the required structure

### HF3. severe out-of-scope content

- Extra paragraphs, appendices, meta-discussion, or rewritten prompt templates
  dominate the output
- Content outside the three sections becomes the primary body

---

## C. cross-question consistency

This section is not used for pass/fail decisions on individual files.
It is for analysis and trigger localization, for example:

- whether a prompt variant collapses across Q3/Q4
- whether implicit triggers are more likely to cause structural failure

For retrospective analysis, combine with grouped statistics in `supplement/04_results/`.