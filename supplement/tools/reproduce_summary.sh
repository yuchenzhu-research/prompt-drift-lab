#!/usr/bin/env bash
set -euo pipefail

# ============================================================
# reproduce_summary.sh
# ------------------------------------------------------------
# P0 CANONICAL BEHAVIOR:
#   - This script is a *thin wrapper*.
#   - It MUST NOT implement any scoring logic.
#   - It calls the canonical aggregator located at:
#       03_evaluation_rules/compute_scores.py
#
# Usage:
#   bash tools/reproduce_summary.sh <RUN_DIR>
#
# Example:
#   bash tools/reproduce_summary.sh runs/2026-01-08_gpt4_promptsetA
#
# Expected directory layout:
#   <RUN_DIR>/
#     ├── judged_scores/
#     └── summary.csv   (output)
# ============================================================

if [ "$#" -ne 1 ]; then
  echo "Usage: $0 <RUN_DIR>"
  exit 1
fi

RUN_DIR="$1"
JUDGED_DIR="${RUN_DIR}/judged_scores"
OUT_FILE="${RUN_DIR}/summary.csv"

# --- Sanity checks -----------------------------------------------------------
if [ ! -d "$RUN_DIR" ]; then
  echo "ERROR: RUN_DIR not found: $RUN_DIR"
  exit 1
fi

if [ ! -d "$JUDGED_DIR" ]; then
  echo "ERROR: judged_scores directory not found: $JUDGED_DIR"
  exit 1
fi

if [ ! -f "03_evaluation_rules/compute_scores.py" ]; then
  echo "ERROR: canonical aggregator not found: 03_evaluation_rules/compute_scores.py"
  exit 1
fi

# --- Call canonical aggregator -----------------------------------------------
python3 03_evaluation_rules/compute_scores.py \
  --input "$JUDGED_DIR" \
  --output "$OUT_FILE"

echo "OK: summary written to $OUT_FILE"