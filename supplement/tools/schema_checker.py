#!/usr/bin/env python3
"""
Schema checker (analysis-level only) for Prompt Drift Lab.

SCOPE
-----
This module validates whether model outputs conform to a
*declared output schema* using deterministic rules.

It does NOT execute any model inference and does NOT attempt
semantic understanding beyond explicit structural constraints.
"""

from typing import Dict, List, Any
import json
import hashlib


# -----------------------------
# Schema definition
# -----------------------------

DEFAULT_SCHEMA = {
    "required_sections": [],        # e.g., ["## Answer", "## Reasoning"]
    "forbidden_sections": [],       # e.g., ["## Analysis"]
    "ordered_sections": [],         # e.g., ["## Step 1", "## Step 2"]
    "max_sections": None,            # e.g., 3
    "allow_extra_text": True,        # strict mode if False
}


# -----------------------------
# Core validation functions
# -----------------------------

def check_required_sections(text: str, required: List[str]) -> Dict:
    missing = [s for s in required if s not in text]
    return {
        "rule": "required_sections",
        "missing": missing,
        "triggered": len(missing) > 0,
    }


def check_forbidden_sections(text: str, forbidden: List[str]) -> Dict:
    present = [s for s in forbidden if s in text]
    return {
        "rule": "forbidden_sections",
        "present": present,
        "triggered": len(present) > 0,
    }


def check_section_order(text: str, ordered: List[str]) -> Dict:
    positions = []
    for s in ordered:
        idx = text.find(s)
        positions.append(idx)

    out_of_order = False
    if all(p >= 0 for p in positions):
        out_of_order = positions != sorted(positions)

    return {
        "rule": "ordered_sections",
        "positions": dict(zip(ordered, positions)),
        "triggered": out_of_order,
    }


def check_max_sections(text: str, max_sections: int) -> Dict:
    section_count = text.count("## ")
    return {
        "rule": "max_sections",
        "count": section_count,
        "max_allowed": max_sections,
        "triggered": section_count > max_sections,
    }


def check_extra_text(text: str, schema: Dict[str, Any]) -> Dict:
    if schema.get("allow_extra_text", True):
        return {
            "rule": "extra_text",
            "triggered": False,
        }

    allowed_markers = schema.get("required_sections", []) + schema.get(
        "ordered_sections", []
    )

    remaining = text
    for m in allowed_markers:
        remaining = remaining.replace(m, "")

    has_extra = len(remaining.strip()) > 0

    return {
        "rule": "extra_text",
        "triggered": has_extra,
    }


# -----------------------------
# Aggregator
# -----------------------------

def validate_schema(text: str, schema: Dict[str, Any]) -> Dict:
    results = []

    results.append(
        check_required_sections(text, schema.get("required_sections", []))
    )
    results.append(
        check_forbidden_sections(text, schema.get("forbidden_sections", []))
    )

    if schema.get("ordered_sections"):
        results.append(
            check_section_order(text, schema.get("ordered_sections", []))
        )

    if schema.get("max_sections") is not None:
        results.append(
            check_max_sections(text, schema.get("max_sections"))
        )

    results.append(check_extra_text(text, schema))

    triggered = [r for r in results if r.get("triggered")]

    return {
        "schema_valid": len(triggered) == 0,
        "violations": triggered,
        "details": results,
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
    example_text = "## Answer\n42\n## Reasoning\nBecause it is."  # mock output

    schema = {
        "required_sections": ["## Answer", "## Reasoning"],
        "forbidden_sections": ["## Analysis"],
        "ordered_sections": ["## Answer", "## Reasoning"],
        "max_sections": 2,
        "allow_extra_text": True,
    }

    report = {
        "output_hash": stable_hash(example_text),
        "schema_check": validate_schema(example_text, schema),
    }

    print(json.dumps(report, indent=2))