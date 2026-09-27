"""
src.phase_b — Phase B: Detection Pipeline.

Responsible for:
1. Retrieving candidate chunks via dense and BM25 retrieval
2. Extracting detection features (disagreement, embedding stats, text stats)
3. Computing suspicion scores from features
4. Applying a configurable threshold to flag suspicious chunks
5. Filtering flagged chunks from the LLM context
6. Logging detection decisions to predictions.jsonl

CRITICAL DESIGN RULE:
    This package must NEVER import from src.phase_a.ground_truth
    or read ground_truth.jsonl. The detector operates blind —
    it does not know which chunks are poisoned.
"""
