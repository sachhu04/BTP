"""Tests for src.phase_a.ground_truth — ground-truth label generation."""

from __future__ import annotations

# TODO: Test cases to implement:
#
# - test_write_labels_creates_file: ground_truth.jsonl is created.
# - test_labels_contain_all_chunks: Every chunk_id in the corpus appears in labels.
# - test_poisoned_chunks_marked: Injected chunk IDs are marked is_poisoned=True.
# - test_clean_chunks_unmarked: Clean chunk IDs are marked is_poisoned=False.
# - test_labels_include_strategy: PoisonLabel.strategy is set correctly.
# - test_load_round_trip: Write → load produces identical labels.
