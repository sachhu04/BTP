"""
src.phase_a.strategies.adversarial_passage — Embedding-targeted adversarial passages.

Inspired by Zhong et al. (EMNLP 2023).

This strategy generates passages that are optimized to have high cosine
similarity with target query embeddings in the dense retrieval space,
while containing attacker-controlled content.

Approach:
- Start from a seed text (relevant document or random).
- Iteratively substitute tokens to maximize embedding similarity
  with the target query (gradient-free or gradient-based).
- Validate that the final passage is retrieved in top-k for the target query.

This is expected to be detectable by the dense-sparse disagreement signal
because the optimization targets the embedding space but NOT the BM25
keyword space.
"""

from __future__ import annotations

# from src.phase_a.strategies.base import BasePoisonStrategy, PoisonedChunk

# TODO: Implement AdversarialPassageStrategy(BasePoisonStrategy)
