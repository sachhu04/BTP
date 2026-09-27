"""
src.phase_b.pipeline — End-to-end Phase B detection pipeline orchestrator.

Orchestrates the full detection pipeline for each user query:

1. Dense retrieval → top-k candidates
2. BM25 retrieval → top-k candidates
3. Feature extraction (disagreement, embedding stats, text stats)
4. Suspicion scoring
5. Threshold-based detection (retain / flag)
6. Chunk filtering (exclude flagged from LLM context)
7. LLM generation (from retained context)
8. Logging detection decisions to predictions.jsonl

This module ties together all Phase B components and src.rag.

Usage (planned):
    pipeline = DetectionPipeline(config)
    result = pipeline.run_query(query, experiment_dir)
    results = pipeline.run_all_queries(queries, experiment_dir)
"""

from __future__ import annotations

# TODO: Implement DetectionPipeline with:
#
# class DetectionPipeline:
#     def __init__(self, config, dense_retriever, bm25_retriever,
#                  feature_extractors, scorer, detector, chunk_filter,
#                  generator) -> None: ...
#     def run_query(self, query: Query) -> PipelineResult: ...
#     def run_all_queries(self, queries: list[Query],
#                         experiment_dir: Path) -> list[PipelineResult]: ...
#     def _log_predictions(self, decisions, output_path: Path) -> None: ...
