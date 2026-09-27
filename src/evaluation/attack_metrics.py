"""
src.evaluation.attack_metrics — Attack success rate metrics.

Computes the Attack Success Rate (ASR): the fraction of targeted queries
where the LLM produced the attacker's intended (wrong) answer.

ASR = (queries where LLM outputs attacker's target answer) / (total targeted queries)

A good defense should reduce ASR from ~90% (PoisonedRAG baseline) to <10%.

Usage (planned):
    asr = compute_attack_success_rate(generated_answers, target_answers, targeted_query_ids)
"""

from __future__ import annotations

# TODO: Implement:
#
# def compute_attack_success_rate(
#     generated: dict[str, str],       # query_id → generated answer
#     target_answers: dict[str, str],  # query_id → attacker's intended answer
#     targeted_ids: list[str],         # query IDs that were targeted by the attack
# ) -> float: ...
