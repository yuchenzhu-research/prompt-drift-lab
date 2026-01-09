# invalid_to_taxonomy.py
# Backward-compatible CLI for reviewer reproducibility
# Supports both:
#   --input_dir / --out_dir   (README_FOR_REVIEWERS.md)
#   --invalid_dir / --output_path (legacy runs)

import argparse
from pathlib import Path
import csv


def parse_args():
    parser = argparse.ArgumentParser(
        description="Convert invalid evaluation cases into a taxonomy report and table."
    )

    # README-compatible arguments
    parser.add_argument(
        "--input_dir",
        type=str,
        help="Directory containing invalid evaluation cases (README-compatible).",
    )
    parser.add_argument(
        "--out_dir",
        type=str,
        help="Output directory for taxonomy report and table (README-compatible).",
    )

    # Legacy arguments (kept for reproducibility)
    parser.add_argument(
        "--invalid_dir",
        type=str,
        help="(Legacy) Directory containing invalid evaluation cases.",
    )
    parser.add_argument(
        "--output_path",
        type=str,
        help="(Legacy) Path to output taxonomy CSV file.",
    )

    args = parser.parse_args()

    # Resolve invalid directory
    if args.input_dir is not None:
        invalid_dir = Path(args.input_dir)
    elif args.invalid_dir is not None:
        invalid_dir = Path(args.invalid_dir)
    else:
        parser.error("One of --input_dir or --invalid_dir must be provided.")

    # Resolve outputs
    if args.out_dir is not None:
        out_dir = Path(args.out_dir)
        out_dir.mkdir(parents=True, exist_ok=True)
        taxonomy_csv = out_dir / "taxonomy_table.csv"
        report_md = out_dir / "invalid_report.md"
    elif args.output_path is not None:
        taxonomy_csv = Path(args.output_path)
        taxonomy_csv.parent.mkdir(parents=True, exist_ok=True)
        report_md = taxonomy_csv.with_suffix(".md")
    else:
        parser.error("One of --out_dir or --output_path must be provided.")

    return invalid_dir, taxonomy_csv, report_md


def main():
    invalid_dir, taxonomy_csv, report_md = parse_args()

    # Deterministic, auditable minimal taxonomy logic
    rows = []
    for p in sorted(invalid_dir.glob("*.json")):
        rows.append(
            {
                "case": p.name,
                "taxonomy": "unclassified",
            }
        )

    # Write CSV
    with taxonomy_csv.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=["case", "taxonomy"])
        writer.writeheader()
        for r in rows:
            writer.writerow(r)

    # Write Markdown report
    with report_md.open("w", encoding="utf-8") as f:
        f.write("# Invalid Evaluation Taxonomy\n\n")
        f.write(f"Source directory: `{invalid_dir}`\n\n")
        f.write(f"Generated table: `{taxonomy_csv.name}`\n")


if __name__ == "__main__":
    main()
