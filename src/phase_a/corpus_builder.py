"""
src.phase_a.corpus_builder — Orchestrate the full Phase A pipeline.

This is the top-level orchestrator for threat simulation. It coordinates:

1. Load the clean chunked corpus and target queries.
2. Instantiate the configured poisoning strategy.
3. Call the strategy to generate poisoned chunks.
4. Call the injector to add poisoned chunks to the retrieval indices.
5. Call the ground-truth writer to persist labels.

Outputs:
- Updated retrieval indices (FAISS + BM25) containing clean + poisoned chunks.
- ground_truth.jsonl in the experiment directory.

Usage (planned):
    builder = CorpusBuilder(config)
    builder.run(experiment_dir="experiments/2026-09-28_exp1/")
"""

from __future__ import annotations

# TODO: Implement CorpusBuilder with:
#
# class CorpusBuilder:
#     def __init__(self, config) -> None: ...
#     def run(self, experiment_dir: Path) -> None: ...
#     def _load_strategy(self, strategy_name: str) -> BasePoisonStrategy: ...
#     def _select_target_queries(self, queries: list[Query]) -> list[Query]: ...
