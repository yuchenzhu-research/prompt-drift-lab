# Five-Step Experimental Workflow

This document describes the end-to-end experimental workflow of Prompt Drift Lab, with emphasis on reproducibility, auditability, and explicit handling of failure cases. The workflow is designed to surface not only successful executions but also systematic failure patterns that inform drift analysis.

---

## Step 1: Identify Core Artifacts

Each reproducible evaluation batch produces the following artifact categories:

1. Raw model outputs preserved verbatim
2. Per-sample evaluation records with rubric scores and validity flags
3. Aggregated summaries derived from scored records
4. Failure and drift diagnosis notes capturing non-compliant behaviors
5. Protocol and configuration records defining execution context

These categories define logical roles rather than fixed filenames. Concrete file realizations are specified elsewhere in the repository.

---

## Step 2: Define Task and Output Contract

**Objective:** Fix the evaluation target so that observed changes can be attributed to prompt perturbations rather than task drift.

- Evaluation questions are drawn from the predefined question set.
- A standard output contract specifies the required section structure.
- Evaluation focuses on structural adherence and instruction following rather than content correctness.

---

## Step 3: Apply Minimal Prompt Perturbations

**Objective:** Introduce controlled variations that remain interpretable.

Prompt variants include baseline, long, weak, and conflict conditions. Constraint signaling is applied at implicit and explicit levels. These variants modify constraint strength, verbosity, and instruction clarity without altering the underlying task.

---

## Step 4: Execute and Preserve Evidence

**Objective:** Ensure traceability and auditability of all generated outputs.

All model outputs are preserved in their original form without manual modification. Each output is associated with execution metadata, including model identifier, prompt variant, constraint level, question identifier, and replicate index.

---

## Step 5: Score, Aggregate, and Analyze Failures

**Objective:** Convert observed behaviors into analyzable records and explicitly characterize failure modes.

- Each output is scored using fixed rubric dimensions.
- Unscorable outputs are marked invalid under strict criteria.
- Aggregation is performed across variants and models using scored records only.

In addition to aggregated scores, the workflow explicitly records and analyzes failure cases. Failure patterns are derived exclusively from rubric-scored records and schema-defined invalidity flags, rather than post-hoc interpretation. Failure analysis focuses on identifying recurring patterns such as structural collapse, instruction substitution, constraint violations, and task rewrites. These failure patterns are treated as primary observations rather than noise and are used to inform drift characterization and methodological discussion.