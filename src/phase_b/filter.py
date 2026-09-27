"""
src.phase_b.filter — Partition chunks into retained and flagged sets.

Responsibilities:
- Accept a list of DetectionDecision objects from the Detector.
- Partition candidate chunks into:
    - retained: Chunks that will be sent to the LLM as context.
    - flagged: Chunks excluded from the LLM context (suspected poison).
- This is a simple partitioning step, explicitly separated for clarity
  and testability.

Usage (planned):
    chunk_filter = ChunkFilter()
    retained, flagged = chunk_filter.apply(decisions, candidate_chunks)
"""

from __future__ import annotations

# TODO: Implement ChunkFilter with:
#
# class ChunkFilter:
#     def apply(self, decisions: list[DetectionDecision],
#               candidates: list[Chunk]) -> tuple[list[Chunk], list[Chunk]]: ...
