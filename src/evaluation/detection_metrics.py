"""
src.evaluation.detection_metrics — Detection performance metrics.

Computes metrics by comparing Phase B detection decisions against
Phase A ground-truth labels.

Metrics:
- Accuracy: (TP + TN) / (TP + TN + FP + FN)
- Precision: TP / (TP + FP)
- Recall (TPR): TP / (TP + FN)
- F1 Score: Harmonic mean of precision and recall
- False Positive Rate: FP / (FP + TN)
- False Negative Rate: FN / (FN + TP)
- AUC-ROC: Area under ROC curve across thresholds

Usage (planned):
    metrics = compute_detection_metrics(ground_truth, predictions)
"""

from __future__ import annotations

# TODO: Implement:
#
# def compute_detection_metrics(
#     ground_truth: dict[str, PoisonLabel],
#     predictions: list[DetectionDecision],
# ) -> dict[str, float]: ...
#
# def compute_roc_auc(
#     ground_truth: dict[str, PoisonLabel],
#     scores: dict[str, float],
# ) -> float: ...
