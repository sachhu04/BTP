#!/usr/bin/env python3
"""
Script 02: Preprocess (chunk) the corpus.

Reads raw documents from data/raw/<dataset>/ and produces chunked
documents in data/processed/<dataset>/chunks.jsonl.

Usage:
    python scripts/02_preprocess_corpus.py --config configs/default.yaml
"""

from __future__ import annotations

import argparse


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Chunk the corpus")
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
    # 1. Load config
    # 2. Instantiate BEIRLoader and Chunker
    # 3. Iterate over corpus documents, chunk each one
    # 4. Write chunks to data/processed/<dataset>/chunks.jsonl

    print(f"[02] Preprocess corpus — config: {args.config}")
    print("     Not yet implemented.")


if __name__ == "__main__":
    main()
