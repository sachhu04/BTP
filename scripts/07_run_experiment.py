#!/usr/bin/env python3
"""
Script 07: Run a full end-to-end experiment (sweep).

Reads an experiment config that defines a parameter sweep, and for each
combination runs Phase A → Phase B → Evaluation.

Each parameter combination gets its own experiment subdirectory.

Usage:
    python scripts/07_run_experiment.py --config configs/experiments/exp_poison_rate_sweep.yaml
"""

from __future__ import annotations

import argparse


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Run an end-to-end experiment sweep")
    parser.add_argument(
        "--config", type=str, required=True,
        help="Path to the experiment sweep config",
    )
    parser.add_argument(
        "--dry-run", action="store_true",
        help="Print the experiment plan without executing",
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()

    # TODO: Implementation
    # 1. Load experiment config
    # 2. Generate parameter combinations from the sweep definition
    # 3. For each combination:
    #    a. Create experiment directory
    #    b. Snapshot merged config
    #    c. Run Phase A (04_run_phase_a logic)
    #    d. Run Phase B (05_run_phase_b logic)
    #    e. Run evaluation (06_evaluate logic)
    # 4. Print summary table of all results

    print(f"[07] Experiment sweep — config: {args.config}")
    if args.dry_run:
        print("     [DRY RUN] Would execute the above experiments.")
    print("     Not yet implemented.")


if __name__ == "__main__":
    main()
