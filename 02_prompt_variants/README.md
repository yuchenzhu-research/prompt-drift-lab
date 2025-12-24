# 02_prompt_variants

This directory contains the prompt texts (`*.txt`) actually used in this project.
The prompt inventory, variable hierarchy, and statistical inclusion rules are
centrally defined in `PROMPT_MANIFEST.md`.

- `PROMPT_MANIFEST.md`: prompt inventory, variable hierarchy (Family / Variant),
  and statistical scope for the primary experiment
- `*.txt`: prompt bodies used in experiments (kept free of explanatory comments
  to preserve clean diffs)

---

## Directory Contents

- `PROMPT_MANIFEST.md`: prompt inventory and experimental inclusion rules
- `00_baseline_prompt_A_ZH.txt`: Prompt Family A (exploratory pilot)
- `01_structured_prompt_B_ZH.txt`: Prompt Family B (protocolized three-section format; primary experimental anchor)
- `02_conflict_prompt_ZH.txt`: B-variant (`conflict`)
- `03_long_prompt_ZH.txt`: B-variant (`long`)
- `04_weak_prompt_ZH.txt`: B-variant (`weak`)

---

## How to Use (Aligned with the Experimental Pipeline)

1. **Primary experiments**: Use Prompt Family B and perform controlled comparisons
   across `baseline / conflict / long / weak`.
2. **Pilot exploration (optional)**: Prompt Family A is used only to supplement
   observed phenomena and mechanism hypotheses; unless it forms a fully matched
   comparison under the same questions and protocol, it is excluded from
   quantitative summaries.
3. **Run logging**: Record `prompt_family`, `prompt_variant`, `prompt_file`,
   and `prompt_hash` in configs or sample metadata to ensure reproducibility and
   auditability.

---

## Relationship to Other Directories

- `01_experiment_design/`: experimental goals, variable definitions, and workflow
- `02_prompt_variants/` (this directory): prompt bodies and prompt manifest
- `03_evaluation_rules/`: validity criteria and scoring rubrics
- `04_results/`: aggregated statistics and attribution analysis
  (primary conclusions are anchored on Prompt Family B)

---

## Maintenance Principles

- Keep prompt bodies (`*.txt`) clean and diff-friendly; place all explanatory and
  analytical content in `PROMPT_MANIFEST.md`.
- When adding new prompt variants, prefer single-factor minimal diffs to avoid
  confounded attribution.
