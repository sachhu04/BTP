# Experiments

Each experiment run is stored in a timestamped subdirectory.

## Naming Convention

```
experiments/<YYYY-MM-DD>_<experiment_name>/
```

Example: `experiments/2026-10-01_poison_rate_sweep_nfcorpus/`

## Contents per Experiment

```
<experiment_id>/
├── config.yaml          # Frozen snapshot of the full merged config
├── ground_truth.jsonl   # Phase A output: {chunk_id, is_poisoned, strategy, target_query_id}
├── predictions.jsonl    # Phase B output: {chunk_id, suspicion_score, is_flagged, features}
├── metrics.json         # Evaluation output: all computed metrics
└── logs/
    └── run.log          # Full execution log
```

## Reproducibility

Any experiment can be exactly reproduced:
```bash
python scripts/07_run_experiment.py --config experiments/<id>/config.yaml
```
