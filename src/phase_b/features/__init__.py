"""
src.phase_b.features — Feature extractors for candidate chunk analysis.

Each feature extractor computes a set of signals from the retrieval results
that may indicate poisoning. Multiple extractors can be combined by the
scorer to produce a composite suspicion score.

Available extractors:
- disagreement: Dense vs BM25 retrieval disagreement (core research signal)
- embedding_stats: Embedding-space anomaly features
- text_stats: Text-level statistical features
"""
