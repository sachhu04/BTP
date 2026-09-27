"""
src.phase_b.features.disagreement — Dense vs BM25 retrieval disagreement features.

This is the CORE RESEARCH MODULE of the project.

Research hypothesis:
    Poisoned documents that are adversarially optimized for dense (embedding-based)
    retrieval may NOT rank highly under sparse (BM25) retrieval, because the
    optimization targets the embedding space but not the keyword space.
    This "disagreement" can serve as a lightweight detection signal.

Features computed for each candidate chunk:
- rank_difference: |dense_rank - bm25_rank| (normalized). High = suspicious.
- in_dense_only: 1 if chunk is in dense top-k but NOT in BM25 top-k.
- in_bm25_only: 1 if chunk is in BM25 top-k but NOT in dense top-k.
- score_ratio: dense_score / bm25_score (normalized). Extreme ratios = suspicious.
- rbo: Rank-Biased Overlap between the two full result lists.
- jaccard: Jaccard similarity of the two result sets.

IMPORTANT: This is a RESEARCH HYPOTHESIS, not an established fact.
The implementation must allow us to experimentally determine whether
poisoned chunks actually exhibit different retrieval behaviour.
"""

from __future__ import annotations

# from src.phase_b.features.base import BaseFeatureExtractor

# TODO: Implement DisagreementFeatureExtractor(BaseFeatureExtractor) with:
#
# class DisagreementFeatureExtractor(BaseFeatureExtractor):
#     name = "disagreement"
#     feature_names = [
#         "rank_difference",
#         "in_dense_only",
#         "in_bm25_only",
#         "score_ratio",
#         "rbo",
#         "jaccard",
#     ]
#
#     def extract(self, query, dense_results, bm25_results) -> dict: ...
#     def _compute_rank_difference(self, ...) -> float: ...
#     def _compute_rbo(self, list_a, list_b, p=0.9) -> float: ...
#     def _compute_jaccard(self, set_a, set_b) -> float: ...
