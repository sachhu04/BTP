"""
src.evaluation.evaluator — Top-level evaluation orchestrator.

Coordinates all metric computations for a single experiment run.

Workflow:
1. Load ground_truth.jsonl from the experiment directory.
2. Load predictions.jsonl from the experiment directory.
3. (Optionally) load generated answers and reference answers.
4. Call each metric module (detection, retrieval, answer, attack, latency).
5. Aggregate results into a single metrics.json.
6. Write metrics.json to the experiment directory.

This is the ONLY module that loads ground-truth labels alongside predictions.

Usage (planned):
    evaluator = Evaluator(config)
    evaluator.evaluate(experiment_dir="experiments/2026-09-28_exp1/")
"""

from __future__ import annotations

# TODO: Implement Evaluator with:
#
# class Evaluator:
#     def __init__(self, config) -> None: ...
#     def evaluate(self, experiment_dir: Path) -> dict[str, float]: ...
#     def _load_ground_truth(self, path: Path) -> dict[str, PoisonLabel]: ...
#     def _load_predictions(self, path: Path) -> list[DetectionDecision]: ...
#     def _write_metrics(self, metrics: dict, path: Path) -> None: ...
