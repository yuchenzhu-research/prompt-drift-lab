# Five-Step Experimental Workflow

This document specifies the experimental workflow used in the Prompt Drift Lab.

It answers a single question:

**How is the Prompt Drift Lab experiment conducted in a reproducible, iterative,
and auditable manner?**

- What is studied: whether **small, controlled changes in prompts, wording, or
  constraint strength** produce **instruction-following degradation, structural
  breakdown, or semantic drift** in large language model outputs.
- What is evaluated: **instruction adherence and output structure compliance**.
  Content correctness is not evaluated.

This document functions as a **methodological protocol**. It does not define
numerical hyperparameters or ground-truth values. All executable settings are
specified in `supplement/01_experiment_design/experiment_protocol_ZH.yaml`.

---

## Step 0: Identify the Core Artifacts

A single reproducible experimental batch (an *Eval Bundle*) produces the
following conceptual artifacts:

1. **Raw model outputs**: preserved verbatim as execution evidence
2. **Per-sample evaluation records**: rubric scores and invalid-case annotations
3. **Aggregated summaries**: summary tables and distributions
4. **Drift diagnosis notes**: categorized failure-mode observations
5. **Protocol record**: model, parameters, and prompt variants used

These artifacts define **logical roles**, not fixed filenames. Their concrete
realizations are defined elsewhere in the repository:

- Output structure definition: `supplement/01_experiment_design/output_schema_ZH.md`
- Evaluation questions: `supplement/01_experiment_design/eval_questions_ZH.jsonl`
- Evaluation protocol (authoritative): `supplement/03_evaluation_rules/EVAL_PROTOCOL_ZH.md`
- Scope boundaries and risks: `supplement/01_experiment_design/threats_and_limitations_ZH.md`

---

## Step 1: Define the Evaluated Task and Output Structure

**Objective:** Fix the evaluation target so that observed changes can be
attributed to prompt perturbations rather than task drift.

Two elements are held constant:

### 1.1 Evaluation Questions

- Questions are selected from `eval_questions_ZH.jsonl`.
- Each question corresponds to a distinct structured-output task type
  (e.g., multi-section formats, strict templates, conflicting constraints).

### 1.2 Standard Output Structure

- The required output structure is defined in `output_schema_ZH.md`.
- Evaluation focuses on **structural compliance**, not answer quality.

---

## Step 2: Define Minimal Prompt Perturbations

**Objective:** Introduce controlled variations that are interpretable and
isolatable.

Prompt variants include:

- `baseline`: reference variant
- `long`: verbose variant with repeated constraints
- `weak`: variant with relaxed constraints
- `conflict`: variant containing conflicting or ambiguous instructions

Constraint signaling is defined at two levels:

- `implicit`: structure is suggested but not enforced
- `explicit`: structure is specified as mandatory

---

## Step 3: Generate Outputs and Preserve Evidence

**Objective:** Ensure traceability and auditability of all generated outputs.

All model outputs are preserved verbatim as execution evidence, without manual
post-processing.

Each output record is associated with:

- Generator model identifier
- Execution timestamp (approximate)
- Prompt variant and constraint level
- Question identifier
- Replicate index

---

## Step 4: Score with the Rubric and Handle Invalid Cases

**Objective:** Convert observed behavior into analyzable records using fixed
criteria.

Each preserved output is scored using the rubrics and validity rules defined in
`supplement/03_evaluation_rules/`.

The `invalid` label is reserved exclusively for **unscorable outputs**, including:

- Explicit refusal or complete task substitution
- Severe truncation preventing structural judgment
- Outputs containing no evaluable content

**Clarifications:**

- Low-quality outputs are scored, not marked invalid.
- A sample is marked invalid only when scoring is not possible.

---

## Step 5: Aggregation and Drift Diagnosis

**Objective:** Derive findings from scores and feed them into subsequent
iterations.

Scores are aggregated along predefined dimensions such as:

- Prompt variant
- Constraint signaling level
- Generator model

Aggregation artifacts (e.g., summary tables or plots) are derived views computed
from scored records and do not introduce new evaluation rules.

Observed failures are assigned to predefined failure modes, including:

- `format_drift`
- `role_confusion`
- `constraint_violation`
- `task_rewrite`
- `verbosity_overflow`