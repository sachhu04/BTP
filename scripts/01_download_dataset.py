#!/usr/bin/env python3
"""
Script 01: Download a BEIR dataset.

Downloads and caches a BEIR-format dataset to data/raw/<dataset_name>/.

Usage:
    python scripts/01_download_dataset.py --config configs/default.yaml
    python scripts/01_download_dataset.py --config configs/default.yaml --dataset-config configs/datasets/scifact.yaml
"""

from __future__ import annotations

import argparse


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Download a BEIR dataset")
    parser.add_argument(
        "--config", type=str, default="configs/default.yaml",
        help="Path to the master config file",
    )
    parser.add_argument(
        "--dataset-config", type=str, default=None,
        help="Path to a dataset-specific config override",
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()

    # TODO: Implementation
    # 1. Load config (merge default + dataset override)
    # 2. Instantiate BEIRLoader
    # 3. Call loader.download()
    # 4. Print summary (dataset name, corpus size, num queries)

    print(f"[01] Download dataset — config: {args.config}")
    print("     Not yet implemented.")


if __name__ == "__main__":
    main()
