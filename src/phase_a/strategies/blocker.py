"""
src.phase_a.strategies.blocker — Refusal-inducing blocker documents.

Inspired by "Machine Against the RAG" (Shafran et al., USENIX Security 2025).

This strategy generates documents designed to cause the LLM to refuse to
answer or produce an unhelpful response, effectively performing a denial-of-
service attack on the RAG system.

Approach:
- Generate documents that contain safety/refusal triggers when retrieved.
- Optimize for high retrieval similarity with target queries.
- The LLM, upon seeing these documents in its context, is induced to
  refuse to answer rather than producing incorrect information.
"""

from __future__ import annotations

# from src.phase_a.strategies.base import BasePoisonStrategy, PoisonedChunk

# TODO: Implement BlockerStrategy(BasePoisonStrategy)
