#!/usr/bin/env python3
"""
Script 04: Run Phase A — Threat Simulation.

Generates poisoned chunks using the configured attack strategy, injects
them into the retrieval indices, and writes ground-truth labels.

Outputs:
- Updated indices in data/indices/<dataset>/ (now contain poisoned chunks)
- experiments/<experiment_id>/ground_truth.jsonl

Usage:
    python scripts/04_run_phase_a.py --config configs/default.yaml \
        --poison-config configs/poisoning/targeted_corruption.yaml \
        --experiment-id my_experiment
"""

from __future__ import annotations

import argparse


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Run Phase A: Threat Simulation")
    parser.add_argument(
        "--config", type=str, default="configs/default.yaml",
        help="Path to the master config file",
    )
    parser.add_argument(
        "--poison-config", type=str, required=True,
        help="Path to the poisoning strategy config",
    )
    parser.add_argument(
        "--dataset-config", type=str, default=None,
        help="Path to a dataset-specific config override",
    )
    parser.add_argument(
        "--experiment-id", type=str, default=None,
        help="Experiment identifier (auto-generated if not provided)",
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()

    # TODO: Implementation
    # 1. Load and merge configs
    # 2. Create experiment directory
    # 3. Snapshot config to experiments/<id>/config.yaml
    # 4. Instantiate CorpusBuilder
    # 5. Run Phase A pipeline
    # 6. Print summary (num poisoned, strategy, target queries)

    print(f"[04] Phase A — config: {args.config}, poison: {args.poison_config}")
    print("     Not yet implemented.")


if __name__ == "__main__":
    main()
