# Architecture

## Two-Phase Design

This project follows a two-phase architecture designed for research reproducibility.

### Phase A: Threat Simulation

**Goal:** Create a poisoned knowledge base with known ground-truth labels.

```
Clean BEIR Corpus
    ↓
Chunking (configurable strategy)
    ↓
Embedding + Index Building (FAISS + BM25)
    ↓
Poison Generation (configurable strategy)
    ↓
Poison Injection (update indices)
    ↓
Ground-Truth Labels → experiments/<id>/ground_truth.jsonl
```

**Code:** `src/phase_a/`, `src/data/`, `src/retrieval/index_builder.py`

### Phase B: Detection Pipeline

**Goal:** Detect poisoned chunks without access to ground-truth labels.

```
User Query
    ↓
┌───────────┬───────────┐
│  Dense    │   BM25    │
│ Retriever │ Retriever │
└─────┬─────┴─────┬─────┘
      │           │
      ↓           ↓
Feature Extraction (disagreement, embedding, text)
      ↓
Suspicion Scoring
      ↓
Threshold Decision (retain / flag)
      ↓
┌───────────┬───────────┐
│ Retained  │  Flagged  │
│ (→ LLM)   │ (excluded)│
└─────┬─────┴─────┬─────┘
      ↓           ↓
LLM Generation  predictions.jsonl
      ↓
Generated Answer
```

**Code:** `src/phase_b/`, `src/retrieval/`, `src/rag/`

### Evaluation

**Goal:** Compare Phase B predictions against Phase A ground-truth labels.

**Code:** `src/evaluation/`

## Ground-Truth Isolation

The ground-truth labels produced by Phase A are stored in the experiment directory and are ONLY read by the evaluation module. The detection pipeline (`src/phase_b/`) never imports from `src/phase_a/ground_truth.py` and never reads `ground_truth.jsonl`.

## Key Interfaces

### `BaseRetriever.retrieve(query, top_k) → list[RetrievalResult]`
All retrievers (dense, BM25, hybrid) share this interface.

### `BasePoisonStrategy.generate(target_queries, corpus, config) → list[PoisonedChunk]`
All attack strategies share this interface.

### `BaseFeatureExtractor.extract(query, dense_results, bm25_results) → dict`
All feature extractors share this interface.
