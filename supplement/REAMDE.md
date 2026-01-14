# Supplement Artifact Pack README

This `supplement/` directory is the complete artifact set referenced by the paper. It is organized for **auditability** and **inspection-driven reproducibility**: reviewers can trace every reported number and every failure case back to preserved raw outputs and fixed evaluation contracts.

No script in this directory is required to be executed by reviewers.

---

## 1) Language Policy and What Is Actually Chinese

This project was executed with **Chinese experimental inputs** but is packaged for **English-speaking review**.

**Chinese (execution inputs):**
- The **authoritative question set** is Chinese and consists of four questions:
  - `01_experiment_design/eval_questions_ZH.jsonl`
- All **generator-side prompt variants used for execution** are Chinese:
  - `02_prompt_variants/00_baseline_prompt_A.txt`
  - `02_prompt_variants/01_structured_prompt_B.txt`
  - `02_prompt_variants/02_conflict_prompt.txt`
  - `02_prompt_variants/03_long_prompt.txt`
  - `02_prompt_variants/04_weak_prompt.txt`

**English (documentation and evaluation contracts):**
- Experimental protocol, output schema, evaluation rules, rubrics, validity criteria, and methodological notes are documented in English across the supplement directories.

**Raw outputs (as generated):**
- The preserved model outputs are stored as **48 raw PDF files** under:
  - `04_results/01_raw_model_outputs/`
- These PDFs are kept verbatim as the evidence layer; they are not edited or cleaned.

---

## 2) What Each Supplement Directory Does

- `01_experiment_design/` — **Design contracts and inputs**
  - Defines the question partitioning (development vs held-out), the execution protocol, and the output structure contract.
  - Contains terminology alignment and explicit threats/limitations for audit and correct interpretation.

- `02_prompt_variants/` — **Generator-side prompt definitions**
  - Stores the Chinese prompt variants used to produce raw outputs.
  - Provides an English-readable description of each variant’s role without introducing an alternative executable prompt set.

- `03_evaluation_rules/` — **Judging and scoring contracts**
  - Defines validity boundaries, scoring dimensions, failure flags, and taxonomy.
  - This is the single location for how outputs are judged and aggregated.

- `04_results/` — **Frozen evidence and derived records**
  - Stores raw model outputs (PDF), per-sample judged records, invalid reports, and summary tables.
  - All reported quantitative results are traceable to artifacts in this directory.

- `05_methodological_addenda_and_controls/` — **Methodological clarifications and control boundaries**
  - Documents design rationale that protects interpretation (e.g., why exploratory failure discovery is separated from protocolized measurement).
  - Extends the narrative without changing execution protocols or scoring rules.

- `tools/` — **Inspection utilities (non-required)**
  - Helper scripts and notes for inspection, formatting checks, and artifact maintenance.
  - These utilities do not define experimental logic, prompt content, or evaluation criteria.

---

## 3) Development vs Evaluation: Why Q1–Q2 and Prompt A Matter

The experiment enforces a strict separation between **prompt development** and **held-out evaluation**.

### Q1–Q2: Development-only (paper emphasis)

- **Q1–Q2** are used exclusively to construct and refine the generation prompts.
- They are deliberately treated as an exploratory surface to expose early failure modes (e.g., structural collapse, instruction substitution, constraint leakage).
- Outputs from this stage are not aggregated into reported quantitative results.

This separation prevents development–evaluation leakage and is central to the paper’s methodological framing.

### Prompt A (00_baseline_prompt_A.txt): Exploratory failure discovery (paper emphasis)

- Prompt **A** is an intentionally minimal baseline used to probe the failure surface during development.
- Its purpose is **failure discovery**, not comparative measurement.
- It motivates later protocolization by showing what breaks when constraint signaling is weak.

### Prompt B (01_structured_prompt_B.txt): Measurement anchor

- Prompt **B** is the protocolized anchor for quantitative evaluation.
- All reported comparisons across variants are defined as controlled perturbations of Prompt B.

The A/B separation is documented as a methodological control: failure discovery is decoupled from failure measurement to preserve the integrity of quantitative interpretation.

---

## Suggested Reviewer Inspection Flow

1. Read design contracts and partitioning in `01_experiment_design/`.
2. Inspect the prompt variants and their roles in `02_prompt_variants/`.
3. Verify validity criteria, rubric dimensions, and failure taxonomy in `03_evaluation_rules/`.
4. Trace raw PDFs → judged records → summary tables in `04_results/`.
5. Use `05_methodological_addenda_and_controls/` for interpretation boundaries and controls.

---

## Notes on Reproducibility

- This artifact is intended for **auditability and traceability** rather than deterministic re-execution of model inference.
- API-driven regeneration is intentionally avoided to prevent nondeterministic reproduction paths caused by model updates and system-side changes.