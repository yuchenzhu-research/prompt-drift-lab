## Terminology Alignment (Bilingual Reference)

**File role**
This document clarifies the correspondence between internal historical naming and the finalized field names used in reported results. All public-facing results and statistics follow the field names defined in `/supplement/04_results/02_cross_model_evaluation/valid_evaluations/summary_tables/*.csv`. This document does not define new experimental conditions or evaluation rules.

---

## Alignment Principles

- During development, multiple internal identifiers were used for prompt variants.
- At result-freeze time, all external reporting converges to a single set of field names.
- This document exists solely to disambiguate naming and prevent misinterpretation of multiple experimental definitions.

---

## Core Terminology Mapping

| Final field name | Internal identifier | Explanation (EN) | 说明（中文） |
|---|---|---|---|
| baseline | prompt_A | Original baseline prompt | 原始基线提示词 |
| conflict | prompt_A_conflict | Adversarially perturbed variant | 对抗性偏移设置 |
| long | prompt_A_long | Length-extended variant | 扩展长度实验 |
| weak | prompt_A_weak | Weakly constrained variant | 弱约束提示词 |

> Internal identifiers were used only during prompt construction and are not part of reported results.

---

## Scope

- This mapping is provided for interpretability of result table fields only.
- It does not affect task definitions in `01_experiment_design/`.
- It does not affect evaluation protocols or scoring logic.
- Unlisted terms follow their plain-language meaning and do not introduce additional experimental definitions.

---

## Reviewer Guidance

Reviewers are expected to:

- Refer exclusively to field names in `/supplement/04_results/02_cross_model_evaluation/valid_evaluations/summary_tables/*.csv` when interpreting results.
- Ignore internal identifiers such as `prompt_A` or `prompt_B`.
- Use this document only to verify that no alternative experimental conditions or post-hoc renaming were introduced.