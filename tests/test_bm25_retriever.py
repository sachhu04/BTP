"""Tests for src.retrieval.bm25 — BM25 retriever."""

from __future__ import annotations

# TODO: Test cases to implement:
#
# - test_retrieve_returns_correct_count: Results length == min(top_k, index_size).
# - test_retrieve_results_sorted_by_score: Results are in descending BM25 score order.
# - test_retrieve_ranks_are_sequential: Ranks are 1, 2, 3, ..., top_k.
# - test_retrieve_implements_interface: BM25Retriever is an instance of BaseRetriever.
# - test_keyword_matching: Query with exact keyword match ranks the matching doc first.
# - test_no_match_query: Query with no keyword overlap returns low/zero scores.
