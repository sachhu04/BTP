"""Tests for src.evaluation.evaluator — evaluation orchestrator."""

from __future__ import annotations

# TODO: Test cases to implement:
#
# - test_perfect_detection: All poisoned flagged, all clean retained → F1=1.0.
# - test_no_detection: No chunks flagged → recall=0, FPR=0.
# - test_all_flagged: All chunks flagged → recall=1.0, high FPR.
# - test_metrics_keys: metrics.json contains all expected metric keys.
# - test_detection_metrics_range: All metrics are in valid ranges [0, 1].
