"""
src.phase_a.injector — Inject poisoned chunks into the retrieval knowledge base.

Responsibilities:
- Accept a list of PoisonedChunk objects from a poisoning strategy.
- Convert them to Chunk objects and add them to the existing corpus.
- Update the FAISS index (add new embeddings) and BM25 index (add new texts).
- Record the chunk_id of every injected poisoned entry.
- Does NOT modify data/raw/ — only updates the indices and processed data.

The injector is strategy-agnostic: it handles any PoisonedChunk objects
regardless of which strategy produced them.

Usage (planned):
    injector = Injector(config, embedder)
    injected_ids = injector.inject(poisoned_chunks, index_dir)
"""

from __future__ import annotations

# TODO: Implement Injector with:
#
# class Injector:
#     def __init__(self, config, embedder: Embedder) -> None: ...
#     def inject(self, poisoned_chunks: list[PoisonedChunk],
#                index_dir: Path) -> list[str]: ...
