# Prompt Manifest

## Purpose

This document enumerates all executable prompt files used in the experiments and
states their experimental roles and inclusion rules for summary tables.
Prompt files are treated as fixed experimental inputs and are not modified
during evaluation.

---

## Prompt Language and Authority

All executable prompt files in this directory are written in **Chinese** and are
used verbatim during experimental execution. English descriptions provided here
are explanatory only and are not executable artifacts.

---

## Prompt Inventory

| File | Variant | Experimental Role |
|---|---|---|
| `00_baseline_prompt_A.txt` | baseline | Pilot / smoke test (qualitative only) |
| `01_structured_prompt_B.txt` | baseline | Primary experimental anchor |
| `02_conflict_prompt.txt` | conflict | Competing-requirements perturbation |
| `03_long_prompt.txt` | long | Redundancy / length perturbation |
| `04_weak_prompt.txt` | weak | Softer-constraint wording perturbation |

**Note on `baseline`:** The `baseline` tag appears in two files. The primary anchor is
`01_structured_prompt_B.txt`; `00_baseline_prompt_A.txt` is used only as a pilot/smoke-test input.

---

## Inclusion Rules for Summary Tables

- **Quantitative aggregation:** `01_structured_prompt_B.txt` and its perturbations
  (`02_conflict_prompt.txt`, `03_long_prompt.txt`, `04_weak_prompt.txt`).
- **Excluded from quantitative summary tables:** `00_baseline_prompt_A.txt`.
  It may be referenced only in qualitative notes/examples.

---

## Variant Descriptions (English Summary)

- **baseline**  
  Defines the three-section output interface and serves as the reference input.

- **conflict**  
  Adds an additional, competing requirement while keeping the same interface.

- **long**  
  Adds redundant background and repeated guidance to increase input length.

- **weak**  
  Uses softer wording around constraints while keeping the same task.

---

## Reproducibility Notes

Each run records the prompt file name and a cryptographic hash to ensure
traceability across raw outputs, judged records, and aggregated summaries.

---

## Relation to Evaluation Rules

This directory contains only executable prompt inputs. Evaluation procedures and
definitions are specified separately under `03_evaluation_rules/`.