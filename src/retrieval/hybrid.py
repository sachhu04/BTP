"""
src.retrieval.hybrid — Hybrid retriever merging dense and BM25 results.

Responsibilities:
- Accept two BaseRetriever instances (e.g., dense + BM25).
- Retrieve top-k from each retriever independently.
- Merge results using configurable fusion strategies:
    - Reciprocal Rank Fusion (RRF)
    - Linear score combination
- Return a unified top-k list.

This module is optional — the disagreement detector in Phase B works
with the *separate* result lists from dense and BM25, not the merged list.
The hybrid retriever exists for experiments comparing hybrid retrieval
as a standalone defense.

Implements the BaseRetriever interface.

Usage (planned):
    hybrid = HybridRetriever(dense_retriever, bm25_retriever, fusion="rrf")
    results = hybrid.retrieve("What is ...", top_k=10)
"""

from __future__ import annotations

# TODO: Implement HybridRetriever(BaseRetriever) with:
#
# class HybridRetriever(BaseRetriever):
#     def __init__(self, retriever_a: BaseRetriever, retriever_b: BaseRetriever,
#                  fusion: str = "rrf") -> None: ...
#     def retrieve(self, query: str, top_k: int) -> list[RetrievalResult]: ...
#     def index_size(self) -> int: ...
