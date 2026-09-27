"""
src.retrieval.base — Abstract Retriever interface.

All retriever implementations (dense, BM25, hybrid) must implement this
interface. This enables:
- Swapping retrievers in experiments without changing downstream code.
- Running dense-only, BM25-only, or combined experiments.
- The disagreement detector to be agnostic to which retrievers produced results.

The interface defines a single method:
    retrieve(query: str, top_k: int) → list[RetrievalResult]
"""

from __future__ import annotations

from abc import ABC, abstractmethod

# from src.data.schema import RetrievalResult


class BaseRetriever(ABC):
    """Abstract base class for all retriever implementations.

    Every retriever must implement the `retrieve` method, which takes
    a query string and returns the top-k most relevant chunks with
    their scores and ranks.
    """

    @abstractmethod
    def retrieve(self, query: str, top_k: int) -> list:
        """Retrieve the top-k most relevant chunks for a query.

        Args:
            query: The user query string.
            top_k: Number of results to return.

        Returns:
            A list of RetrievalResult objects, sorted by descending score,
            with rank assigned starting from 1.
        """
        ...

    @abstractmethod
    def index_size(self) -> int:
        """Return the number of chunks currently in the index."""
        ...
