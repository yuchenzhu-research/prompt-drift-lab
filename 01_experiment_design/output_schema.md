# Standard Output Schema v2.0

This document defines the **standard output schema** for structured-output tasks
in Prompt Drift Lab.

The evaluation focuses on whether the model **follows the required structure**,
rather than the correctness of the content itself.

This schema serves as the upstream source of truth for the evaluation rubric:
- A_structure: compliance with the required structure
- B_snapshot_constraint: whether the fact snapshot is descriptive rather than analytic
- C_actionability: whether the search instructions are executable
- D_completeness: whether all required sections are present
- E_drift_failure: whether explicit drift occurs (task rewrite, boundary violation,
  topic deviation, or role confusion)

---

## 1. Global Output Constraints

The final output produced by the evaluated model **MUST** satisfy all of the following constraints:

1. **Exactly three top-level sections**, in the fixed order below. The section headers MUST appear exactly as follows:

   **Section 1**

   ```
   [Fact Snapshot]
   ```

   **Section 2**

   ```
   [ChatGPT Web Search Instruction]
   ```

   **Section 3**

   ```
   [Gemini Deep Research Prompt]
   ```

2. **No additional headings, preambles, or closing text are allowed**

   - Do not include greetings such as "Sure", "Here is", or "Hope this helps".
   - Do not add appendices, notes, remarks, summaries, or FAQs.

3. **Do not directly answer the original question Q** This task acts as a *prompt generator / research assistant*. The output must consist of:

   - one fact snapshot, and
   - two executable retrieval / research instructions

4. **Language**: Chinese by default (unless the question explicitly requires English)
---

## 2. Canonical Template

The output must strictly follow the template below:

## 1. [Fact Snapshot]
(Use ≤50 characters to calmly and objectively describe the observed phenomenon or surface-level conclusion. Do not explain causes, give advice, or define terms.)

## 2. [ChatGPT Web Search Instruction]
(Provide an instruction that can be directly copied into ChatGPT for web search and research synthesis. The instruction must be executable and specify source and deliverable requirements.)
<Insert copy-ready instruction text here>

## 3. [Gemini Deep Research Prompt]
(Provide an instruction that can be directly copied into Gemini Deep Research for broad search and literature comparison.)
<Insert copy-ready prompt text here>
