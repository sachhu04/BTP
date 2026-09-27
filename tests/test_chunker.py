"""Tests for src.data.chunker — document chunking."""

from __future__ import annotations

# TODO: Test cases to implement:
#
# - test_chunk_single_document: Chunk a document and verify chunk count, IDs, and text coverage.
# - test_chunk_overlap: Verify that overlap between consecutive chunks is correct.
# - test_chunk_ids_unique: All chunk IDs must be unique across documents.
# - test_chunk_links_to_parent: Each chunk's doc_id matches its parent document.
# - test_empty_document: Chunking an empty document returns an empty list.
# - test_short_document: Document shorter than chunk_size returns a single chunk.
# - test_configurable_chunk_size: Different chunk sizes produce different chunk counts.
