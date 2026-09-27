"""
src.phase_a — Phase A: Threat Simulation.

Responsible for:
1. Generating poisoned chunks using configurable attack strategies
2. Injecting poisoned chunks into the retrieval knowledge base
3. Recording ground-truth labels (chunk_id → is_poisoned) for evaluation

Ground-truth labels produced here are ONLY consumed by src.evaluation.
The detection pipeline (src.phase_b) must NEVER import from this package.
"""
