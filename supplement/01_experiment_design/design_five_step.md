# Five-Step Experimental Workflow

This document answers a single question:

**How is the Prompt Drift Lab experiment conducted in a way that is reproducible,
iterative, and statistically analyzable?**

- What we study: whether **small changes in prompts, wording, or constraint strength**
  lead to **instruction-following degradation, structural breakdown, or semantic drift**
  in large language model outputs.
- What we evaluate: **whether the model follows instructions and preserves the required
  output structure**, not whether the content itself is correct.

> This document serves as a *methodological guide*.
> It does not define hard parameters or ground-truth values.
> All concrete experimental settings are specified in
> `experiment_protocol.yaml`.

---

## Step 0: Identify the Five Core Artifacts (What You Ultimately Produce)

A single reproducible experimental batch (an *Eval Bundle*) produces at least the
following artifacts:

1. **Raw model outputs** (PDF): primary evidence of model behavior  
2. **Eval Bundle JSON**: per-file rubric scores and invalid-case records  
3. **Aggregated summaries** (optional): mean scores, distributions, failure patterns  
4. **Drift diagnosis notes** (optional): where and why failures occur  
5. **Protocol record**: model, parameters, and versions used (recorded in `experiment_protocol.yaml`)

These artifacts correspond to the following files in the repository:

- Output structure definition: `output_schema.md`
- Evaluation questions: `eval_questions_ZH.jsonl`
- Experimental protocol (source of truth): `experiment_protocol.yaml`
- Risks and boundaries: `threats_and_limitations.md`

---

## Step 1: Define the Evaluated Task and Output Structure (Task Specification)

**Goal:** Ensure the evaluated target is *stable*.
If the task itself keeps changing, drift cannot be attributed.

Two elements must be fixed:

### 1.1 Evaluation Questions (Task Definition)

- Select questions Q1–Q4 from `eval_questions_ZH.jsonl`
- Each question represents a distinct structured-output task type
  (e.g., three-section format, strict templates, conflicting constraints)

### 1.2 Standard Output Structure (Output Schema)

- Defined in `output_schema.md`
- The evaluation focuses on **structural compliance**, not answer quality

**Checkpoint (must pass before Step 2):**
- Question text remains stable (do not modify questions mid-run)
- Output structure remains stable (section definitions and templates unchanged)

---

## Step 2: Define Minimal Prompt Perturbations (Prompt Variants)

**Goal:** Keep variations interpretable and attributable.

Common prompt variants (examples):

- `baseline`: normal reference version  
- `long`: longer, more verbose, repetitive constraints  
  (tests the assumption “longer prompts improve compliance”)  
- `weak`: weakened hard constraints  
  (tests whether structure relies on strong instructions)  
- `conflict`: introduces ambiguity or conflicting requirements  
  (tests how models resolve or collapse under conflict)

Trigger strength is also defined:

- `implicit`: structure is suggested or implied  
- `explicit`: strict and mandatory structural instructions  

**Checkpoint:**
- Differences between variants are intentional and describable in one sentence
- Do not modify multiple independent factors simultaneously (attribution will fail)

---

## Step 3: Generate Outputs and Preserve Evidence (Run → Archive)

**Goal:** Ensure every sample is traceable and auditable.

### 3.1 Recommended File Naming Convention

A unified file naming scheme is strongly recommended to ensure that each output is
traceable, machine-parseable, and easy to aggregate in downstream analysis.

The following format is used throughout the project:

```
q{QID}_{version}_{trigger}_{model}_r{rep}.pdf
```

Where:

- `QID` refers to the evaluation question identifier (e.g., Q3, Q4)
- `version` refers to the prompt variant (e.g., baseline, long, weak, conflict)
- `trigger` refers to the instruction style (implicit or explicit)
- `model` refers to the generator model name
- `rep` refers to the replicate index of the run

**Examples:**

- `q3_baseline_explicit_chatgpt_r1.pdf`
- `q4_conflict_implicit_gemini_r2.pdf`


### 3.2 Runtime Metadata (Strongly Recommended)

Each output should be traceable to:

- Generator model (exact version or UI label)
- Approximate timestamp
- Decoding parameters (e.g., temperature, top_p)
- Prompt version, trigger type, question ID, replicate index

> This metadata may be embedded in the PDF header or stored in a separate run log.
> *Being able to align evidence with the protocol is a baseline requirement
> for workshop-level projects.*

**Checkpoint:**
- Outputs are preserved as raw evidence (no manual edits)
- Filenames are machine-parseable for downstream aggregation

---

## Step 4: Score with the Rubric and Handle Invalid Cases (Score → Validate)

**Goal:** Convert qualitative behavior into analyzable data.

### 4.1 Rubric-Based Scoring

Each PDF is scored across multiple dimensions (e.g., 0/1/2 scale), such as:

- `A_structure`: whether the required structure is preserved
- `B_snapshot_constraint`: whether the fact snapshot is factual and non-analytic
- `C_actionability`: whether instructions are executable
- `D_completeness`: whether required components are covered
- `E_drift_failure`: whether obvious drift or task deviation occurs

> Detailed rubric definitions are specified in `03_评测规则/`
> and are not repeated here.

### 4.2 Definition of Invalid Samples

The `invalid` label is reserved strictly for **unscorable outputs**, such as:

- Explicit refusal, casual chat, or complete task change
- Severe truncation preventing structural judgment
- Outputs containing no scorable content

**Important:**
- Poor performance ≠ invalid
- If a sample can be scored, it should receive a low score rather than be marked invalid

**Checkpoint:**
- Every file is either included in `per_file_scores` or `invalid_files`
- Each invalid case must include an explicit reason

---

## Step 5: Aggregation and Drift Diagnosis (Aggregate → Diagnose → Iterate)

**Goal:** Turn scores into findings, and findings into the next experiment.

### 5.1 Minimal Aggregation (Recommended)

At minimum, aggregate results along:

- Prompt version (`baseline / long / weak / conflict`)
- Trigger type (`implicit / explicit`)
- Generator model (`chatgpt / gemini / claude`)

Outputs may include:

- `results/summary.csv` (or an equivalent summary table)
- A short set of qualitative observations (recorded in notes)

### 5.2 Drift Diagnosis via Failure Modes

Observed failures are categorized into reusable failure modes, such as:

- `format_drift` (loss of required structure)
- `role_confusion` (role mixing or conversational shift)
- `constraint_violation` (explicit rule violations)
- `task_rewrite` (reinterpreting the task)
- `verbosity_overflow` (excessive explanation breaking the template)

### 5.3 Iteration Rules (Preventing Uncontrolled Drift)

- Modify only one variable per iteration (prompt version, trigger, or question)
- Each new variant must state the hypothesis it is testing
- All changes must be recorded back into `experiment_protocol.yaml`
  to maintain a single source of truth

**Checkpoint:**
- Can you clearly state the *main conclusion* of this run?
- Can you clearly state the *causal hypothesis* tested in the next iteration?
