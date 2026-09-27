"""
src.retrieval — Retrieval module (shared by Phase A and Phase B).

Provides modular retriever implementations with a common abstract interface:
- DenseRetriever: Sentence Transformers + FAISS
- BM25Retriever: rank_bm25
- HybridRetriever: Merges results from any two retrievers

Also provides:
- Embedder: Embedding model wrapper
- IndexBuilder: Build and persist FAISS / BM25 indices
"""
