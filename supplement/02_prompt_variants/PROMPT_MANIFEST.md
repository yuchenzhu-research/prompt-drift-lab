# PROMPT_MANIFEST.md

# Prompt Inventory and Variable Definitions

This document defines the prompt assets, variable hierarchy, and statistical
scope used in this project, ensuring that comparisons across prompt variants are
reproducible, auditable, and well-defined.

---

## 0. Scope and Statistical Inclusion

- **Primary experiment (quantitative analysis)**: Uses **Prompt Family B (protocolized three-section format)** as the reference. Only **perturbed variants of B** (`baseline / conflict / long / weak`) are included in quantitative comparisons.
- **Pilot exploration (qualitative archive)**: `00_baseline_prompt_A_ZH.txt` corresponds to **Prompt Family A (exploratory)** and is used for motivation and failure-mode discovery. Unless A forms a complete, matched comparison under the same question set, parameters, and run counts, it is **excluded from primary quantitative summaries**.

In short: **statistics are anchored on B; A is used only to supplement observed phenomena and mechanism hypotheses**.

---

## 1. File Inventory

| File | Prompt Family | Prompt Variant | Intended Use |
|---|---|---|---|
| `00_baseline_prompt_A_ZH.txt` | A | baseline | Pilot exploration |
| `01_structured_prompt_B_ZH.txt` | B | baseline | Primary experimental anchor (protocol prompt) |
| `02_conflict_prompt_ZH.txt` | B | conflict | Introduce instruction tension; test priority failure |
| `03_long_prompt_ZH.txt` | B | long | Increase length and redundancy; test attention dilution |
| `04_weak_prompt_ZH.txt` | B | weak | Weaken constraints; test fallback to natural dialogue |

---

## 2. Variable Hierarchy (Family vs. Variant)

To avoid conflating prompt "versions" and "variants", variables are defined at
two distinct levels:

- **Prompt Family**: A vs. B (two distinct three-section templates)
- **Prompt Variant**: Single-factor perturbations applied within a given family
  (`baseline / conflict / long / weak …`)

All run artifacts (raw outputs, judged scores, summaries) are recommended to
explicitly record:

- `prompt_family`: `A` or `B`
- `prompt_variant`: `baseline` / `conflict` / `long` / `weak`

---

## 3. Prompt Family A: Exploratory (Pilot Baseline)

**Purpose**: Early-stage pipeline validation and failure-mode exposure.

**Commonly observed phenomena** (for qualitative logging):
- Structural drift: section merging, heading rewriting, missing fields
- Instruction deviation: ignored constraints, unauthorized task expansion
- Semantic drift: off-topic responses, stance-first narratives, overgeneralization
- Silent constraint loss: superficially relevant output missing critical actions or fields

**Statistical boundary**: Unless A forms a fully matched comparison with B under
identical question coverage and run protocol, it is not merged into B’s
quantitative results.

---

## 4. Prompt Family B: Protocolized Three-Section Format (Primary Anchor)

**Goal**: Encode output requirements as an executable and verifiable protocol,
so that drift is easier to detect, score, and trace via the rubric.

**Design principles** (as specified in the prompt text itself):
- Structural anchoring: clearer three-section boundaries for alignment and scoring
- Verifiable constraints: reduced gray zones of superficial compliance
- Mechanism orientation: encourages falsifiable hypotheses and minimal validation steps

---

## 5. Perturbation Space for Family B (Prompt Variants)

All variants below are derived from Family B. In principle, each variant modifies
only one primary dimension to form a minimal, controlled contrast.

### 5.1 `baseline` (`01_structured_prompt_B_ZH.txt`)

- **Use**: Primary experimental baseline.
- **Expectation**: Stable structure, complete fields, straightforward scoring.

### 5.2 `conflict` (`02_conflict_prompt_ZH.txt`)

- **Perturbation**: Introduces potentially conflicting or tension-inducing
  instructions to test priority resolution.
- **Typical failures**: Protocol bypass, unstable priority handling, partial
  alignment collapse.

### 5.3 `long` (`03_long_prompt_ZH.txt`)

- **Perturbation**: Increases prompt length and redundancy to test attention
  dilution and local forgetting.
- **Typical failures**: Partial compliance, submerged key constraints, task
  reinterpretation.

### 5.4 `weak` (`04_weak_prompt_ZH.txt`)

- **Perturbation**: Softens hard constraints into suggestive phrasing to test
  regression toward natural dialogue distributions.
- **Typical failures**: Structural breakdown, missing fields, increased silent
  constraint loss.

---

## 6. Reproducibility Records (Minimum Recommended Fields)

To ensure auditability, each run and evaluation is recommended to record the
following fields (e.g., in configs or sample metadata):

- `question_id`: Question identifier (e.g., Q1–Q4)
- `model`: Evaluated model
- `prompt_family` / `prompt_variant`
- `prompt_file`: Prompt file name
- `prompt_hash`: Content hash of the prompt (e.g., SHA-256)
- `temperature` / `top_p` / `seed` / `n_runs`
- `run_date`: Execution date (platform updates may affect behavior)

---

## 7. Constraints for Adding or Modifying Prompt Variants (Minimal Diffs)

When introducing new variants, the following constraints are recommended:

1. **Single factor**: Test only one hypothesis at a time (e.g., length, conflict,
   constraint strength, example placement)
2. **Identifiable change**: The modification point should be clearly attributable
   (readable diffs)
3. **Traceability**: Results should be comparable along the same dimension in
   aggregation and attribution

---

## 8. Alignment with Evaluation Rules

- Prompts define the **input perturbation space** (what is varied on the input side).
- Evaluation rules determine **output behavior** via fixed rubrics and validity criteria (what is measured on the output side).

All evaluation-related protocols, rubrics, and scoring logic are centralized under:

- `03_evaluation_rules/`
  - evaluation protocols (`EVAL_PROTOCOL.md`, `EVAL_PROTOCOL_ZH.md`)
  - validity criteria (`01_validity_criteria*.md`)
  - scoring dimensions and rubrics (`02_scoring_dimensions*.md`)
  - judge prompts (`JUDGE_PROMPT*.md`)
  - aggregation and verification scripts (`compute_scores*.py`)

**Separation of concerns**:
- Prompt variants are responsible for constructing controlled input perturbations.
- Evaluation rules are fixed and prompt-agnostic, and do not access prompt content directly.


