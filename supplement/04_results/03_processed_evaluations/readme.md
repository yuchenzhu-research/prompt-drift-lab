# Processed Evaluations

This directory contains **deterministically processed evaluation artifacts** derived from raw judge outputs.

## Inputs and provenance
- All files in this directory are generated **exclusively** from JSON artifacts in `02_raw_judge_evaluations/`.
- No PDF files or natural language outputs are re-parsed or reinterpreted during processing.

## Contents
- `record_*.json`: per-file evaluation records generated from judge JSON artifacts.
- `summary_tables/`: tabular aggregations (e.g., long-form and grouped CSVs) derived deterministically from records.

## Guarantees
- Processing is script-based and reproducible.
- Each record corresponds to a single evaluated file and is identified by a stable hash.
- No manual editing or selective filtering is performed.

This directory serves as the **authoritative source of aggregated evaluation results**, fully traceable to raw judge outputs.