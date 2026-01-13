# Prompt Drift Lab

## Overview

This repository documents an experimental study on **prompt drift** in large language models. The focus is on how small, localized changes in prompt structure, wording, or formatting can lead to systematic failures in instruction following, output schema compliance, and semantic alignment.

The work emphasizes empirical observation over optimization. Rather than proposing improved prompting techniques, it examines where and how existing prompts degrade under realistic variations.

---

## Motivation

Prompt-based interactions are often treated as static artifacts. In practice, prompts evolve: constraints are reordered, clarifications are appended, formatting is adjusted, and language drifts over time.

This project treats prompt drift as a first-class experimental variable and asks:

> When prompts change in minor, seemingly innocuous ways, which behaviors fail and which remain stable?

---

## Experimental Framing

The experimental design separates exploration from measurement:

- **Exploratory prompts** are used to expose a broad surface of potential failure modes.
- **Protocolized prompts** are used to measure those failures under fixed and auditable conditions.

This separation allows failure behavior to be observed without allowing uncontrolled variance to affect quantitative results.

---

## Failure Modes Studied

The analysis focuses on recurring categories of failure:

1. Instruction-following degradation
2. Output format and schema violations
3. Semantic drift and content deviation
4. Instability across repeated or near-identical runs

Failures are evaluated across multiple prompt variants and multiple model families under a fixed evaluation protocol.

---

## Repository Structure

This repository is organized as a complete, auditable artifact:

- **Experiment design**: task definitions, schemas, and protocols
- **Prompt variants**: baseline, structured, conflicting, long, and weak prompts
- **Evaluation rules**: judge contracts, rubrics, and scoring logic
- **Results**: fixed model outputs, judged records, and summary tables
- **Methodological addenda**: controls and interpretation boundaries

All reported quantitative results are derived exclusively from the artifacts stored in this repository.

---

## Reproducibility Scope

Two layers of reproducibility are distinguished:

- **Model generation** (prompt → output), which is inherently non-deterministic under web-based interfaces
- **Evaluation and analysis** (output → scores → tables), which is fully inspectable and logically reproducible

Accordingly, this repository supports analysis-level reproducibility rather than end-to-end re-execution of model inference.

---

## Scope and Limitations

This work does not claim comprehensive coverage of prompt robustness or model behavior. It is intentionally narrow in scale and conservative in its claims.

Its value lies in making failure behavior explicit, traceable, and auditable under controlled variations, rather than in maximizing performance or breadth.