"""
src.phase_b.features.base — Abstract interface for feature extractors.

All feature extractors implement this interface. Each extractor receives
the query and retrieval results from both dense and BM25 retrievers,
and returns a dictionary of feature name → value for each candidate chunk.

This design allows:
- Running experiments with different feature combinations.
- Adding new feature extractors without modifying the scorer or pipeline.
- Independently testing each extractor.
"""

from __future__ import annotations

from abc import ABC, abstractmethod

# from src.data.schema import RetrievalResult


class BaseFeatureExtractor(ABC):
    """Abstract base class for feature extractors.

    Each extractor computes features for every candidate chunk based on
    the retrieval results from dense and BM25 retrievers.
    """

    @abstractmethod
    def extract(
        self,
        query: str,
        dense_results: list,
        bm25_results: list,
    ) -> dict[str, dict[str, float]]:
        """Extract features for each candidate chunk.

        Args:
            query: The user query string.
            dense_results: Top-k results from dense retrieval.
            bm25_results: Top-k results from BM25 retrieval.

        Returns:
            A dict mapping chunk_id → {feature_name: feature_value}.
            Must include entries for all chunks in the union of both result lists.
        """
        ...

    @property
    @abstractmethod
    def name(self) -> str:
        """Return the extractor name (used as config key and log prefix)."""
        ...

    @property
    @abstractmethod
    def feature_names(self) -> list[str]:
        """Return the names of features this extractor produces."""
        ...
