# Phase A: Threat Simulation — Design Notes

## Purpose

Phase A builds a poisoned knowledge base with known ground-truth labels,
enabling controlled evaluation of Phase B detection methods.

## Pipeline Steps

1. **Load corpus:** `BEIRLoader` downloads/loads a BEIR dataset.
2. **Chunk documents:** `Chunker` splits documents into chunks.
3. **Build indices:** `IndexBuilder` creates FAISS + BM25 indices.
4. **Select targets:** Choose which queries to target for poisoning.
5. **Generate poisons:** A `PoisonStrategy` creates `PoisonedChunk` objects.
6. **Inject poisons:** `Injector` adds poisoned chunks to the indices.
7. **Record labels:** `GroundTruthWriter` writes `ground_truth.jsonl`.

## Adding a New Attack Strategy

See [adding_a_poison_strategy.md](adding_a_poison_strategy.md).

## Configuration

Poisoning parameters are in `configs/poisoning/<strategy>.yaml`.
Key parameters:
- `strategy`: Strategy name
- `num_poisoned`: Number of poisoned chunks to inject
- `poison_rate`: Alternative to num_poisoned (as a fraction)
- `target_queries`: Which queries to target ("random", "all", or list)
- Strategy-specific sub-parameters

## Output

- Updated indices in `data/indices/<dataset>/`
- `experiments/<id>/ground_truth.jsonl`
