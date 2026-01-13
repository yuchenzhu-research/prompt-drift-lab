# Standard Output Schema

> **Status Note**  
> This English file is provided **for structural reference only**.  
> The **authoritative output schema** is defined in:
>
> - `output_schema_ZH.md`
>
> In case of any inconsistency, the Chinese version prevails.

---

This document defines the **standard output schema** for structured-output tasks
in Prompt Drift Lab.

The evaluation focuses on whether the model **follows the required structure**,
rather than the correctness of the content itself.

This schema serves as a **non-authoritative reference** aligned with the Chinese
schema and is intended to help non-Chinese reviewers understand the output layout.

---

## 1. Global Output Constraints

The final output produced by the evaluated model **MUST** satisfy all of the following constraints:

1. **Exactly three top-level sections**, in the fixed order below.  
   The section headers are shown here **for reference** and follow the numbering
   and bracketed style used in the raw outputs.

   **Section 1**

   ```
   1. [Fact Snapshot]
   ```

   **Section 2**

   ```
   2. [ChatGPT Web Search Instruction]
   ```

   **Section 3**

   ```
   3. [Model Reasoning Instruction]
   ```

   > Example from raw output: `3. [Gemini Deep Research Prompt]`

2. **No additional headings, preambles, or closing text are allowed**

   - Do not include greetings such as "Sure", "Here is", or "Hope this helps".
   - Do not add appendices, notes, remarks, summaries, or FAQs.

3. **Do not directly answer the original question Q**.  
   This task acts as a *prompt generator / research assistant*. The output must consist of:

   - one fact snapshot, and
   - two executable retrieval / research instructions

4. **Language**: Chinese by default (unless the question explicitly requires English)

---

## 2. Canonical Template

The output should follow the template below:

## 1. [Fact Snapshot]
Use ≤50 characters to calmly and objectively describe the observed phenomenon or surface-level conclusion. Do not explain causes, give advice, or define terms.

## 2. [ChatGPT Web Search Instruction]
Provide an instruction that can be directly copied into ChatGPT for web search and research synthesis. The instruction must be executable and specify source and deliverable requirements.

## 3. [Model Reasoning Instruction]
Provide an instruction that can be directly copied into a deep research model for broad search and literature comparison.