"""
src.rag.generator — Generate answers from retained context.

Responsibilities:
- Accept retained (filtered) chunks and the user query.
- Construct a prompt using PromptTemplates.
- Call the LLM via LLMClient.
- Return the generated answer text.
- Measure and report generation latency.

Usage (planned):
    generator = Generator(llm_client, prompt_templates)
    answer = generator.generate(query="...", retained_chunks=[...])
"""

from __future__ import annotations

# TODO: Implement Generator with:
#
# class Generator:
#     def __init__(self, llm_client: LLMClient,
#                  prompt_templates: PromptTemplates) -> None: ...
#     def generate(self, query: str, retained_chunks: list[Chunk]) -> str: ...
