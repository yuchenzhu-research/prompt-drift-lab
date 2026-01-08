# supplement_min (v3)

This directory contains the **official, frozen minimal supplement bundle (v3)** for *Prompt Drift Lab*.

## What “minimal” means (important)
“Minimal” **does NOT mean** skipping early-numbered folders.  
It means excluding *paper source trees and historical drafts*, while **retaining all materials necessary for auditability and interpretation**.

## Directory map (authoritative)

- `01_experiment_design/` — experiment assumptions, task construction logic, and design rationale  
- `02_prompt_variants/` — prompt manifests (EN/ZH), frozen and hash-locked  
- `03_evaluation_rules/` — evaluation protocol + judge contract (EN/ZH), frozen and hash-locked  
- `04_results/` — released result tables and figures referenced by the paper  
- `05_summary_and_outlook/` — interpretation notes and high-level takeaways  
- `06_methodological_addenda_and_controls/` — ablations, controls, and robustness notes  
- `07_deep_research/` — background research PDFs and extended context  
- `paper_assets/` — figures/tables used by the paper (no source TeX)  
- `tools/` — helper scripts (non-canonical)

## Canonical vs non-canonical
Only a **subset of files** are hash-locked as the *evaluation contract*.  
See `VERSION_MAP.md` for the authoritative list and SHA256 values.

## Integrity check
From this directory:

```bash
sha256sum -c VERSION_MAP.sha256
```

Expected: every line returns `OK`.
