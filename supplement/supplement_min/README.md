# Supplement (Minimal)

This directory contains the **minimal supplement bundle** for *Prompt Drift Lab*.

The goal of this supplement is to provide **sufficient materials for auditability and interpretation**, while excluding paper source trees and historical drafts. All artifacts included here correspond to the experiments reported in the paper.

## What “minimal” means
“Minimal” does **not** mean omitting early-numbered folders or evaluation components. It means:
- excluding paper source files (e.g., LaTeX trees)
- excluding internal version histories and editorial artifacts
- retaining all materials necessary to understand, verify, and interpret the reported results

## Directory overview

- `01_experiment_design/` — experiment assumptions, task construction logic, and design rationale
- `02_prompt_variants/` — prompt manifests (EN/ZH)
- `03_evaluation_rules/` — evaluation protocol and judge contract (EN/ZH)
- `04_results/` — released result tables and figures referenced by the paper
- `05_summary_and_outlook/` — interpretation notes and high-level takeaways
- `06_methodological_addenda_and_controls/` — ablations, controls, and robustness notes
- `07_deep_research/` — background research materials and extended context
- `paper_assets/` — figures and tables used by the paper (no paper source files)
- `tools/` — helper scripts (non-canonical; provided for reference only)

## Notes on integrity and scope
- This supplement is intended for **reading and inspection**, not for rebuilding the paper source.
- Result files, evaluation outputs, and supporting materials are included as-is to preserve their original experimental context.
- Helper scripts are provided for transparency but are not part of the evaluation contract.

All materials in this directory are aligned with the experiments described in the paper.