"""
src.rag.llm_client — LLM backend abstraction.

Provides a unified interface for interacting with different LLM backends:
- "none": No LLM (for experiments focused purely on retrieval/detection).
- "huggingface": Local model via HuggingFace Transformers (e.g., Mistral-7B).
- "openai_compatible": Remote API compatible with the OpenAI chat completions format.
- "mock": Returns a fixed response (for testing).

The backend is selected via configuration. No LangChain dependency.

Usage (planned):
    client = LLMClient(config)
    response = client.generate(prompt="...", max_new_tokens=256)
"""

from __future__ import annotations

# TODO: Implement LLMClient with:
#
# class LLMClient:
#     def __init__(self, config: LLMConfig) -> None: ...
#     def generate(self, prompt: str, **kwargs) -> str: ...
#     def is_available(self) -> bool: ...
