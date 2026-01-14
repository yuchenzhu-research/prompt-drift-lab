## Output Schema

This document defines the required output structure for all evaluated model responses. The schema specifies structural constraints only and does not define task semantics or evaluation criteria.

---

### Global Constraints

An evaluated output MUST satisfy all of the following:

1. Exactly three top-level sections, in the order listed below.
2. No additional headings, preambles, or trailing text.
3. The output must not directly answer the original question.

---

### Section Structure

1. **fact snapshot**  
   A concise factual statement (≤ 50 characters). No explanation or interpretation.

2. **chatgpt search instructions**  
   Executable instructions for online search and synthesis.

3. **gemini deep research instructions**  
   Executable instructions for broad literature and mechanism exploration.

---

### Notes

- The schema enforces structure only; content correctness is evaluated separately.
- Field names and section labels follow the conventions used in result tables and evaluation protocol.
- Minor preambles or extraneous text may be recorded as drift if the required section structure remains identifiable.