#!/usr/bin/env python3
"""
Script 03: Build retrieval indices (FAISS + BM25) from the clean chunked corpus.

Reads chunks from data/processed/<dataset>/chunks.jsonl and builds:
- FAISS dense index → data/indices/<dataset>/faiss.index
- BM25 sparse index → data/indices/<dataset>/bm25.pkl
- ID mapping → data/indices/<dataset>/faiss_id_map.json

Usage:
    python scripts/03_build_indices.py --config configs/default.yaml
"""

from __future__ import annotations

import argparse


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Build retrieval indices")
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
    # 2. Instantiate Embedder and IndexBuilder
    # 3. Read chunks from data/processed/
    # 4. Build FAISS and BM25 indices
    # 5. Save to data/indices/

    print(f"[03] Build indices — config: {args.config}")
    print("     Not yet implemented.")


if __name__ == "__main__":
    main()
