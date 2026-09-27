"""
src.data.beir_loader — Download and lazy-load BEIR-format datasets.

Responsibilities:
- Download a BEIR dataset by name (using HuggingFace datasets or direct URL).
- Lazy-load corpus.jsonl and queries.jsonl using generators to avoid loading
  multi-million-document corpora entirely into memory.
- Load qrels (query-document relevance judgments).
- Support configurable dataset name so any BEIR dataset can be substituted.

The dataset layer is independent from poisoning and detection code.

Usage (planned):
    loader = BEIRLoader(config)
    for doc in loader.iter_corpus():
        ...
    queries = loader.load_queries()
    qrels = loader.load_qrels(split="test")
"""

from __future__ import annotations

# TODO: Implement BEIRLoader class with the following interface:
#
# class BEIRLoader:
#     def __init__(self, config: DatasetConfig) -> None: ...
#     def download(self) -> Path: ...
#     def iter_corpus(self) -> Iterator[Document]: ...
#     def load_queries(self, split: str = "test") -> list[Query]: ...
#     def load_qrels(self, split: str = "test") -> list[QRel]: ...
#     def corpus_size(self) -> int: ...
