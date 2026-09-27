"""
src.data.chunker — Document chunking with configurable strategies.

Responsibilities:
- Split documents into chunks of configurable size with configurable overlap.
- Support multiple chunking strategies:
    - "fixed": Fixed token-count windows with overlap.
    - "sentence": Sentence-boundary-aware chunking.
- Assign each chunk a unique chunk_id linked to its parent doc_id.
- Chunk size and overlap are read from the project configuration.

Usage (planned):
    chunker = Chunker(config)
    chunks: list[Chunk] = chunker.chunk_document(document)
    all_chunks: Iterator[Chunk] = chunker.chunk_corpus(corpus_iterator)
"""

from __future__ import annotations

# TODO: Implement Chunker class with the following interface:
#
# class Chunker:
#     def __init__(self, config: ChunkingConfig) -> None: ...
#     def chunk_document(self, doc: Document) -> list[Chunk]: ...
#     def chunk_corpus(self, docs: Iterator[Document]) -> Iterator[Chunk]: ...
