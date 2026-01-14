# Validity Criteria — Binary Structural Screening

## Purpose

This document serves two strictly limited purposes:

1) To provide a **binary screen** (pass / fail) for identifying structurally valid
   versus structurally failed outputs, enabling efficient filtering and spot-checking;
2) To act as a **human-review reference** aligned with `eval_protocol.md`.

It defines **hard validity boundaries and canonical forms only**.
It does **not** produce scores and does **not** generate statistical conclusions.

---

## A. Strict Pass

If conditions SP1–SP5 are all satisfied, the output is considered
**structurally valid** under the evaluation protocol.

Typical manifestations include stable structure,
consistent constraint execution, and minimal drift.

### SP1. Three-section structure is strictly present and correctly ordered

All three sections **must appear as actual output sections**
and in the following order:

1. `[Fact Snapshot]`
2. `[ChatGPT Web Search Instruction]`
3. `[Gemini Deep Research Instruction]`

### SP2. Fact Snapshot strictly satisfies constraints

- Approximately **≤ 50 characters**
  (whitespace-stripped character count may be used as an approximation)
- States only phenomena or conclusions;
  **no causes, mechanisms, or recommendations**
- Contains **no sources, links, or citations**

### SP3. The second section is an executable retrieval instruction

- Clearly specifies *what to search*, *how to search*, and *what to produce*
- Includes at least one **verifiable constraint**
  (e.g., time range, source type, quantity, or output format)

### SP4. The third section satisfies deep-investigation completeness

Must include **both** of the following:

- At least one **source-related requirement**
  (e.g., sources, links, timestamps)
- At least one **structured-output requirement**
  (e.g., tables, comparisons, taxonomies, lists, decision trees, diagrams)

### SP5. No out-of-protocol content

- No greetings, closings, appendices, diagnoses, or prompt rewrites
  outside the three sections
- No preamble text such as personal stances, conclusions, or summaries
  before Section 1

---

## B. Structural Failure

If any of HF1–HF3 occurs, the output is classified as a
**structural failure**.

In practice, this usually corresponds to `A_structure = 0`
or a very low `E_drift_failure` score,
and other dimensions are not meaningfully comparable.

### HF1. Three-section structure not executed

- The output discusses, analyzes, or teaches the format
  without actually producing it
- Section headers appear only in *suggestions, templates,
  or repair instructions*, not in the actual output

### HF2. Task reinterpretation

- The task of generating three-section instructions is rewritten
  as directly answering the question, writing an essay, or diagnosing prompts
- Extensive opinions, recommendations, or summaries override
  the structural instructions

### HF3. Severe out-of-scope content

- Additional paragraphs, appendices, meta-discussion,
  or rewritten prompt templates dominate the output
- Explanatory text outside the three sections becomes the primary content,
  displacing the protocol-defined output

---

## C. Cross-question Consistency

This section is **not used for binary validity decisions on individual files**.
It is intended for **analysis and trigger localization only**:

- Whether the same prompt variant exhibits systematic collapse
  across Q3/Q4 or implicit/explicit triggers
- Used to identify triggering conditions
  (e.g., implicit prompts being more prone to structural failure)

For retrospective analysis, combine with grouped statistics
in `supplement/04_results/`.