#!/usr/bin/env python3
"""
Rubric scorer (analysis-level only) for Prompt Drift Lab.

POSITIONING
-----------
This module maps *detected failures* (schema violations and drift signals)
into **rubric-aligned scores** using transparent, deterministic rules.

It does NOT judge model quality holistically and does NOT perform
model inference. It only scores *observed outputs* based on a fixed rubric.
"""

from typing import Dict, List
import json
import hashlib


# -----------------------------
# Rubric definition (fixed)
# -----------------------------

DEFAULT_RUBRIC = {
    "schema_compliance": {
        "max_score": 2,
        "penalties": {
            "schema_violation": 2,
        },
    },
    "instruction_following": {
        "max_score": 3,
        "penalties": {
            "instruction_deviation": 2,
            "extraneous_content": 1,
        },
    },
    "semantic_fidelity": {
        "max_score": 3,
        "penalties": {
            "semantic_drift": 2,
        },
    },
}


# -----------------------------
# Core scoring logic
# -----------------------------

def score_dimension(
    detected_failures: List[str], dimension_cfg: Dict
) -> Dict:
    """
    Score a single rubric dimension given detected failure types.
    """
    score = dimension_cfg["max_score"]
    applied_penalties = []

    for failure, penalty in dimension_cfg.get("penalties", {}).items():
        if failure in detected_failures:
            score -= penalty
            applied_penalties.append({"failure": failure, "penalty": penalty})

    score = max(score, 0)

    return {
        "score": score,
        "max_score": dimension_cfg["max_score"],
        "penalties": applied_penalties,
    }


def score_output(
    detected_failures: List[str], rubric: Dict = DEFAULT_RUBRIC
) -> Dict:
    """
    Map detected failure types to rubric-aligned scores.
    """
    dimension_scores = {}
    total_score = 0
    total_max = 0

    for dim, cfg in rubric.items():
        dim_result = score_dimension(detected_failures, cfg)
        dimension_scores[dim] = dim_result
        total_score += dim_result["score"]
        total_max += dim_result["max_score"]

    return {
        "dimension_scores": dimension_scores,
        "total_score": total_score,
        "total_max": total_max,
        "normalized_score": round(total_score / total_max, 3)
        if total_max > 0
        else 0.0,
    }


# -----------------------------
# Utility
# -----------------------------

def stable_hash(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


# -----------------------------
# Example usage
# -----------------------------

if __name__ == "__main__":
    # Example detected failures from analysis tools
    failures = ["schema_violation", "semantic_drift"]

    report = {
        "output_hash": stable_hash("example output"),
        "rubric_score": score_output(failures),
    }

    print(json.dumps(report, indent=2))