"""
src.phase_a.ground_truth — Generate and persist ground-truth labels.

Responsibilities:
- Accept the list of injected poisoned chunk IDs from the Injector.
- Generate a ground_truth.jsonl file mapping chunk_id → PoisonLabel.
- Write this file to the experiment directory.

CRITICAL DESIGN RULE:
    This module is consumed ONLY by src.evaluation.
    The detection pipeline (src.phase_b) must NEVER import this module
    or read ground_truth.jsonl. The detector must operate blind.

Usage (planned):
    writer = GroundTruthWriter()
    writer.write(poisoned_chunk_ids, all_chunk_ids, strategy_name,
                 output_path="experiments/<id>/ground_truth.jsonl")
"""

from __future__ import annotations

# TODO: Implement GroundTruthWriter with:
#
# class GroundTruthWriter:
#     def write(self, poisoned_ids: list[str], all_ids: list[str],
#               strategy: str, target_map: dict[str, str],
#               output_path: Path) -> None: ...
#
#     def load(self, path: Path) -> dict[str, PoisonLabel]: ...
