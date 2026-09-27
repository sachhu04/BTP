"""
src.retrieval.index_builder — Build and persist FAISS and BM25 indices.

Responsibilities:
- Accept an iterable of Chunk objects (from the chunker).
- Build a FAISS index from chunk embeddings (via the Embedder).
- Build a BM25 index from chunk texts.
- Persist both indices to disk under data/indices/<dataset_name>/.
- Maintain a chunk_id ↔ FAISS internal ID mapping (faiss_id_map.json).

Called during:
- Initial clean corpus setup (script 03).
- After Phase A poison injection (to rebuild indices with injected chunks).

Usage (planned):
    builder = IndexBuilder(config, embedder)
    builder.build_from_chunks(chunks, output_dir)
"""

from __future__ import annotations

# TODO: Implement IndexBuilder with:
#
# class IndexBuilder:
#     def __init__(self, config, embedder: Embedder) -> None: ...
#     def build_from_chunks(self, chunks: Iterable[Chunk], output_dir: Path) -> None: ...
#     def _build_faiss_index(self, chunks: list[Chunk], output_dir: Path) -> None: ...
#     def _build_bm25_index(self, chunks: list[Chunk], output_dir: Path) -> None: ...
