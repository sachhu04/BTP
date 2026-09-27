"""
src.phase_b.features.text_stats — Text-level statistical features.

Computes lightweight, always-available features based on the textual
properties of candidate chunks. These do not require embeddings or
model inference.

Features computed for each candidate chunk:
- chunk_length: Number of tokens in the chunk.
- vocab_richness: Type-token ratio (unique tokens / total tokens).
- avg_word_length: Average word length in characters.
- special_char_ratio: Fraction of non-alphanumeric characters.
- perplexity: (Optional) LM perplexity score if a language model is available.

These features are supplementary — primarily useful as part of an
ensemble with disagreement and embedding features.
"""

from __future__ import annotations

# from src.phase_b.features.base import BaseFeatureExtractor

# TODO: Implement TextStatsExtractor(BaseFeatureExtractor)
