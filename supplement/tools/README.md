# Tools README

## Scope

This directory contains analysis-level tools only. The tools operate exclusively on already-generated model outputs and do not perform or simulate any model inference.

All model outputs analyzed in this project were collected via web-based LLM interfaces. As execution-level reproduction is not feasible under this collection setting, the tools in this directory are designed to support a fully reproducible post-hoc analysis pipeline.

---

## Tooling Overview

The tools provided here perform deterministic, rule-based analysis on fixed model outputs, including:

- Structural and format validation
- Prompt-drift and failure-type detection
- Instruction-following deviation analysis
- Rubric-aligned scoring and aggregation

No tool in this directory introduces stochastic behavior or relies on external services.

---

## Functional Boundaries

### What These Tools Do

- Analyze raw model outputs for predefined failure categories
- Validate schema and formatting constraints
- Detect instruction-following and semantic drift patterns
- Map detected failures to rubric-aligned scores
- Emit structured and auditable JSON artifacts

### What These Tools Do Not Do

- Execute or invoke any LLM
- Reproduce original model generations
- Perform model benchmarking or ranking
- Claim execution-level reproducibility
- Introduce semantic interpretation beyond declared rules

---

## File Structure

```
tools/
├── drift_analyzer.py
├── schema_checker.py
├── rubric_scorer.py
├── input_example.jsonl
├── output_example.json
└── LICENSE
```

---

## Input Contract

All tools consume JSONL-formatted inputs. Each line corresponds to a single model output record and must include:

- `sample_id`: unique identifier
- `prompt_id`: base prompt identifier
- `prompt_variant`: prompt variant identifier
- `schema_id`: expected output schema identifier
- `raw_output`: unmodified model output text

A concrete example is provided in `input_example.jsonl`.

---

## Output Contract

The analysis pipeline produces structured JSON outputs that record:

- Schema validation outcomes
- Detected failure and drift categories
- Rubric-aligned scores
- Intermediate diagnostic signals

An end-to-end example is provided in `output_example.json`.

---

## Reproducibility

Given identical input files and configuration, all outputs produced by these tools are reproducible.

The tools are deterministic and do not depend on model randomness, sampling parameters, or external APIs.

---

## Intended Use

These tools support prompt-drift analysis, failure taxonomy validation, and methodological transparency in workshop-level submissions.

They are not intended for leaderboard benchmarking, comparative performance claims, or deployment evaluation.