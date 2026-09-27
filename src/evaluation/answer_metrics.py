"""
src.evaluation.answer_metrics — Answer quality metrics.

Computes metrics comparing the LLM-generated answer against reference
answers from the BEIR qrels / dataset.

Metrics:
- Exact Match (EM): 1 if the prediction exactly matches the reference.
- Token-level F1: Harmonic mean of token precision and recall.
- BERTScore: Semantic similarity between prediction and reference embeddings.

Usage (planned):
    metrics = compute_answer_metrics(predictions, references)
"""

from __future__ import annotations

# TODO: Implement:
#
# def compute_answer_metrics(
#     predictions: dict[str, str],   # query_id → generated answer
#     references: dict[str, str],    # query_id → reference answer
# ) -> dict[str, float]: ...
#
# def exact_match(prediction: str, reference: str) -> float: ...
# def token_f1(prediction: str, reference: str) -> float: ...
