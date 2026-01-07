#!/usr/bin/env bash
set -euo pipefail

# Recompute summary tables from existing judged JSON files and diff against the committed summary.
# (Aggregation-only; does NOT re-judge model outputs.)

DATE_STR=$(date +%F)
RUN_DIR="runs/${DATE_STR}_NA_cross_model_eval_v2"

MAIN_DIR="04_results/02_cross_model_evaluation/valid_evaluations/main_method_cross_model"
SUPPORT_DIR="04_results/02_cross_model_evaluation/valid_evaluations/supporting_method_self_eval"
ORIG_DIR="04_results/02_cross_model_evaluation/valid_evaluations/summary_tables"
OUT_DIR="${RUN_DIR}/outputs/summary_tables"

mkdir -p "${RUN_DIR}/config" "${RUN_DIR}/inputs" "${RUN_DIR}/outputs" "${RUN_DIR}/logs" "${OUT_DIR}"

# Run recompute
python 03_evaluation_rules/compute_scores.py \
  --main_dir "${MAIN_DIR}" \
  --support_dir "${SUPPORT_DIR}" \
  --out_dir "${OUT_DIR}" \
  --strict \
  > "${RUN_DIR}/logs/compute_scores.stdout.txt" \
  2> "${RUN_DIR}/logs/compute_scores.stderr.txt"

# Diff
REPORT="${RUN_DIR}/outputs/diff_report.md"
{
  echo "# Recompute Summary Diff Report"
  echo
  echo "- date: ${DATE_STR}"
  echo "- script: 03_evaluation_rules/compute_scores.py (v2.1)"
  echo "- strict: true"
  echo
  echo "## File-level diff (orig vs recomputed)"
  echo
  for f in $(ls "${ORIG_DIR}"/*.csv | xargs -n1 basename | sort); do
    if diff -u "${ORIG_DIR}/${f}" "${OUT_DIR}/${f}" >/dev/null; then
      echo "- ✅ ${f}: identical"
    else
      echo "- ❌ ${f}: DIFF"
      diff -u "${ORIG_DIR}/${f}" "${OUT_DIR}/${f}" | head -n 60
      echo
    fi
  done
} > "${REPORT}"

# Hashes (auditability)
sha256sum "${MAIN_DIR}"/*.json "${SUPPORT_DIR}"/*.json | sort -k2 > "${RUN_DIR}/inputs/sha256_inputs.txt"
sha256sum "${OUT_DIR}"/*.csv | sort -k2 > "${RUN_DIR}/outputs/sha256_outputs.txt"
sha256sum "${ORIG_DIR}"/*.csv | sort -k2 > "${RUN_DIR}/outputs/sha256_original_summary_tables.txt"

echo "OK. Wrote: ${RUN_DIR}"
