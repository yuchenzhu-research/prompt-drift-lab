# Prompt Inventory and Variable Definitions

This document defines the prompt assets, variable hierarchy, and statistical scope
used in this project. Its purpose is to ensure that comparisons across prompt
variants are reproducible, auditable, and well-defined.

---

## Prompt Language Note

All prompt files in this directory are written in English for structural clarity
and portability. During execution, these prompts are applied to **Chinese-language
questions and outputs**. The prompt language therefore does not indicate the
language of the evaluated task.

---

## 0. Scope and Statistical Inclusion

- **Primary experiment (quantitative analysis)**: Uses **Prompt Family B**
  (protocolized three-section format) as the reference. Only **perturbed variants
  of Family B** (`baseline`, `conflict`, `long`, `weak`) are included in
  quantitative comparisons.
- **Pilot exploration (qualitative archive)**: `00_baseline_prompt_A.txt`
  corresponds to **Prompt Family A (exploratory)** and is used for early pipeline
  validation and failure-mode discovery. Unless Family A forms a complete and
  matched comparison under identical questions, parameters, and run counts, it is
  excluded from primary quantitative summaries.

In short, **statistics are anchored on Family B; Family A is used only to
supplement observed phenomena**.

---

## 1. File Inventory

| File | Prompt Family | Prompt Variant | Intended Use |
|---|---|---|---|
| `00_baseline_prompt_A.txt` | A | baseline | Pilot exploration |
| `01_structured_prompt_B.txt` | B | baseline | Primary experimental anchor |
| `02_conflict_prompt.txt` | B | conflict | Instruction tension and priority stress |
| `03_long_prompt.txt` | B | long | Length and redundancy stress |
| `04_weak_prompt.txt` | B | weak | Constraint relaxation stress |

---

## 2. Variable Hierarchy

To avoid conflating prompt families and prompt variants, variables are defined at
two levels:

- **Prompt Family**: `A` or `B`
- **Prompt Variant**: `baseline`, `conflict`, `long`, `weak`

All run artifacts (raw outputs, judged scores, summaries) record the following
fields:

- `prompt_family`
- `prompt_variant`

---

## 3. Prompt Family A: Exploratory Baseline

**Purpose**: Early-stage pipeline validation and exposure of failure modes.

**Observed phenomena (qualitative logging)**:
- Structural drift (section merging, heading rewriting, missing fields)
- Instruction deviation (ignored constraints, unauthorized task expansion)
- Semantic drift (off-topic responses, stance-first narratives)
- Silent constraint loss (outputs that appear relevant but omit required actions
  or fields)

**Statistical boundary**: Unless Family A forms a fully matched comparison with
Family B under identical question coverage and run protocol, it is not merged
into quantitative results.

---

## 4. Prompt Family B: Protocolized Three-Section Format

**Role**: Serve as the primary experimental anchor.

**Design principles**:
- Structural anchoring: explicit section boundaries to support alignment and
  scoring
- Verifiable constraints: reduced ambiguity in compliance assessment
- Mechanism orientation: encourages falsifiable hypotheses and traceable failure
  modes

---

## 5. Perturbation Space for Family B

Each variant modifies a single primary dimension to create a minimal and
controlled contrast.

### 5.1 `baseline`

- Stable structure and complete fields
- Serves as the reference condition

### 5.2 `conflict`

- Introduces instruction tension to stress priority resolution
- Typical failures: protocol bypass, unstable priority handling

### 5.3 `long`

- Increases length and redundancy to stress attention and memory
- Typical failures: submerged constraints, partial compliance

### 5.4 `weak`

- Relaxes hard constraints into suggestive phrasing
- Typical failures: structural breakdown, missing fields

---

## 6. Reproducibility Records

Each run and evaluation records the following fields:

- `question_id`
- `model`
- `prompt_family`
- `prompt_variant`
- `prompt_file`
- `prompt_hash`
- `temperature`, `top_p`, `seed`, `n_runs`
- `run_date`

---

## 7. Constraints for Adding Prompt Variants

New variants must satisfy the following constraints:

1. Single-factor modification
2. Identifiable and attributable change
3. Traceability across aggregation and diagnosis

---

## 8. Alignment with Evaluation Rules

- Prompt variants define the **input perturbation space**.
- Evaluation rules define **output behavior** through fixed rubrics and validity
  criteria.

Evaluation protocols and scoring logic are centralized under:

- `supplement/03_evaluation_rules/`

Prompt variants do not access evaluation logic, and evaluation rules do not
inspect prompt content.

