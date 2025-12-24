# EVAL_PROTOCOL

> Goal: Ensure that any evaluation-side terminology such as “baseline / version / prompt” is **fully consistent** with:
> - `01_experiment_design/`
> - `02_prompt_variants/`
>
> Core constraint: **The evaluation process is A/B-blind and judges samples strictly based on metadata and outputs.**

---

## 0. Scope
This protocol defines how existing experimental artifacts are evaluated and aggregated. It covers:
- Instruction-following degradation
- Format break / schema violations
- Semantic drift / task deviation
- (Optional) Citation or search behavior drift

Out of scope:
- Re-running models (this protocol evaluates *existing* outputs only)
- Subjective inference on prompt text (evaluation relies on **metadata + outputs**, not prompt content)
- Introducing new metrics or dimensions (dimension definitions are authoritative elsewhere)

---

## 1. Terminology and Naming
### 1.1 Single Source of Truth
- **Official names for prompt variants / versions / baselines are defined in `02_prompt_variants/`.**
- **Official names for eval sets / dataset versions are defined in `01_experiment_design/`.**
- This protocol introduces no new external terminology. Any new terms must be internal to evaluation operations and must not conflict with 01/02.

### 1.2 Terminology Alignment Table (Must Match 01/02 Exactly)
> Copy the “official naming” verbatim from 01/02 to ensure that each concept has a single, unambiguous name throughout the project.

| Concept | Official Naming (from 01/02) | Description | Deprecated / Disallowed Aliases |
|---|---|---|---|
| Prompt Variant / Version | (to be filled) | e.g., prompt_a / prompt_b, or vA / vB as defined in 02 | (to be filled) |
| Prompt Set / Pack | (to be filled) | e.g., promptset / prompt_pack, per 02 | (to be filled) |
| Baseline | (to be filled) | Must specify whether this is a prompt baseline or model baseline | (to be filled) |
| Eval Set | (to be filled) | e.g., eval_set_v*.jsonl, per 01 | (to be filled) |
| Run | (to be filled) | e.g., runs/YYYY-MM-DD_<model>_<promptset>/, per 01 | (to be filled) |

### 1.3 A/B-Blind Principle
- The evaluation side **does not read** prompt content.
- The evaluation side **does not use** “A/B” as a scoring prior.
- Grouping and aggregation rely solely on sample metadata fields such as:
  - `prompt_version` / `prompt_id` / `promptset`
  - `eval_set_version`
  - `model`
  - `run_id`
- If critical metadata is missing, the sample must be treated as *metadata-incomplete* and must not be repaired by inference.

---

## 2. Inputs and Evaluation Units
### 2.1 Evaluation Inputs
Evaluation inputs consist of one or more run directories. Each run must contain at minimum:
1. Configuration (model / temperature / sampling / seed / prompt version / eval set version)
2. Raw outputs (unaltered model outputs)
3. Judged scores (per-question, per-dimension scores with evidence)
4. Summary (one aggregated row per run)

File presence and naming conventions follow the definitions in `01_experiment_design/`.

### 2.2 Evaluation Unit
- The atomic evaluation unit is **a single sample output**, typically:
  *one model × one prompt version × one question × one generation*.
- Each sample must be traceable to metadata (run_id, model, prompt_version, eval_set_version, question_id, etc.).

---

## 3. Dimension Binding (Rubric = dimensions + validity + judge prompt)
### 3.1 Source of Truth
In this repo, the “Rubric” is defined by the following **concrete files**:
- **Scoring dimensions + bands:** `03_evaluation_rules/02_scoring_dimensions.md`
- **Validity (valid/invalid gating):** `03_evaluation_rules/01_validity_criteria.md`
- **Judge prompt (exact judging instruction):** `03_evaluation_rules/JUDGE_PROMPT.md`

This protocol specifies **how these documents are applied**, not how they are extended.

### 3.2 Failure Taxonomy (For Attribution Only)
The following tags may be used in rationales for attribution (multi-label allowed):
- A. Schema / format error
- B. Instruction deviation
- C. Semantic drift
- D. Robustness issues (variance)
- E. Evaluation gaming

These tags do not introduce new scoring dimensions and do not alter dimension definitions.

---

## 4. Evaluation Procedure
### 4.1 Pre-check
For each run:
1. Verify configuration metadata is complete and parseable (`model`, `sampling`, `seed`, `prompt_version`, `eval_set_version`).
2. Verify raw outputs are truly raw and unmodified.
3. If missing elements are found, record `input_incomplete`; existing samples may still be evaluated.

### 4.2 Sample-level Scoring
For each sample output:
1. Read the question (and reference information, if provided by the eval set).
2. Score strictly based on the output text and the dimension definitions.
3. Record:
   - Per-dimension scores
   - Evidence snippets (short excerpts from the output)
   - Failure attribution tags (A–E)
4. **Must not**:
   - Adjust scores based on prompt version identity
   - Assume an A/B comparison during scoring

### 4.3 Aggregation and Statistics
- All aggregated numbers must be reproducible from metadata-defined groupings.
- Allowed grouping keys are metadata fields only (e.g., prompt_version, model, eval_set_version).
- A/B comparisons are performed **only at the aggregation stage**, never during scoring.

---

## 5. Outputs and Persistence
### 5.1 Judged Scores (Per-sample Records)
Each sample must generate one record containing at least:
- `run_id`
- `model`
- `prompt_version`
- `eval_set_version`
- `question_id`
- `scores` (organized by dimensions)
- `evidence` (short excerpts)
- `failure_tags` (A–E, multi-label)

Field names follow existing implementations in 01/02. This protocol does not mandate renaming legacy fields.

### 5.2 Summary (One Row per Run)
Each run must produce a single summary row containing at least:
- Run identifier (consistent with directory naming)
- Sample count
- Mean / proportion statistics per dimension
- Proportions of key failure types (A–E)

---

## 6. Consistency and Auditability
### 6.1 Reproducibility Acceptance Criteria
A run is considered reproducible if:
- Every value in the summary table can be recomputed from the run directory
- Any judged score record can be traced back to its corresponding raw output and configuration

### 6.2 Terminology Consistency Check
A full-text audit across this file, `JUDGE_PROMPT`, and `00_evaluation_protocol` must confirm:
- Identical spelling and usage of key terms such as “baseline”, “version”, “prompt_version”, “promptset”, and `eval_set_version`
- No multiple aliases for the same concept

---

## 7. Change Log
- Step (Alignment): updated references to match repo structure (`02_prompt_variants/`); bound “Rubric” to concrete files (`02_scoring_dimensions`, `01_validity_criteria`, `JUDGE_PROMPT`).
