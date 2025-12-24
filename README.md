# Prompt Drift Lab
**A Reproducible Evaluation Framework for Instruction-Following Stability in Large Language Models**

> This repository is primarily documented in Chinese, while key model names, frameworks, and technical terms are preserved in English to align with academic and industrial conventions.
>
> Intended readers:
> - **Research reviewers / advisors**: interested in reproducibility, evidence chains, and attribution logic;
> - **Industry mentors / practitioners**: interested in executable evaluation loops, prompt version management, and failure-mode analysis.

---

## 1. Motivation (Why This Exists)

In real-world applications, the behavior of large language models (LLMs) can change significantly under **small variations in prompt format, wording, length, or constraint expression**. Common manifestations include:

- Decreased instruction-following performance;
- Structural or format breakdown (format break / schema violation);
- Semantic drift or off-topic responses;
- *Silent constraint violations*, where outputs appear compliant but omit critical requirements.

This project abstracts such prompt-sensitive behavioral degradation under the term **Prompt Drift**, and operationalizes it into a **reproducible, controlled, and attributable evaluation loop**:

> **Prompt design → Batch execution → Unified judging → Aggregation & comparison → Failure attribution → Iterative refinement**

---

## 2. What’s Inside the Repository

This repository covers the full evaluation pipeline for Prompt Drift, including:

- Fixed evaluation set and experimental setup: `01_experiment_design/`
- Prompt variants and intended differences: `02_prompt_variants/`
- Evaluation protocol and judge prompts: `03_evaluation/`
- Results, artifacts, and evidence entry points: `04_results/`
- Summary, limitations, and extrapolation boundaries: `05_summary_and_outlook/`
- Methodological addenda and A/B comparison rationale: `06_methodological_addenda_and_controls/`
- Deep research notes and reference materials: `07_deep_research/`

---

## 3. Research Questions

This project addresses the following questions:

- **RQ1: What are the primary manifestations of Prompt Drift?**  
  (instruction failure, structural breakdown, semantic drift, silent constraint omission)

- **RQ2: Which prompt perturbations are most likely to trigger degradation?**  
  (length expansion, conflicting instructions, weakened constraints, structural requirements)

- **RQ3: Do different models exhibit consistent sensitivity to the same perturbations?**  
  (cross-model robustness)

- **RQ4: Can failures be systematically attributed to actionable prompt design defects?**  
  (actionable prompt fixes)

---

## 4. Recommended Reading Path (30-Second Entry)

### 4.1 Where to Start

To quickly build a complete understanding of the evaluation loop—**protocol → prompt versions → judging → results → evidence**—we recommend the following order:

1. `01_experiment_design/README.md`: evaluation scope, assumptions, protocol, and field constraints
2. `02_prompt_variants/PROMPT_MANIFEST.md`: minimal-difference design of Prompt A/B and variants
3. `03_evaluation/EVAL_PROTOCOL.md` and `JUDGE_PROMPT.md`: scoring dimensions, compliance rules, and output schema
4. `04_results/README.md`: results index (summary / main_method / supporting_method / valid & invalid)
5. `04_results/03_results_analysis_EN.md`: comparative findings and failure attribution (traceable to PDFs and judge JSON)
6. `06_methodological_addenda_and_controls/README_EN.md`: methodological justification and A/B comparison rationale
7. `05_summary_and_outlook/README_EN.md`: limitations, external validity, and future directions

> **Core principle**: every conclusion in this repository must be traceable back to raw model outputs and per-sample judging records in `04_results/`.

### 4.2 Reproducibility Contract

- Fixed: evaluation set version, prompt version, model version, and sampling parameters
- Persisted: configuration, raw outputs, judged scores, and summary tables
- Any modification to protocols or prompts must be reflected in the corresponding manifests and README files

---

## 5. Method Overview

This project adopts a **protocol-driven evaluation** approach, transforming prompt-induced behavioral changes into controlled, reproducible, and attributable comparisons.

### 5.1 Prompt Variants

Comparison groups are constructed using **minimal differences**:

- **Prompt A (baseline)**: minimally viable, weakly structured natural-language prompt
- **Prompt B (structured)**: explicitly structured prompt with hard constraints (fields, ordering, prohibitions)
- **long**: expanded context and redundant explanations
- **weak**: systematically weakened constraint expressions
- **conflict**: introduction of instruction tension or potential conflicts

Design motivations and version details are documented in `02_prompt_variants/PROMPT_MANIFEST.md`.

### 5.2 Fixed Evaluation Set

A fixed evaluation set ensures comparability across prompts and models: `01_experiment_design/questions.jsonl`.  
At the current stage, the set size is intentionally limited to prioritize **observability and attribution** over task-space coverage.

### 5.3 Outputs as Evidence

For each `(prompt × question × model)` combination:

- Raw model outputs are preserved (PDF) as first-level evidence;
- A clear distinction is maintained between *model output failure* (experimental phenomenon) and *invalid evaluation artifacts* (data quality issues).

### 5.4 Judging and Scoring

All evaluations follow a unified protocol:

- `03_evaluation/EVAL_PROTOCOL.md`
- `03_evaluation/JUDGE_PROMPT.md`

Definitions of primary and supporting methods, aggregation rules, and consistency checks are indexed in `04_results/README.md`.

### 5.5 Aggregation and Attribution

Per-sample scores are aggregated into comparable tables and analyzed using the following discipline:

> Aggregated trends → grouped comparisons → sample-level backtracking (PDF + judge JSON)

This ensures that every reported observation is supported by a verifiable evidence chain.

---

## 6. Rubric and Failure Taxonomy

- **Hard Compliance**: structural correctness, field completeness, and prohibition enforcement
- **Behavioral Scores**: relevance, completeness, structural stability, and constraint satisfaction
- **Failure Taxonomy**: format errors, instruction deviation, semantic drift, silent constraint omission

Detailed definitions and scoring criteria are provided in `03_evaluation/`.

---

## 7. Why Prompt B over Prompt A

The methodological rationale for Prompt A/B differences, the three-step template comparative evaluation, and the decision to anchor the main experiment on Prompt B are consolidated in:

- `06_methodological_addenda_and_controls/A_B_comparative_rationale_EN.md`
- `06_methodological_addenda_and_controls/Prompt_A_B_three_step_template_comparative_evaluation.pdf`

This section addresses the evidence-chain question of *why Prompt B is selected as the main experimental anchor*, fully aligned with the statistical practices in `04_results/`.

---

## 8. Limitations

- The evaluation set is limited in size; external generalization should be treated with caution;
- Model versions, decoding parameters, and judge selection may affect observed boundaries;
- Fine-grained semantic distinctions may still require sampled manual review, using PDFs and judge JSON as evidence.

---

## 9. Citation

For reproduction, reporting, or follow-up research, please cite:

- This repository (Git commit hash or release tag)
- Evaluation protocol: `03_evaluation/EVAL_PROTOCOL.md`
- Judge prompts: `03_evaluation/JUDGE_PROMPT.md`
- Prompt inventory: `02_prompt_variants/PROMPT_MANIFEST.md`
- A/B comparison rationale: `06_methodological_addenda_and_controls/A_B_comparative_rationale_EN.md`