"""
src.data.schema — Shared data types used across all modules.

Defines the canonical representations for documents, chunks, queries,
relevance judgments, poison labels, and retrieval results. All modules
operate on these types rather than raw dicts/tuples.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any


@dataclass
class Document:
    """A single document from the BEIR corpus."""

    doc_id: str
    title: str
    text: str
    metadata: dict[str, Any] = field(default_factory=dict)


@dataclass
class Chunk:
    """A text chunk derived from a parent document.

    Attributes:
        chunk_id: Unique identifier for this chunk.
        doc_id: Identifier of the parent document.
        text: The chunk text content.
        metadata: Arbitrary metadata (source, position, etc.).
    """

    chunk_id: str
    doc_id: str
    text: str
    metadata: dict[str, Any] = field(default_factory=dict)


@dataclass
class Query:
    """A user query from the BEIR query set."""

    query_id: str
    text: str


@dataclass
class QRel:
    """A query–document relevance judgment.

    Attributes:
        query_id: The query identifier.
        doc_id: The document/chunk identifier.
        relevance: Relevance score (typically 0, 1, or 2 in BEIR).
    """

    query_id: str
    doc_id: str
    relevance: int


@dataclass
class PoisonLabel:
    """Ground-truth label for a poisoned chunk.

    Written by Phase A. Read ONLY by the evaluation module.
    Phase B (detection) must NEVER access these labels.

    Attributes:
        chunk_id: The poisoned chunk's identifier.
        is_poisoned: Always True for entries in the poison label set.
        strategy: Name of the poisoning strategy that created this chunk.
        target_query_id: The query this poison was designed to target (if any).
    """

    chunk_id: str
    is_poisoned: bool
    strategy: str
    target_query_id: str | None = None


@dataclass
class RetrievalResult:
    """A single result from a retrieval operation.

    Attributes:
        chunk: The retrieved chunk.
        score: Retrieval score (cosine similarity, BM25 score, etc.).
        rank: 1-indexed rank in the result list.
    """

    chunk: Chunk
    score: float
    rank: int


@dataclass
class DetectionDecision:
    """The detector's decision for a single candidate chunk.

    Attributes:
        chunk_id: The chunk being evaluated.
        suspicion_score: Scalar anomaly/suspicion score (higher = more suspicious).
        is_flagged: True if the chunk is flagged as suspicious.
        features: The raw feature values used to compute the score.
    """

    chunk_id: str
    suspicion_score: float
    is_flagged: bool
    features: dict[str, float] = field(default_factory=dict)
