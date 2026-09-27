"""
src.retrieval.embedder — Embedding model wrapper.

Responsibilities:
- Load a Sentence Transformers model by name.
- Encode single texts and batches of texts into dense vectors.
- Support configurable batch size, device (CPU/CUDA), and normalization.
- Provide optional embedding caching to avoid redundant encoding.

Used by:
- DenseRetriever (for encoding queries at retrieval time)
- IndexBuilder (for encoding corpus chunks at index-build time)
- Phase A strategies (for encoding poisoned chunks)

Usage (planned):
    embedder = Embedder(config)
    vector = embedder.encode("some text")
    vectors = embedder.encode_batch(["text1", "text2", ...])
"""

from __future__ import annotations

# TODO: Implement Embedder class with the following interface:
#
# class Embedder:
#     def __init__(self, config: EmbeddingConfig) -> None: ...
#     def encode(self, text: str) -> np.ndarray: ...
#     def encode_batch(self, texts: list[str]) -> np.ndarray: ...
#     def dimension(self) -> int: ...
