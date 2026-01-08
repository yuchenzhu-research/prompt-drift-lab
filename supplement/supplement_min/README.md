# Supplement (Minimal)

This directory contains the **minimal supplement bundle** for *Prompt Drift Lab*.

The goal of this supplement is to provide **sufficient materials for auditability and interpretation**, while excluding paper source trees and historical drafts. All artifacts included here correspond to the experiments reported in the paper.

---

## What “minimal” means
“Minimal” does **not** mean omitting early-numbered folders or evaluation components. It means:
- excluding paper source files (e.g., LaTeX trees)
- excluding internal version histories and editorial artifacts
- retaining all materials necessary to understand, verify, and interpret the reported results

---

## Directory overview

- `01_experiment_design/` — experiment assumptions, task construction logic, and design rationale
- `02_prompt_variants/` — prompt manifests (EN/ZH)
- `03_evaluation_rules/` — evaluation protocol and judge contract (EN/ZH)
- `04_results/` — released result tables and figures referenced by the paper
- `05_summary_and_outlook/` — interpretation notes and high-level takeaways
- `06_methodological_addenda_and_controls/` — ablations, controls, and robustness notes
- `paper_assets/` — figures and tables used by the paper (no paper source files)
- `tools/` — helper scripts for aggregation, inspection, and consistency checking

---

## Notes on integrity and scope

- This supplement is intended for **reading and inspection**, not for rebuilding the paper source.
- Result files, evaluation outputs, and supporting materials are included as-is to preserve their original experimental context.
- Helper scripts are provided for transparency and auditability, but are **not** part of the evaluation contract.

All materials in this directory are aligned with the experiments described in the paper.

---

## 📌 Reproducibility Note: Summary Re-computation

> **Important:**  
> The script `tools/reproduce_summary.sh` is designed for **aggregation and consistency checking** over the **committed summary tables**.  
> It does **not** re-run judgment or re-compute summaries directly from raw JSON evaluation outputs.
>
> Specifically, the script:
> - Aggregates and reformats existing CSV files under `04_results/.../summary_tables/`
> - Generates a fresh `runs/YYYY-MM-DD_*/` directory for auditability
> - Produces a diff report to verify consistency against the committed results
>
> This design choice ensures deterministic reproduction and avoids re-running model judgments or human evaluation steps, which are outside the scope of this artifact.
>
> In other words, an empty `outputs/summary_tables/` directory inside a run indicates **no inconsistency detected**, rather than a failed reproduction.
