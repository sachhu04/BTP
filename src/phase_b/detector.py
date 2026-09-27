"""
src.phase_b.detector — Threshold-based retain/flag decision.

Responsibilities:
- Accept suspicion scores for each candidate chunk (from the Scorer).
- Apply a configurable threshold to produce binary decisions.
- Output a DetectionDecision (retain or flag) for each chunk.

This module has NO ACCESS to ground-truth labels.
It operates purely on computed suspicion scores.

Usage (planned):
    detector = Detector(config)
    decisions = detector.decide(scores, features)
    # decisions: list[DetectionDecision]
"""

from __future__ import annotations

# TODO: Implement Detector with:
#
# class Detector:
#     def __init__(self, threshold: float) -> None: ...
#     def decide(self, scores: dict[str, float],
#                features: dict[str, dict[str, float]]) -> list[DetectionDecision]: ...
