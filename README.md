# Prompt Drift Lab
**A reproducible evaluation scaffold for instruction-following stability under prompt perturbations (prompt drift).**

> Bilingual repo policy:
> - Files **without** `_ZH` are the **English** version.
> - Files **with** `_ZH` are the **Chinese** version.
>
> Note on PDFs:
> - Many PDFs under `07_deep_research/` are **Chinese-only**. English native readers may not be able to read them.
> - They are kept here **for citation, traceability, and experiment record-keeping** (not as “required reading”).

- 中文版入口：[`README_ZH.md`](README_ZH.md)

---

## 0) 30-second start

1. **Experiment design** → `01_experiment_design/README.md`
2. **Generator prompts & variants** → `02_prompt_variants/README.md`
3. **Evaluation rules (protocol + judge contract)** → `03_evaluation_rules/README.md`
4. **Results artifacts & tables** → `04_results/README.md`
5. **Interpretation + boundaries (no new experiments)** → `05_summary_and_outlook/README.md`

---

## 1) What this repo contains (by folder)

- `01_experiment_design/`  
  Questions (`eval_questions_*.jsonl`), experiment protocol (`experiment_protocol*.yaml`), output schema, and terminology alignment.

- `02_prompt_variants/`  
  **Generator-side** prompts + controlled variants (A/B/…); manifest files mapping `prompt_id/prompt_version -> file`.

- `03_evaluation_rules/`  
  **Judge-side** contract: protocol, validity criteria, scoring dimensions, and schema.
  - Key entrypoints: `EVAL_PROTOCOL.md`, `JUDGE_PROMPT.md`

- `04_results/`  
  Raw outputs, judged JSON/CSV tables, and analysis notes. This is the “evidence layer”.

- `05_summary_and_outlook/`  
  The **interpretive layer**: result-level summaries, implications, explicit non-claims, and future work ideas  
  (must remain traceable to `04_results/` and `03_evaluation_rules/`).

- `06_methodological_addenda_and_controls/`  
  Rationale, controls, and methodological notes that explain *why this setup* (without overstating claims).

- `07_deep_research/`  
  Literature notes and PDFs (often Chinese-only) kept for **citation/record**.

---

## 2) Claim boundary (important)

- This repo is **artifact-first**: prompts, protocol, outputs, scoring, and tables are explicit.
- Any interpretation should be **traceable** to:
  - results in `04_results/`, and
  - rules in `03_evaluation_rules/`.
- Do **not** treat this repo as a benchmark with broad generalization claims beyond the recorded setup.

---

## 3) Quick reproducibility

- Re-score / re-aggregate from existing judged outputs:
  - see `03_evaluation_rules/compute_scores.py`
- Full re-run (re-generating model outputs) requires external model access and is not bundled as a single turnkey script in this repo.

---

## 4) Naming conventions

- `_ZH` suffix = Chinese counterpart file.
- Prefer stable ids (`question_id`, `prompt_id`, `prompt_version`) to keep runs auditable.
