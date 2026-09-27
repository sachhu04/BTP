#!/usr/bin/env python3
"""
Script 06: Evaluate an experiment run.

Loads ground_truth.jsonl and predictions.jsonl from an experiment directory,
computes all metrics, and writes metrics.json.

Usage:
    python scripts/06_evaluate.py --experiment-dir experiments/my_experiment
"""

from __future__ import annotations

import argparse


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Evaluate an experiment")
    parser.add_argument(
        "--experiment-dir", type=str, required=True,
        help="Path to the experiment directory",
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()

    # TODO: Implementation
    # 1. Instantiate Evaluator
    # 2. Call evaluator.evaluate(experiment_dir)
    # 3. Print summary metrics

    print(f"[06] Evaluate — experiment-dir: {args.experiment_dir}")
    print("     Not yet implemented.")


if __name__ == "__main__":
    main()
