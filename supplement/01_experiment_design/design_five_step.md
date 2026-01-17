# Five-Step Experimental Workflow

This document describes the end-to-end experimental workflow of Prompt Drift Lab. It documents how experimental inputs are prepared, how model outputs are generated and preserved, and how evidence is organized for downstream processing. It does not define evaluation criteria, scoring logic, or validity rules.

---

## Step 1: Identify Core Artifacts

Each reproducible evaluation batch produces the following artifact categories:

1. Raw model outputs preserved verbatim
2. Per-sample processing records derived from raw outputs
3. Aggregated summaries derived from downstream processing
4. Failure and drift observation notes derived from recorded outputs
5. Protocol and configuration records defining execution context

These categories describe logical roles rather than fixed filenames. Concrete file realizations are specified elsewhere in the repository.

---

## Step 2: Define Task and Output Contract

**Objective:** Fix the task formulation and output structure so that observed changes can be attributed to prompt perturbations rather than task drift.

- Evaluation questions are drawn from the predefined question set.
- A standard output contract specifies the required section structure.
- This document records the existence of an output contract but does not restate or interpret any evaluation criteria.

---

## Step 3: Apply Minimal Prompt Perturbations

**Objective:** Introduce controlled prompt variations that remain interpretable.

Prompt variants include baseline, long, weak, and conflict conditions. Constraint signaling is applied at implicit and explicit levels. These variants modify prompt wording and instruction emphasis without altering the underlying task specification.

---

## Step 4: Execute and Preserve Evidence

**Objective:** Ensure traceability and auditability of all generated outputs.

All model outputs are preserved in their original form without manual modification. Each output is associated with execution metadata such as model identifier, prompt variant, trigger type, and question identifier.

---

## Step 5: Organize Outputs for Downstream Evaluation

**Objective:** Prepare generated outputs for downstream evaluation and analysis without defining evaluation logic.

Generated outputs are organized and stored to support downstream evaluation, aggregation, and analysis. All evaluation criteria, validity handling, scoring procedures, and failure definitions are specified exclusively in `supplement/03_evaluation_rules/` and are not duplicated or interpreted here.