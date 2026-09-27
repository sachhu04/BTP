"""
src.evaluation.latency_metrics — Latency measurement and reporting.

Computes per-query latency breakdown and aggregate statistics.

Metrics:
- retrieval_latency_ms: Time for dense + BM25 retrieval.
- feature_extraction_latency_ms: Time for feature computation.
- scoring_latency_ms: Time for suspicion scoring.
- generation_latency_ms: Time for LLM generation.
- total_latency_ms: End-to-end query latency.
- detection_overhead_ms: Total latency − (retrieval + generation).
- Aggregate stats: mean, median, p95, p99 across all queries.

Usage (planned):
    stats = compute_latency_stats(timing_records)
"""

from __future__ import annotations

# TODO: Implement:
#
# def compute_latency_stats(
#     timing_records: list[dict[str, float]],
# ) -> dict[str, float]: ...
