"""
Shared pytest fixtures for the test suite.

Provides small, in-memory test data so tests run fast without
downloading BEIR datasets or building real indices.
"""

from __future__ import annotations

import pytest

from src.data.schema import Chunk, Query, RetrievalResult, PoisonLabel


# ── Fixtures: Mini Corpus ──


@pytest.fixture
def sample_chunks() -> list[Chunk]:
    """A small corpus of 10 clean chunks for testing."""
    return [
        Chunk(
            chunk_id=f"clean_{i:03d}",
            doc_id=f"doc_{i:03d}",
            text=f"This is clean document number {i} about topic {chr(65 + i)}.",
            metadata={"source": "test"},
        )
        for i in range(10)
    ]


@pytest.fixture
def sample_poisoned_chunks() -> list[Chunk]:
    """A small set of 3 poisoned chunks for testing."""
    return [
        Chunk(
            chunk_id=f"poison_{i:03d}",
            doc_id=f"poison_doc_{i:03d}",
            text=f"This is a poisoned document number {i} with misleading information.",
            metadata={"source": "test", "poisoned": True},
        )
        for i in range(3)
    ]


@pytest.fixture
def sample_queries() -> list[Query]:
    """A small set of 5 queries for testing."""
    return [
        Query(query_id=f"q_{i:03d}", text=f"What is topic {chr(65 + i)}?")
        for i in range(5)
    ]


@pytest.fixture
def sample_ground_truth() -> dict[str, PoisonLabel]:
    """Ground-truth labels for the sample corpus (10 clean + 3 poisoned)."""
    labels = {}
    for i in range(10):
        labels[f"clean_{i:03d}"] = PoisonLabel(
            chunk_id=f"clean_{i:03d}",
            is_poisoned=False,
            strategy="none",
        )
    for i in range(3):
        labels[f"poison_{i:03d}"] = PoisonLabel(
            chunk_id=f"poison_{i:03d}",
            is_poisoned=True,
            strategy="targeted_corruption",
            target_query_id=f"q_{i:03d}",
        )
    return labels


@pytest.fixture
def sample_dense_results(sample_chunks, sample_poisoned_chunks) -> list[RetrievalResult]:
    """Simulated dense retrieval results (poisoned docs rank high)."""
    all_chunks = sample_poisoned_chunks + sample_chunks[:7]
    return [
        RetrievalResult(chunk=c, score=1.0 - i * 0.1, rank=i + 1)
        for i, c in enumerate(all_chunks)
    ]


@pytest.fixture
def sample_bm25_results(sample_chunks) -> list[RetrievalResult]:
    """Simulated BM25 results (poisoned docs do NOT appear)."""
    return [
        RetrievalResult(chunk=c, score=10.0 - i, rank=i + 1)
        for i, c in enumerate(sample_chunks)
    ]
