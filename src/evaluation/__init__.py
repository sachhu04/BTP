"""
src.evaluation — Evaluation module.

This is the ONLY place where ground-truth labels (from Phase A) are
loaded alongside detection predictions (from Phase B) to compute
performance metrics.

Metric categories:
- Detection: Precision, Recall, F1, FPR, FNR, AUC-ROC
- Retrieval: Recall@k, Precision@k, MRR, Retrieval Success Rate
- Answer quality: Exact Match, token-level F1, BERTScore
- Attack: Attack Success Rate (ASR)
- Latency: Per-query and aggregate timing
"""
