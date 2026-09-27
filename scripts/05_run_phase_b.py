#!/usr/bin/env python3
"""
Script 05: Run Phase B — Detection Pipeline.

For each query, runs the full detection pipeline:
query → dual retrieval → feature extraction → scoring → detection → filtering → generation.

Outputs:
- experiments/<experiment_id>/predictions.jsonl

Usage:
    python scripts/05_run_phase_b.py --config configs/default.yaml \
        --experiment-dir experiments/my_experiment
"""

from __future__ import annotations

import argparse


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Run Phase B: Detection Pipeline")
    parser.add_argument(
        "--config", type=str, default="configs/default.yaml",
        help="Path to the master config file",
    )
    parser.add_argument(
        "--experiment-dir", type=str, required=True,
        help="Path to the experiment directory (must contain config.yaml from Phase A)",
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()

    # TODO: Implementation
    # 1. Load config from experiment directory
    # 2. Instantiate retrievers, feature extractors, scorer, detector, filter, generator
    # 3. Build DetectionPipeline
    # 4. Load queries
    # 5. Run pipeline on all queries
    # 6. Write predictions.jsonl to experiment directory

    print(f"[05] Phase B — experiment-dir: {args.experiment_dir}")
    print("     Not yet implemented.")


if __name__ == "__main__":
    main()
