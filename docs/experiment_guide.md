# Experiment Guide

## Running a Single Experiment

### Step-by-step

```bash
# 1. Download dataset
python scripts/01_download_dataset.py --config configs/default.yaml

# 2. Preprocess
python scripts/02_preprocess_corpus.py --config configs/default.yaml

# 3. Build indices
python scripts/03_build_indices.py --config configs/default.yaml

# 4. Run Phase A
python scripts/04_run_phase_a.py \
    --config configs/default.yaml \
    --poison-config configs/poisoning/targeted_corruption.yaml \
    --experiment-id my_first_experiment

# 5. Run Phase B
python scripts/05_run_phase_b.py \
    --config configs/default.yaml \
    --experiment-dir experiments/my_first_experiment

# 6. Evaluate
python scripts/06_evaluate.py \
    --experiment-dir experiments/my_first_experiment
```

## Running a Parameter Sweep

```bash
python scripts/07_run_experiment.py \
    --config configs/experiments/exp_poison_rate_sweep.yaml
```

This will:
1. Read the sweep configuration
2. Generate all parameter combinations
3. Run Phase A → Phase B → Evaluation for each combination
4. Save results in separate experiment subdirectories

## Defining a Custom Experiment

Create a YAML file in `configs/experiments/`:

```yaml
experiment:
  name: "my_custom_sweep"
  description: "..."

  base_config: "configs/default.yaml"
  dataset_config: "configs/datasets/nfcorpus.yaml"
  poison_config: "configs/poisoning/targeted_corruption.yaml"

  sweep:
    parameter: "poisoning.num_poisoned"
    values: [1, 5, 10, 20]

  overrides:
    retrieval.top_k: 10
    seed: 42
```

## Experiment Output Structure

```
experiments/<experiment_id>/
├── config.yaml          # Exact config used (frozen at start)
├── ground_truth.jsonl   # Phase A labels
├── predictions.jsonl    # Phase B decisions
├── metrics.json         # All computed metrics
└── logs/
    └── run.log
```

## Reproducing an Experiment

```bash
# Re-run with the exact same config
python scripts/07_run_experiment.py \
    --config experiments/<experiment_id>/config.yaml
```
