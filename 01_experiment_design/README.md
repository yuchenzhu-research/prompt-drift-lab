# Experiment Design

This directory defines the experimental design of **Prompt Drift Lab**.
It specifies the evaluation tasks, controlled variables, output constraints,
and reproducibility assumptions used throughout all experiments.

The core focus of this project is **prompt-induced behavior drift** in large
language models, where the underlying task semantics remain unchanged while
the prompt formulation varies.

---

## Research Objective

The objective of this experiment is to study how **minimal or non-semantic
prompt variations** can lead to observable changes in model behavior, including:

- Instruction-following degradation
- Output format or schema violations
- Semantic deviation from the intended task
- Increased variance across repeated runs

This study does **not** aim to evaluate general task performance or language
understanding, but rather the **robustness of instruction following** under
prompt perturbations.

---

## Evaluation Tasks

The evaluation tasks consist of a small, fixed set of questions covering
multiple categories, including:

- Factual queries
- Photography-related knowledge
- Model behavior and instruction-following scenarios
- Prompting and meta-level reasoning questions

Each question is assigned a stable identifier (e.g., `Q1`, `Q2`, `Q3`, `Q4`)
and is reused across all prompt variants to ensure comparability.

---

## Evaluation Language Note

All experiments are conducted using the original **Chinese** evaluation
questions (`eval_questions_ZH.jsonl`).

An English-translated version (`eval_questions_EN.jsonl`) is provided **solely
for reviewer readability** and documentation purposes.
The translated questions are **not used as experimental inputs** and do not
affect the evaluation setup or results.

---

## Controlled Variables

To isolate prompt-induced effects, the following variables are held constant
across experimental conditions:

- Task semantics
- Evaluation questions
- Model version
- Decoding configuration
- Evaluation and scoring protocol

The **only manipulated factor** in the experiment is the **prompt formulation**
(e.g., structure, length, explicitness, or internal constraint conflicts).

---

## Required Output Structure

All model outputs are evaluated against a **strict three-section format**:

1. **[Fact Snapshot]**
2. **[ChatGPT Web Search Instruction]**
3. **[Gemini Deep Research Instruction]**

The required section order and content constraints are defined in
`output_schema.md`. Outputs that violate section order, omit required sections,
or exceed defined constraints are treated as structural failures during
evaluation.

---

## Experiment Protocol

The exact evaluation protocol used in the current experimental run is specified
in `experiment_protocol.yaml`.

This protocol is aligned with existing evaluation artifacts and documents
only configurations that have already been executed and scored. No future or
hypothetical settings are included.

---

## Reproducibility Assumptions

The experiment is designed with reproducibility as a primary constraint:

- Each evaluated output is associated with a specific prompt version and
  evaluation protocol version
- Scoring criteria are deterministic and explicitly documented
- Evaluation records capture per-dimension scores and supporting evidence

All experimental results can be traced back to their corresponding inputs,
outputs, and evaluation records.

---

## Directory Contents

- `README.md`  
  English overview of the experimental design (this file)

- `README_ZH.md`  
  Chinese reference version

- `eval_questions_ZH.jsonl`  
  Original Chinese evaluation questions used in all experiments

- `eval_questions_EN.jsonl`  
  English translations of the evaluation questions for reviewer readability only

- `experiment_protocol.yaml`  
  Evaluation protocol aligned with the current experimental run

- `experiment_protocol_ZH.yaml`  
  Chinese reference version of the evaluation protocol

- `output_schema.md`  
  Specification of the required output format and constraints

- `output_schema_ZH.md`  
  Chinese reference version of the output format specification

- `design_five_step.md`  
  Step-by-step description of the experimental design process

- `design_five_step_ZH.md`  
  Chinese reference version of the design process description

- `terminology_alignment.md`  
  Alignment of key terms used across design, evaluation, and analysis

- `terminology_alignment_ZH.md`  
  Chinese reference version of terminology alignment

- `threats_and_limitations.md`  
  Known limitations and potential threats to validity

- `threats_and_limitations_ZH.md`  
  Chinese reference version of threats and limitations
