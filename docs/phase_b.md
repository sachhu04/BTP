# Phase B: Detection Pipeline — Design Notes

## Purpose

Phase B detects poisoned chunks at query time **without access to ground-truth labels**.
It must operate as if it does not know which documents were poisoned.

## Pipeline Steps

For each user query:

1. **Dense retrieval:** Retrieve top-k candidates via FAISS.
2. **BM25 retrieval:** Retrieve top-k candidates via BM25.
3. **Feature extraction:** Compute detection signals for each candidate.
4. **Suspicion scoring:** Combine features into a scalar score.
5. **Detection decision:** Apply threshold to decide retain/flag.
6. **Filtering:** Partition candidates into retained and flagged sets.
7. **LLM generation:** Generate answer from retained context only.
8. **Logging:** Write decisions to `predictions.jsonl`.

## Research Signal: Dense–Sparse Disagreement

The core hypothesis is that poisoned chunks optimized for dense retrieval
will NOT rank highly under BM25, creating a detectable "disagreement."

Key features in `src/phase_b/features/disagreement.py`:
- `rank_difference`: |dense_rank - bm25_rank|
- `in_dense_only`: Present in dense top-k but absent from BM25 top-k
- `score_ratio`: dense_score / bm25_score
- `rbo`: Rank-Biased Overlap between result lists
- `jaccard`: Jaccard similarity of result sets

**This is a hypothesis under investigation, not an established fact.**

## Ground-Truth Isolation

`src/phase_b/` has ZERO imports from `src/phase_a/ground_truth`.
This is enforced by convention and tested in `tests/test_detector.py`.

## Configuration

Detection parameters are in `configs/default.yaml` under `detection:`.
Key parameters:
- `features`: List of feature extractors to use
- `scorer.method`: Scoring algorithm
- `threshold`: Suspicion score threshold
