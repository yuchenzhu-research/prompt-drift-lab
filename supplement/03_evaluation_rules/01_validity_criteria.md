# 01_Validity Criteria (Hard Constraints)

## Purpose (Read First)

This document defines **binary validity criteria** for determining whether an output is structurally acceptable or a structural failure.
It serves two purposes:

1) To provide a fast, binary screen for identifying *structurally valid* vs. *structurally failed* outputs, enabling efficient filtering and spot-checking;
2) To act as an auxiliary explanation and human review reference for `03_evaluation_rules/EVAL_PROTOCOL_ZH.md`.

**Important Notes**
- Official scoring follows the 0/1/2 rubric defined in `EVAL_PROTOCOL_ZH.md`;
- This document defines only **hard validity boundaries and canonical forms**. It does **not** replace scoring and does **not** produce any statistical conclusions.

---

## A. Strict Pass (Sufficient Conditions)

If conditions SP1–SP5 are all satisfied, the output can be considered **very close to full-compliance behavior under the rubric**.
Typical manifestations include stable structure, consistent constraint execution, and minimal drift.

### SP1. Three-section structure is strictly present and correctly ordered

All three sections MUST appear as *actual output sections* and in the following order:

1. `[Fact Snapshot]`
2. `[ChatGPT Web Search Instruction]`
3. `[Gemini Deep Research Instruction]`

### SP2. Fact Snapshot strictly satisfies constraints

- Approximately **≤ 50 characters** (whitespace-stripped character count may be used as an approximation)
- States only phenomena or conclusions; **no causes, mechanisms, or recommendations**
- Contains **no sources, links, or citations** (to avoid turning the snapshot into a retrieval or review section)

### SP3. The second section is an executable retrieval instruction

- Clearly specifies *what to search*, *how to search*, and *what to produce*
- Includes at least one **verifiable constraint** (e.g., time range, source type, quantity, or output format)

### SP4. The third section satisfies deep-investigation completeness

Must include **both** of the following:

- At least one **source-related requirement** (e.g., sources, links, timestamps)
- At least one **structured-output requirement** (e.g., tables, comparisons, taxonomies, lists, decision trees, diagrams)

### SP5. No out-of-protocol content (≈ zero drift)

- No greetings, closings, appendices, diagnoses, or prompt rewrites outside the three sections
- No preamble text such as personal stances, conclusions, or summaries before Section 1

---

## B. Structural Failure (Hard Fail, Necessary Conditions)

If any of HF1–HF3 occurs, the output is classified as a **structural failure**.
In practice, this usually corresponds to `A_structure = 0` under the rubric or a very low `E_drift_failure` score, and other dimensions are not meaningfully comparable.

### HF1. Three-section structure not executed (or only described)

- The output discusses, analyzes, or teaches the format without actually producing it
- Section headers appear only in *suggestions, templates, or repair instructions*, not in the actual output

### HF2. Task reinterpretation (role override / goal rewrite)

- The task of generating three-section instructions is rewritten as directly answering the question, writing an essay, or diagnosing prompts
- Extensive opinions, recommendations, or summaries override the structural instructions

### HF3. Severe out-of-scope content (extra body dominates)

- Additional paragraphs, appendices, meta-discussion, or rewritten prompt templates dominate the output
- Explanatory text outside the three sections becomes the primary content, displacing the protocol-defined output

---

## C. Cross-question Consistency (Bundle-level Check, Non-binding)

This section is **not used for binary validity decisions on individual files**.
It is intended for analysis and trigger localization only:

- Whether the same prompt variant exhibits systematic collapse across Q3/Q4 or implicit/explicit triggers
- Used to identify triggering conditions (e.g., implicit prompts being more prone to structural failure)

> Recommended to combine with grouped statistics in `04_results/` (by version / by question / by trigger) for retrospective analysis.
