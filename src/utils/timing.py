"""
src.utils.timing — Latency measurement utilities.

Provides decorators and context managers for measuring execution time
of individual pipeline stages (retrieval, feature extraction, scoring,
generation). Timing data is collected for the latency metrics module.

Usage (planned):
    @timed("dense_retrieval")
    def retrieve(query):
        ...

    with Timer("feature_extraction") as t:
        features = extractor.extract(...)
    print(f"Took {t.elapsed_ms:.1f}ms")
"""

from __future__ import annotations

# TODO: Implement:
#
# class Timer:
#     def __init__(self, name: str) -> None: ...
#     def __enter__(self) -> Timer: ...
#     def __exit__(self, *args) -> None: ...
#     @property
#     def elapsed_ms(self) -> float: ...
#
# def timed(name: str) -> Callable: ...  # Decorator version
