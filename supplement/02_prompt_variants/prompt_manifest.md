# Prompt Manifest

## Purpose

This document enumerates all executable prompt variants used in the experiments
and clarifies their experimental roles and statistical inclusion boundaries.
Prompt files are treated as fixed experimental inputs and are not modified
during evaluation.

---

## Prompt Language and Authority

All executable prompt files in this directory are written in **Chinese** and are
used verbatim during experimental execution. English descriptions provided here
serve explanatory purposes only and do not constitute executable prompt artifacts.

---

## Prompt Inventory

| File | Variant | Experimental Role |
|---|---|---|
| `00_baseline_prompt_A.txt` | baseline | Exploratory pilot (qualitative only) |
| `01_structured_prompt_B.txt` | baseline | Primary experimental anchor |
| `02_conflict_prompt.txt` | conflict | Instruction conflict perturbation |
| `03_long_prompt.txt` | long | Length and redundancy perturbation |
| `04_weak_prompt.txt` | weak | Constraint relaxation perturbation |

---

## Statistical Inclusion

- Quantitative analysis is conducted exclusively on prompt variants derived from
  the protocolized three-section format (`01_structured_prompt_B.txt` and its
  perturbations).
- `00_baseline_prompt_A.txt` is used for early pipeline validation and failure-mode
  discovery only and is excluded from aggregated quantitative results unless
  explicitly stated.

---

## Variant Descriptions (English Summary)

- **baseline**  
  Specifies a strict three-section output format and serves as the reference
  condition for evaluation.

- **conflict**  
  Introduces mutually competing instructions to stress priority resolution and
  structural robustness.

- **long**  
  Expands the baseline prompt with verbose explanations and redundant guidance to
  stress attention and constraint retention.

- **weak**  
  Softens constraint signaling to test sensitivity to under-specified
  instructions.

---

## Reproducibility Notes

Each run records the prompt file name and a cryptographic hash to ensure
traceability across raw outputs, scored records, and aggregated summaries.

---

## Alignment with Evaluation Rules

Prompt variants define the input perturbation space only. Evaluation logic,
scoring rubrics, and validity criteria are defined independently under
`03_evaluation_rules/` and do not inspect prompt content.