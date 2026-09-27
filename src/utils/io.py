"""
src.utils.io — File I/O helper functions.

Provides common I/O patterns used throughout the project:
- JSONL streaming reader (generator-based, memory efficient).
- JSONL writer (append or overwrite mode).
- Pickle save/load for serialized objects (BM25 index, etc.).
- Path resolution helpers.

Usage (planned):
    for record in read_jsonl("data/processed/nfcorpus/chunks.jsonl"):
        ...
    write_jsonl(records, "experiments/exp1/predictions.jsonl")
    save_pickle(bm25_index, "data/indices/nfcorpus/bm25.pkl")
"""

from __future__ import annotations

# TODO: Implement:
#
# def read_jsonl(path: str | Path) -> Iterator[dict]: ...
# def write_jsonl(records: Iterable[dict], path: str | Path, mode: str = "w") -> None: ...
# def save_pickle(obj: Any, path: str | Path) -> None: ...
# def load_pickle(path: str | Path) -> Any: ...
# def ensure_dir(path: str | Path) -> Path: ...
