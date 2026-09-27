"""
src.evaluation.retrieval_metrics — Retrieval quality metrics.

Computes standard information retrieval metrics.

Metrics:
- Recall@k: Fraction of relevant documents in the top-k results.
- Precision@k: Fraction of top-k results that are relevant.
- MRR (Mean Reciprocal Rank): Average of 1/rank of the first relevant result.
- RSR (Retrieval Success Rate): Fraction of queries where at least one
  poisoned document appears in top-k (attack metric).

Usage (planned):
    metrics = compute_retrieval_metrics(qrels, retrieval_results, k=10)
"""

from __future__ import annotations

# TODO: Implement:
#
# def compute_retrieval_metrics(
#     qrels: list[QRel],
#     results: dict[str, list[RetrievalResult]],
#     k: int = 10,
# ) -> dict[str, float]: ...
#
# def recall_at_k(relevant: set[str], retrieved: list[str], k: int) -> float: ...
# def precision_at_k(relevant: set[str], retrieved: list[str], k: int) -> float: ...
# def mrr(relevant: set[str], retrieved: list[str]) -> float: ...
