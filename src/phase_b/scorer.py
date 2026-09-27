"""
src.phase_b.scorer — Compute suspicion scores from extracted features.

Responsibilities:
- Accept feature vectors for each candidate chunk (from one or more extractors).
- Combine features into a scalar suspicion score using a configurable method.
- Support multiple scoring methods:
    - "weighted_sum": Linear combination of features with configurable weights.
    - "isolation_forest": scikit-learn Isolation Forest on the feature matrix.
    - "threshold_rule": Simple rule-based scoring (e.g., flag if in_dense_only=1).

The scorer does NOT make the retain/flag decision — that is the detector's job.

Usage (planned):
    scorer = Scorer(config)
    scores = scorer.score(features_by_chunk)
    # scores: dict[chunk_id, float]
"""

from __future__ import annotations

# TODO: Implement Scorer with:
#
# class Scorer:
#     def __init__(self, config: ScorerConfig) -> None: ...
#     def score(self, features: dict[str, dict[str, float]]) -> dict[str, float]: ...
#     def _weighted_sum(self, features: dict[str, float]) -> float: ...
#     def _isolation_forest(self, feature_matrix: np.ndarray) -> np.ndarray: ...
