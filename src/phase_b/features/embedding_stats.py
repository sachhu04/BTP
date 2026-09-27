"""
src.phase_b.features.embedding_stats — Embedding-space statistical features.

Computes anomaly features based on the geometric properties of chunk
embeddings relative to the query and the corpus distribution.

Features computed for each candidate chunk:
- query_distance: Cosine distance between chunk embedding and query embedding.
- corpus_centroid_distance: Distance from the chunk to the corpus centroid.
- nearest_neighbor_distance: Distance to the chunk's nearest neighbor in the index.
- embedding_norm: L2 norm of the chunk embedding.
- isolation_score: How isolated the chunk is relative to its neighborhood.

These features may capture adversarial passages that have been optimized
to sit in unusual regions of the embedding space.
"""

from __future__ import annotations

# from src.phase_b.features.base import BaseFeatureExtractor

# TODO: Implement EmbeddingStatsExtractor(BaseFeatureExtractor)
