# 04 Results (Index)

**You are here:** `04_results/README.md`  
**Upstream:** `01_experiment_design/` → `02_prompt_variants/` → `03_evaluation_rules/`  
**Downstream:** `05_summary_and_outlook/`  
**Sidecar:** `06_methodological_addenda_and_controls/` (controls & rationale)

## Purpose
This folder contains **all evidence artifacts** for the reported results:
- aggregated tables (CSV),
- evaluation bundles (JSON),
- raw model outputs (PDF),
- valid vs. invalid buckets for auditability.

> This file is an **index only** (where things are).  
> For interpretation, failure modes, and attribution logic, see: `04_results/03_results_analysis.md`.

---

## 30-second entry: where the numbers are

### 1) Main summary (start here)
- **Global summary table:**  
  `04_results/02_cross_model_evaluation/valid_evaluations/summary_tables/summary.csv`

### 2) Breakdown tables (for slicing)
- `.../summary_tables/main_method_by_*.csv`
- `.../summary_tables/supporting_method_by_*.csv`
- `.../summary_tables/main_method_inter_judge_agreement.csv`

---

## Where the evidence files are

### A) Raw model outputs (generation artifacts)
- `04_results/01_raw_model_outputs/`  
  (PDFs grouped by generator model)

### B) Valid evaluations (included in aggregation)
- **Main method (cross-model judging):**  
  `04_results/02_cross_model_evaluation/valid_evaluations/main_method_cross_model/`
- **Supporting method (self-eval; sanity-check only):**  
  `04_results/02_cross_model_evaluation/valid_evaluations/supporting_method_self_eval/`

### C) Invalid evaluations (excluded from aggregation; used for diagnosis)
- `04_results/02_cross_model_evaluation/invalid_evaluations/`
  - `invalid_evaluations/README.md` (how invalid is defined + flags)
  - `invalid_evaluations/used_evaluation_protocol.md` (protocol snapshot)
  - `invalid_evaluations/used_prompt_manifest.md` (prompt snapshot)
  - `invalid_evaluations/main_method_cross_model/`
  - `invalid_evaluations/supporting_method_self_eval/`

---

## How to verify any claim (3 steps)
1) Locate the relevant row in `summary_tables/summary.csv` (or a `*_by_*.csv` slice).  
2) Open the corresponding evaluation bundle JSON under `valid_evaluations/.../`.  
3) Trace back to the raw generation PDF under `01_raw_model_outputs/` if needed.

---

## What to read next
- Interpretation & failure modes: `04_results/03_results_analysis.md`  
- Final takeaways & claim boundary: `05_summary_and_outlook/README.md`  
- Why Prompt B is used for main reporting: `06_methodological_addenda_and_controls/README.md`
