"""
src.rag.prompt_templates — System and user prompt templates for RAG generation.

Provides configurable prompt templates that format the system instruction,
retrieved context chunks, and user query into a final prompt string for
the LLM.

Templates are plain Python f-strings or Jinja2 templates — no framework dependency.

Usage (planned):
    templates = PromptTemplates(config)
    prompt = templates.format_rag_prompt(query="...", context_chunks=[...])
"""

from __future__ import annotations

# TODO: Implement PromptTemplates with:
#
# class PromptTemplates:
#     def __init__(self, config=None) -> None: ...
#     def format_rag_prompt(self, query: str, context_chunks: list[Chunk]) -> str: ...
#     def format_system_prompt(self) -> str: ...
