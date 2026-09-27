# Analysis and Detection of Data Poisoning Attacks in LLM Retrieval Pipelines

> BTech Project — 2026

## Overview

This project investigates **data poisoning attacks** against Retrieval-Augmented Generation (RAG) systems and develops **lightweight detection mechanisms** to identify and exclude poisoned documents from the LLM context window.

### Research Hypothesis

Poisoned documents that are adversarially optimized for dense (embedding-based) retrieval may exhibit **measurably different retrieval behaviour** under sparse (BM25) retrieval. This _dense–sparse disagreement_ can serve as a lightweight, training-free detection signal.

### Two-Phase Architecture

| Phase | Purpose | Key Output |
|-------|---------|------------|
| **Phase A — Threat Simulation** | Build a clean retrieval corpus, generate poisoned entries using configurable attack strategies, inject them into the knowledge base, and record ground-truth labels | Poisoned knowledge base + `ground_truth.jsonl` |
| **Phase B — Detection Pipeline** | For each user query, retrieve candidates via dense and BM25 retrieval, extract detection features, score suspicion, apply a threshold, filter flagged chunks, and generate an answer from retained context | `predictions.jsonl` + generated answers |
| **Evaluation** | Compare Phase B predictions against Phase A ground-truth labels | Detection metrics, retrieval metrics, answer quality, ASR, latency |

## Project Structure

```
rag-poison-detection/
├── configs/          # YAML configuration files
├── data/             # Raw, processed, and indexed data (gitignored)
├── src/              # Core implementation
│   ├── data/         # BEIR loading, chunking, schemas
│   ├── retrieval/    # Dense, BM25, and hybrid retrievers
│   ├── phase_a/      # Threat simulation (poisoning + ground truth)
│   ├── phase_b/      # Detection pipeline (features + scoring + filtering)
│   ├── rag/          # LLM generation
│   ├── evaluation/   # All metrics computation
│   └── utils/        # Config, logging, I/O, reproducibility
├── scripts/          # Numbered entry-point scripts (01–07)
├── experiments/      # Per-run outputs (config, labels, predictions, metrics)
├── results/          # Aggregated tables, plots, reports
├── notebooks/        # Exploratory analysis and visualization
├── tests/            # Pytest test suite
└── docs/             # Architecture and contributor documentation
```

## Setup

### Prerequisites

- Python 3.10+
- (Optional) CUDA-capable GPU for embedding and LLM inference

### Installation

```bash
# Clone the repository
git clone <repo-url>
cd rag-poison-detection

# Create a virtual environment
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# (Optional) Install in editable mode for development
pip install -e .
```

### Environment Variables

Copy the example environment file and fill in any required values:

```bash
cp .env.example .env
```

## Usage

Run scripts in order for a full experiment:

```bash
# 1. Download a BEIR dataset
python scripts/01_download_dataset.py --config configs/default.yaml

# 2. Chunk the corpus
python scripts/02_preprocess_corpus.py --config configs/default.yaml

# 3. Build retrieval indices (FAISS + BM25)
python scripts/03_build_indices.py --config configs/default.yaml

# 4. Run Phase A: threat simulation
python scripts/04_run_phase_a.py --config configs/default.yaml --poison-config configs/poisoning/targeted_corruption.yaml

# 5. Run Phase B: detection pipeline
python scripts/05_run_phase_b.py --config configs/default.yaml --experiment-dir experiments/<experiment_id>

# 6. Evaluate
python scripts/06_evaluate.py --experiment-dir experiments/<experiment_id>

# 7. Or run an end-to-end experiment sweep
python scripts/07_run_experiment.py --config configs/experiments/exp_poison_rate_sweep.yaml
```

## Running Tests

```bash
pytest tests/ -v
```

## Technology Stack

| Component | Tool |
|-----------|------|
| Dense embeddings | Sentence Transformers |
| Dense retrieval | FAISS |
| Sparse retrieval | rank_bm25 |
| Data format | BEIR-compatible JSONL |
| Numerics | NumPy, pandas |
| ML utilities | scikit-learn |
| Visualization | Matplotlib, seaborn |
| LLM (optional) | HuggingFace Transformers / OpenAI-compatible API |

## Team

- [Team member names here]

## License

[License here]
