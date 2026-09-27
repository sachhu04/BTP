"""Tests for src.phase_b.detector — threshold-based detection."""

from __future__ import annotations

# TODO: Test cases to implement:
#
# - test_above_threshold_flagged: Chunks with score > threshold are flagged.
# - test_below_threshold_retained: Chunks with score <= threshold are retained.
# - test_threshold_zero_flags_all: threshold=0 flags everything.
# - test_threshold_one_retains_all: threshold=1.0 retains everything (if scores ∈ [0,1]).
# - test_decisions_contain_all_chunks: Every scored chunk gets a decision.
# - test_detector_does_not_use_ground_truth: Verify no import from phase_a.ground_truth.
