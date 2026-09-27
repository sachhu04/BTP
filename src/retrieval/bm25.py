"""
src.retrieval.bm25 — BM25 sparse retriever using rank_bm25.

Responsibilities:
- Load a pre-built (pickled) BM25 index from disk.
- Tokenize queries using the configured tokenizer.
- Perform BM25 scoring and return top-k results.
- Return top-k RetrievalResult objects with BM25 scores.

Implements the BaseRetriever interface.

Usage (planned):
    retriever = BM25Retriever(config, index_path)
    results = retriever.retrieve("What is ...", top_k=10)
"""

from __future__ import annotations

# TODO: Implement BM25Retriever(BaseRetriever) with:
#
# class BM25Retriever(BaseRetriever):
#     def __init__(self, config, index_dir: Path) -> None: ...
#     def retrieve(self, query: str, top_k: int) -> list[RetrievalResult]: ...
#     def index_size(self) -> int: ...
