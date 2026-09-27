"""
src.retrieval.dense — Dense retriever using Sentence Transformers + FAISS.

Responsibilities:
- Load a pre-built FAISS index from disk.
- Encode queries using the Embedder.
- Perform approximate nearest neighbor search via FAISS.
- Return top-k RetrievalResult objects with cosine similarity scores.

Implements the BaseRetriever interface.

Usage (planned):
    retriever = DenseRetriever(config, embedder, index_path)
    results = retriever.retrieve("What is ...", top_k=10)
"""

from __future__ import annotations

# TODO: Implement DenseRetriever(BaseRetriever) with:
#
# class DenseRetriever(BaseRetriever):
#     def __init__(self, config, embedder: Embedder, index_dir: Path) -> None: ...
#     def retrieve(self, query: str, top_k: int) -> list[RetrievalResult]: ...
#     def index_size(self) -> int: ...
