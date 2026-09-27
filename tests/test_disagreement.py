"""Tests for src.phase_b.features.disagreement — dense-BM25 disagreement features."""

from __future__ import annotations

# TODO: Test cases to implement:
#
# - test_identical_results_zero_disagreement: When dense and BM25 return the same
#   chunks in the same order, disagreement features should be minimal.
# - test_disjoint_results_max_disagreement: When dense and BM25 return completely
#   different chunk sets, disagreement features should be maximal.
# - test_dense_only_chunks_flagged: Chunks in dense top-k but not BM25 top-k
#   should have in_dense_only=1.
# - test_rank_difference_computed: rank_difference = |dense_rank - bm25_rank|.
# - test_jaccard_range: Jaccard similarity is between 0 and 1.
# - test_rbo_range: Rank-Biased Overlap is between 0 and 1.
# - test_features_returned_for_all_candidates: Feature dict includes every chunk
#   in the union of both result lists.
