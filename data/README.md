# Data Directory

This directory stores all data artifacts. It is **gitignored** — do not commit large data files.

## Layout

```
data/
├── raw/                    # Downloaded BEIR datasets (untouched originals)
│   └── <dataset_name>/
│       ├── corpus.jsonl    # One JSON object per document: {"_id": ..., "title": ..., "text": ...}
│       ├── queries.jsonl   # One JSON object per query: {"_id": ..., "text": ...}
│       └── qrels/
│           └── test.tsv    # Tab-separated: query_id, corpus_id, relevance_score
│
├── processed/              # Chunked corpus ready for indexing
│   └── <dataset_name>/
│       └── chunks.jsonl    # One JSON object per chunk: {"chunk_id": ..., "doc_id": ..., "text": ..., "metadata": {...}}
│
└── indices/                # Serialized retrieval indices
    └── <dataset_name>/
        ├── faiss.index     # FAISS dense retrieval index
        ├── faiss_id_map.json  # Maps FAISS internal IDs → chunk_ids
        └── bm25.pkl        # Pickled BM25 index
```

## Download

Run the download script to populate `raw/`:

```bash
python scripts/01_download_dataset.py --config configs/default.yaml
```

The script uses the `beir` dataset loader from HuggingFace `datasets` or the BEIR benchmark library.
