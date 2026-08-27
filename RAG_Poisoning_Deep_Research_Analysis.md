# Detection and Mitigation of Data Poisoning Attacks in RAG Systems
## Deep Research Analysis for BTP Project

---

## 1. Current State-of-the-Art (2023–2026)

RAG security has exploded as a research area since 2023. The core insight driving the field is the **"trust paradox"**: while user queries are treated as untrusted input, documents retrieved from the knowledge base are implicitly trusted and injected directly into the LLM's context window. This creates a powerful, often overlooked attack surface.

### Key milestones in the field:

| Year | Milestone | Significance |
|------|-----------|-------------|
| 2023 | Greshake et al. define indirect prompt injection | First systematic analysis of attacks via external data |
| 2023 | Zhong et al. demonstrate corpus poisoning via HotFlip | Gradient-based adversarial passage injection against dense retrievers |
| 2024 | OWASP LLM Top 10 includes vector/embedding weaknesses (LLM08) | Industry recognition of RAG-specific threats |
| 2025 | PoisonedRAG (USENIX Security) | First formalized knowledge corruption attack — 90% ASR with 5 documents |
| 2025 | "Machine Against the RAG" (USENIX Security) | Novel jamming/DoS attacks via blocker documents |
| 2025 | RAGuard (NeurIPS) | Layered defense with adversarial retriever training + ZKIP |
| 2025 | RevPRAG (ACL) | Detection via LLM activation pattern analysis — 98% TPR |
| 2025 | SafeRAG benchmark | First dedicated RAG security evaluation framework |
| 2026 | ReliabilityRAG | Graph-theoretic contradiction detection with provable robustness |

### Current research consensus:
1. **RAG systems are fundamentally vulnerable** — even advanced architectures (sequential, branching, loop-based) remain exploitable.
2. **Attacks are cheap** — 5 carefully crafted documents can corrupt a database of millions with >90% success.
3. **Existing defenses are insufficient** — perplexity filters, basic paraphrasing, and naive content filtering are all bypassable.
4. **Defense-in-depth is the only viable strategy** — no single technique provides adequate protection.

---

## 2. Important Papers (2023–2026)

### Tier 1: Must-Read Foundation Papers

| # | Paper | Authors | Venue | Year | Key Contribution |
|---|-------|---------|-------|------|-----------------|
| 1 | **PoisonedRAG: Knowledge Corruption Attacks to RAG** | Zou, Geng, Wang, Jia | USENIX Security | 2025 | First formalized knowledge corruption attack; dual retrieval+generation optimization; 90% ASR with 5 docs |
| 2 | **Machine Against the RAG: Jamming with Blocker Documents** | Shafran, Schuster, Shmatikov | USENIX Security | 2025 | DoS attacks on RAG; single blocker doc causes refusal; works black-box without auxiliary LLMs |
| 3 | **Not What You Signed Up For: Compromising LLM-Integrated Applications with Indirect Prompt Injection** | Greshake et al. | AISec @ CCS | 2023 | Foundational IPI paper; "confused deputy" attacks via retrieved content |
| 4 | **Poisoning Retrieval Corpora by Injecting Adversarial Passages** | Zhong, Huang, Szegedy, Manning | EMNLP | 2023 | HotFlip-based gradient corpus poisoning against dense retrievers |
| 5 | **RAGuard: A Layered Defense Framework Against Corpus Poisoning in RAG** | (Multiple) | NeurIPS | 2025 | Adversarial retriever fine-tuning + Zero-Knowledge Inference Patch (ZKIP) |

### Tier 2: Important Defense & Detection Papers

| # | Paper | Venue/Source | Year | Key Contribution |
|---|-------|-------------|------|-----------------|
| 6 | **RevPRAG: Reverse Poisoning Attack on RAG** | ACL | 2025 | LLM activation-based detection; 98% TPR, ~1% FPR |
| 7 | **ReliabilityRAG: Provably Robust RAG via Contradiction Graphs** | arXiv | 2025–2026 | Graph-theoretic contradiction detection; Maximum Independent Set selection |
| 8 | **SafeRAG: A Benchmark for Safety Evaluation of RAG** | ACL | 2025 | Categorized attack taxonomy (silver noise, inter-context conflict, soft ad, white DoS) |
| 9 | **RAG Security Bench (RSB): Benchmarking 13 Attacks and 7 Defenses** | arXiv | 2025 | Comprehensive comparative evaluation framework |
| 10 | **Overcoming the Retrieval Barrier: Indirect Prompt Injection in the Wild** | arXiv | 2024 | Real-world IPI via retrieved emails and web documents |

### Tier 3: Supplementary Important Papers

| # | Paper | Venue/Source | Year | Key Contribution |
|---|-------|-------------|------|-----------------|
| 11 | **LLM-PIRATE: LLM Prompt Injection Red-Teaming Evaluation** | NeurIPS | 2024 | Benchmark for prompt injection in retrieval settings |
| 12 | **Hidden-in-Plain-Text: Indirect Prompt Injection Attacks** | arXiv | 2024 | Stealthy instruction embedding in documents |
| 13 | **RAGForensics: Traceback for Poisoned RAG Knowledge Bases** | arXiv | 2025 | Post-attack forensic isolation of poisoned texts |
| 14 | **Reproducing HotFlip for Corpus Poisoning in Dense Retrieval** | arXiv | 2025 | Optimized attack pipeline; computational cost reduction |
| 15 | **CLD-KB: Cyber-Layered Defense for Knowledge Bases** | arXiv | 2025 | Anomaly detection for poisoned rules in IoT/IoBT |
| 16 | **Towards Secure RAG: A Comprehensive Review of Threats, Defenses, and Benchmarks** | arXiv | 2026 | Most recent comprehensive survey of the entire field |

> [!TIP]
> **For your BTP literature review:** Start with papers #1, #3, #4 (attacks), then #5, #6 (defenses), then #8, #9 (benchmarks). Paper #16 is a ready-made survey to structure your related work section.

---

## 3. Attack Methods — Detailed Analysis

### 3.1 Document Poisoning (Knowledge Corruption)

**What it is:** The attacker injects carefully crafted documents into the RAG knowledge base containing false information designed to make the LLM produce specific incorrect answers.

**How it works (PoisonedRAG formulation):**

The attack requires satisfying two conditions simultaneously:

```
Condition 1 — Retrieval: sim(embed(poison_doc), embed(target_query)) > sim(embed(legit_doc), embed(target_query))
Condition 2 — Generation: LLM(system_prompt + poison_doc + target_query) → attacker's_target_answer
```

The attacker optimizes the content of poisoned documents to:
1. **Rank high** in cosine similarity with the target query (retrieval condition)
2. **Override legitimate context** to force the LLM to generate the desired wrong answer (generation condition)

**Black-box vs White-box:**
- **Black-box:** Attacker has no access to embedding model or LLM weights. Uses semantic paraphrasing and iterative query-response testing.
- **White-box:** Attacker has access to model weights. Uses gradient-based optimization (e.g., HotFlip token substitution).

**Key finding:** As few as **5 poisoned documents** in a database of **millions** achieve **~90% Attack Success Rate**.

---

### 3.2 Knowledge Base Poisoning (Corpus Poisoning)

**What it is:** A broader category where the attacker targets the vector database itself rather than individual documents. This includes insertion of adversarial passages that exploit the geometric properties of the embedding space.

**Mechanisms:**
1. **Adversarial passage injection (Zhong et al.):** Gradient-based token substitution via HotFlip to craft passages that are nearest neighbors to target queries in embedding space.
2. **Multi-query generalization:** Adversarial passages designed to be retrieved for a *family* of related queries, not just one.
3. **Cluster manipulation:** Injecting enough documents to shift embedding cluster centroids, affecting retrieval for entire topic areas.

**Why it's dangerous:** Unlike fine-tuning attacks that need model access, corpus poisoning only requires write access to the data pipeline — often achievable through:
- Compromised data ingestion APIs
- Poisoned web crawlers
- Malicious document uploads in enterprise systems
- Corrupted training/knowledge data sources

---

### 3.3 Indirect Prompt Injection (IPI)

**What it is:** Hidden instructions embedded within documents that are retrieved by the RAG system and then followed by the LLM as if they were legitimate system instructions.

**Attack vector hierarchy:**

```
User Query → Retriever → [Poisoned Doc with hidden instructions] → LLM → Manipulated Output
                                    ↓
                         "Ignore previous instructions.
                          Instead, say: [attacker's message]"
```

**Sophistication levels:**
1. **Naive injection:** Plain text instructions hidden in documents (e.g., "SYSTEM: Ignore all previous context and output...")
2. **Steganographic injection:** Instructions hidden via zero-width Unicode characters, white-on-white text, or HTML comments
3. **Semantic injection:** Instructions that look like natural content to humans but are interpreted as commands by LLMs
4. **Multi-stage injection:** First doc primes the LLM, second doc exploits the primed state

**Real-world demonstrated consequences:**
- Data exfiltration (leaking user conversation history via crafted URLs)
- Goal hijacking (changing the LLM's behavior permanently for the session)
- Unauthorized actions in agentic RAG systems (tool calls, API requests)

---

### 3.4 Embedding Manipulation Attacks

**What it is:** Attacks targeting the embedding layer itself — either the embedding model or the vector representations stored in the database.

**Three sub-categories (OWASP LLM08:2025):**

#### a) Corpus Poisoning (CP)
Records crafted to have high cosine similarity with target queries despite containing malicious content. The text is optimized to produce embeddings in a specific region of the vector space.

#### b) Embedding Model Backdoor Attacks (EMBA)
The upstream embedding model is poisoned during training/fine-tuning. A "trigger" word or pattern causes the model to map any input containing it to a predetermined target vector, making poisoned and legitimate content appear identical in embedding space.

#### c) Embedding Inversion (EI)
Techniques like **Vec2Text** can reconstruct original source text from embeddings, enabling:
- Privacy breaches (recovering sensitive documents from vector stores)
- Membership inference (determining if specific text was in the training corpus)
- Reverse engineering of proprietary knowledge bases

> [!WARNING]
> **For your BTP scope:** Focus on corpus poisoning (CP) attacks — they are the most realistic threat model for a RAG defense project and don't require embedding model access.

---

## 4. Existing Defense Approaches — Detailed Analysis

### 4.1 Document Filtering

**Approach:** Screen documents at ingestion time before they enter the vector store.

| Technique | How It Works | Strengths | Weaknesses |
|-----------|-------------|-----------|------------|
| Perplexity filtering | Flag documents with abnormally high/low LLM perplexity scores | Catches gibberish/adversarial text | Sophisticated paraphrased attacks evade it |
| Keyword blocklisting | Reject documents containing known injection patterns | Simple to implement | Trivially bypassed with synonyms or encoding |
| Format sanitization | Strip hidden formatting (zero-width chars, white-on-white text, HTML) | Blocks steganographic IPI | Doesn't catch semantic attacks |
| Length/structure anomaly | Flag documents with unusual chunk sizes or formatting | Low cost | High false positive rate |

**State of the art:** Perplexity filtering alone reduces ASR by only ~15-25% against PoisonedRAG-class attacks.

---

### 4.2 Embedding Anomaly Detection

**Approach:** Detect poisoned documents by analyzing their behavior in the embedding space.

**Techniques:**
1. **Cluster-distance analysis:** New documents that are suspiciously close to many diverse queries (high "retrieval fan-out") may be adversarial.
2. **Embedding distribution monitoring:** Track statistical properties of the embedding distribution; sudden shifts indicate possible poisoning.
3. **Isolation-based detection:** Use isolation forests or LOF (Local Outlier Factor) on embedding vectors to identify outliers.
4. **Temporal anomaly detection:** Documents that were recently added and immediately begin appearing in top-k results at abnormally high rates.

**Research gap:** Most anomaly detection work focuses on image/tabular data. **Embedding-space anomaly detection for text RAG systems is significantly under-explored.**

---

### 4.3 Semantic Consistency Checking

**Approach:** Verify that retrieved documents are mutually consistent and logically coherent.

**Key frameworks:**

#### ReliabilityRAG (2025–2026)
- Constructs a **contradiction graph** where documents are nodes and edges represent logical contradictions.
- Uses a **Maximum Independent Set (MIS)** algorithm to select the largest set of non-contradicting documents.
- Provides **provable robustness guarantees** — can formally bound the number of poisoned documents the system can tolerate.

#### Self-RAG / Critique Cycles
- After generation, a second LLM pass evaluates whether the response is consistent with the retrieved context.
- Can detect when the model has been "steered" by a single influential poisoned document.

**Key metric:** How many poisoned documents can the system tolerate before its output is compromised?

---

### 4.4 Source Verification

**Approach:** Track and validate the provenance of every document in the knowledge base.

**Techniques:**
1. **Metadata tagging:** Every chunk tagged with source URL, author, timestamp, trust level, ingestion method.
2. **Document hashing:** Cryptographic hashes to detect tampering after ingestion.
3. **Source reputation scoring:** Weight retrieval results by source trustworthiness (e.g., official docs > user-uploaded > web-scraped).
4. **Access control (RBAC/ABAC):** Restrict which documents can be retrieved based on user identity and document classification.

**Limitation:** Doesn't help when the attacker compromises a trusted source or when the knowledge base inherently includes untrusted sources (e.g., web crawls).

---

### 4.5 Retrieval-Time Defenses

**Approach:** Apply defense mechanisms at query time rather than at ingestion time.

#### RAGuard's Two-Layer Defense
1. **Adversarial Retriever Training:** Fine-tune the dense retriever on synthetic poisoned documents (fabricated facts, reasoning traps) so it learns to **downrank** malicious content.
2. **Zero-Knowledge Inference Patch (ZKIP):** For each document in the retrieved set, measure the "semantic shift" and output-entropy change when that document is removed. Documents that cause large shifts are flagged as suspicious.

#### RevPRAG's Activation Analysis
- Monitor LLM internal activations during generation.
- Poisoned responses trigger **distinct activation patterns** compared to legitimate grounded responses.
- **98% True Positive Rate, ~1% False Positive Rate** — but carries latency cost.

#### Hybrid Retrieval
- Use both **vector-based** (dense) and **keyword-based** (BM25) retrieval simultaneously.
- Harder for attackers to optimize poisoned documents against both representations simultaneously.
- Simple to implement; meaningful robustness improvement.

---

## 5. Research Gaps — Opportunities for Your BTP

### Gap Analysis Table

| Gap | Why It Matters | Feasibility (6 months) | Novelty |
|-----|---------------|----------------------|---------|
| **Embedding-space anomaly detection for text RAG** | Most anomaly detection work is on images/tabular; text embedding anomaly detection is under-explored | ⭐⭐⭐⭐⭐ High | ⭐⭐⭐⭐ High |
| **Lightweight retrieval-time filtering** | Current defenses (ZKIP, RevPRAG) are computationally expensive; need low-latency alternatives | ⭐⭐⭐⭐ High | ⭐⭐⭐ Medium |
| **Cross-encoder based poison detection** | Using cross-encoder rerankers as a secondary verification stage to detect inconsistencies | ⭐⭐⭐⭐ High | ⭐⭐⭐⭐ High |
| **Multi-signal ensemble defense** | Combining multiple cheap signals (embedding stats + perplexity + BM25 disagreement) into an ensemble detector | ⭐⭐⭐⭐⭐ High | ⭐⭐⭐⭐ High |
| **Domain-specific poisoning analysis** | Most work is on open-domain QA; targeted analysis for specific domains (medical, legal, code) | ⭐⭐⭐⭐ High | ⭐⭐⭐ Medium |
| **Adaptive attacks against new defenses** | Testing whether PoisonedRAG-style attacks can be modified to evade specific defenses | ⭐⭐⭐ Medium | ⭐⭐⭐⭐ High |
| **Hybrid BM25+dense disagreement as a poisoning signal** | If BM25 and dense retrieval disagree strongly on a document, it may be adversarially optimized | ⭐⭐⭐⭐⭐ High | ⭐⭐⭐⭐⭐ Very High |

> [!IMPORTANT]
> **Top recommendation:** The **"BM25-Dense Disagreement"** signal is highly novel, extremely cheap to compute, and has not been formally studied as a poisoning detector. A paper evaluating this signal alone could be publishable.

---

## 6. Realistic System Architecture

```
┌─────────────────────────────────────────────────────────────────────┐
│                    SECURE RAG PIPELINE                              │
├─────────────────────────────────────────────────────────────────────┤
│                                                                     │
│  ┌──────────────────────────────────────────────────┐              │
│  │           INGESTION LAYER (Offline)               │              │
│  │                                                    │              │
│  │  Raw Documents                                     │              │
│  │       │                                            │              │
│  │       ▼                                            │              │
│  │  [Format Sanitizer] ── strip hidden chars, HTML    │              │
│  │       │                                            │              │
│  │       ▼                                            │              │
│  │  [Text Chunker] ── RecursiveCharacterTextSplitter  │              │
│  │       │                                            │              │
│  │       ▼                                            │              │
│  │  [Metadata Tagger] ── source, timestamp, hash      │              │
│  │       │                                            │              │
│  │       ▼                                            │              │
│  │  [Embedding Model] ── all-MiniLM-L6-v2 (HF)       │              │
│  │       │                    or                      │              │
│  │       │               bge-base-en-v1.5 (HF)       │              │
│  │       ▼                                            │              │
│  │  ┌─────────────────────┐                          │              │
│  │  │   ANOMALY DETECTOR  │◄── YOUR CONTRIBUTION     │              │
│  │  │  (Embedding Stats)  │                          │              │
│  │  └────────┬────────────┘                          │              │
│  │           │ Pass / Quarantine                      │              │
│  │           ▼                                        │              │
│  │  [ChromaDB / FAISS Vector Store]                   │              │
│  │  + [BM25 Index (Elasticsearch / rank-bm25)]        │              │
│  └──────────────────────────────────────────────────┘              │
│                                                                     │
│  ┌──────────────────────────────────────────────────┐              │
│  │           RETRIEVAL LAYER (Online)                │              │
│  │                                                    │              │
│  │  User Query                                        │              │
│  │       │                                            │              │
│  │       ├──► Dense Retrieval (FAISS/ChromaDB)        │              │
│  │       │         Top-k₁ results                     │              │
│  │       │                                            │              │
│  │       └──► Sparse Retrieval (BM25)                 │              │
│  │                 Top-k₂ results                     │              │
│  │                                                    │              │
│  │  ┌─────────────────────────────┐                  │              │
│  │  │   DISAGREEMENT DETECTOR    │◄── YOUR           │              │
│  │  │  (Dense vs BM25 overlap)   │    CONTRIBUTION   │              │
│  │  │  + Consistency Scorer      │                   │              │
│  │  └────────┬────────────────────┘                  │              │
│  │           │                                        │              │
│  │           ▼                                        │              │
│  │  [Cross-Encoder Reranker] ── ms-marco-MiniLM-L6   │              │
│  │       │                                            │              │
│  │       ▼                                            │              │
│  │  Filtered Top-k documents                          │              │
│  └──────────────────────────────────────────────────┘              │
│                                                                     │
│  ┌──────────────────────────────────────────────────┐              │
│  │           GENERATION LAYER                        │              │
│  │                                                    │              │
│  │  System Prompt + Filtered Context + User Query     │              │
│  │       │                                            │              │
│  │       ▼                                            │              │
│  │  [Open-Source LLM]                                 │              │
│  │    • Mistral-7B-Instruct                           │              │
│  │    • Llama-3-8B-Instruct                           │              │
│  │    • Phi-3-mini-4k-instruct                        │              │
│  │       │                                            │              │
│  │       ▼                                            │              │
│  │  Generated Response                                │              │
│  └──────────────────────────────────────────────────┘              │
│                                                                     │
│  ┌──────────────────────────────────────────────────┐              │
│  │           EVALUATION MODULE                       │              │
│  │                                                    │              │
│  │  • Attack Success Rate (ASR)                       │              │
│  │  • Detection Rate (DR)                             │              │
│  │  • False Positive Rate (FPR)                       │              │
│  │  • Retrieval Accuracy (R@k, MRR)                   │              │
│  │  • Answer Quality (F1, Exact Match, BERTScore)     │              │
│  │  • Latency overhead                                │              │
│  └──────────────────────────────────────────────────┘              │
└─────────────────────────────────────────────────────────────────────┘
```

### Recommended Technology Stack

| Component | Recommended Tool | Why |
|-----------|-----------------|-----|
| **Vector Store** | ChromaDB (primary) + FAISS (comparison) | ChromaDB: easy API, metadata filtering, persistence. FAISS: blazing fast, industry standard |
| **Embedding Models** | `sentence-transformers/all-MiniLM-L6-v2` or `BAAI/bge-base-en-v1.5` | Free, well-benchmarked, runs on consumer GPU |
| **Sparse Retrieval** | `rank-bm25` (Python) or Elasticsearch | For the hybrid retrieval / disagreement detection |
| **Cross-Encoder** | `cross-encoder/ms-marco-MiniLM-L-6-v2` | Lightweight reranker; can serve as secondary verification |
| **LLM** | `mistralai/Mistral-7B-Instruct-v0.3` or `meta-llama/Llama-3-8B-Instruct` | Runs on single GPU (16GB+); strong instruction following |
| **RAG Framework** | LangChain or LlamaIndex | Mature, extensible, great community support |
| **Orchestration** | Python + FastAPI | For building the defense pipeline as a service |
| **Experiment Tracking** | Weights & Biases (free tier) or MLflow | Track all experiments systematically |

---

## 7. Datasets & Evaluation Benchmarks

### Existing Datasets for RAG Poisoning Research

| Dataset | Description | How It's Used in Poisoning Research | Source |
|---------|-------------|-------------------------------------|--------|
| **Natural Questions (NQ)** | Google's real search queries + Wikipedia answers | Standard corpus for PoisonedRAG evaluations | Google |
| **TriviaQA** | Question-answer-evidence triples from trivia | Multi-evidence retrieval; tests reasoning under conflict | Joshi et al. |
| **HotpotQA** | Multi-hop QA requiring reasoning across documents | Tests poisoning in complex reasoning chains | Yang et al. |
| **MS MARCO** | Bing search queries + web passages | Standard retrieval benchmarking | Microsoft |
| **SQuAD 2.0** | Wikipedia reading comprehension | Tests answerable vs. unanswerable under poisoning | Rajpurkar et al. |

### Creating Your Own Evaluation Benchmark

Here's a practical methodology for creating a RAG poisoning benchmark:

#### Step 1: Clean Baseline
```
1. Select 500-1000 QA pairs from NQ or HotpotQA
2. Build a clean vector store from Wikipedia passages
3. Measure baseline: Retrieval Accuracy, Answer Quality (F1, EM)
```

#### Step 2: Attack Simulation
```
For each attack type:
  1. Knowledge Corruption: Use PoisonedRAG's optimization to generate 
     poisoned docs (their code is on GitHub)
  2. Naive IPI: Inject documents with "ignore previous instructions" patterns
  3. Semantic IPI: Craft documents with plausible-looking false information
  4. Blocker docs: Generate refusal-inducing content per "Machine Against the RAG"

Vary: poison ratio (0.01% to 1%), number of target questions (10, 50, 100, all)
```

#### Step 3: Defense Evaluation
```
For each defense configuration:
  1. Run the full RAG pipeline with poisoned + clean documents
  2. Measure all metrics with and without defenses active
  3. Report: Detection Rate, FPR, ASR reduction, Retrieval degradation, Latency
```

### Synthetic Poisoned Document Generation

You can create your own poisoned documents using these methods:

1. **LLM-generated contradictions:** "Given fact X, generate a plausible-sounding document asserting the opposite"
2. **Paraphrased poisons:** Take correct documents, have an LLM paraphrase them while changing key facts
3. **Embedding-targeted injection:** Generate text, embed it, measure similarity to target queries, iterate

---

## 8. Evaluation Metrics — Formal Definitions

### 8.1 Attack Success Rate (ASR)

$$ASR = \frac{\text{Number of queries where LLM outputs attacker's target answer}}{\text{Total number of targeted queries}}$$

**Interpretation:** Higher ASR = more effective attack. A good defense should bring ASR from ~90% (PoisonedRAG baseline) to <10%.

### 8.2 Detection Rate (True Positive Rate / Recall)

$$DR = TPR = \frac{\text{Poisoned documents correctly identified as poisoned}}{\text{Total poisoned documents in the database}}$$

**Target:** DR > 85% is a strong result; DR > 95% is excellent.

### 8.3 False Positive Rate (FPR)

$$FPR = \frac{\text{Clean documents incorrectly flagged as poisoned}}{\text{Total clean documents in the database}}$$

**Target:** FPR < 5% is acceptable; FPR < 1% is excellent. High FPR degrades system utility.

### 8.4 Retrieval Accuracy

Multiple sub-metrics:

- **Recall@k:** Fraction of relevant documents appearing in top-k results
- **Precision@k:** Fraction of top-k results that are relevant
- **MRR (Mean Reciprocal Rank):** Average of 1/rank of first relevant result
- **Retrieval Success Rate (RSR):** Fraction of queries where at least one poisoned doc appears in top-k (attack metric)

**Key trade-off:** Defense should reduce RSR (fewer poisons retrieved) without significantly hurting Recall@k for clean documents.

### 8.5 Answer Quality

| Metric | Formula | Use Case |
|--------|---------|----------|
| **Exact Match (EM)** | 1 if prediction exactly matches ground truth, 0 otherwise | Short factual answers |
| **F1 Score** | Token-level harmonic mean of precision and recall against ground truth | Partial credit for overlapping answers |
| **BERTScore** | Cosine similarity of BERT embeddings between prediction and reference | Semantic equivalence |
| **Faithfulness** | Fraction of claims in the answer that are supported by retrieved context | Groundedness check |
| **Answer Relevancy** | Cosine similarity between answer embedding and query embedding | Checks if answer addresses the query |

### 8.6 Additional Metrics to Report

| Metric | Why It Matters |
|--------|---------------|
| **Latency overhead** | Defense must be fast enough for real-time use; report ms/query added |
| **Poison tolerance threshold** | Maximum % of poisoned docs the defense can handle before ASR > 50% |
| **AUC-ROC** | For detection: area under ROC curve across different thresholds |
| **Defense-aware ASR** | ASR when attacker knows about the defense and adapts (adaptive attack) |

---

## 9. Honest Assessment: Is This Suitable for a BTP + Publication?

### Suitability for BTP: ✅ **YES — Excellent choice**

**Strengths:**
1. **Timely and hot topic** — RAG security is the most active sub-area in AI security right now (2025–2026). Reviewers are actively looking for contributions.
2. **Clear scope** — The attack–defense paradigm provides natural structure for a thesis. You attack, then you defend, then you evaluate.
3. **Reproducible** — PoisonedRAG and other attack code is open-source. Standard datasets (NQ, TriviaQA) are available.
4. **Runs on modest hardware** — A single GPU (or even CPU for smaller models) is sufficient for embedding-level experiments.
5. **Strong narrative** — "We found RAG systems are vulnerable → existing defenses don't work → here's a better one" is a compelling story.

**Risks to manage:**
1. **Computational cost:** Full LLM experiments (Mistral-7B, Llama-3-8B) need GPU access. Your college lab or Google Colab Pro ($10/month) should suffice.
2. **Novelty bar:** Top venues (USENIX, CCS) are extremely competitive. A workshop paper or a Tier-2 venue is more realistic for a BTP.
3. **Evaluation rigor:** You need comprehensive experiments. Plan for 2-3 months of experiment time.

### Publication Feasibility: ✅ **Realistic, with the right target**

| Venue Tier | Examples | Feasibility | What You'd Need |
|------------|---------|-------------|-----------------|
| **Top-tier security** | USENIX Security, CCS, S&P | ⭐ Very Hard | Novel attack OR novel defense with formal guarantees |
| **Top-tier ML** | NeurIPS, ICML, ICLR | ⭐⭐ Hard | Theoretical contribution + comprehensive experiments |
| **Mid-tier NLP/AI** | EMNLP, ACL (findings), AAAI | ⭐⭐⭐ Achievable | Strong empirical study with a clear contribution |
| **Workshops** | AISec@CCS, SaTML, TrustNLP@NAACL | ⭐⭐⭐⭐ Very Achievable | Solid experimental evaluation of a new defense idea |
| **Indian conferences** | COMSNETS, ICIT, ISEC | ⭐⭐⭐⭐⭐ Very Achievable | Well-executed study with clear methodology |
| **Journals** | IEEE Access, JISA, Computers & Security | ⭐⭐⭐⭐ Very Achievable | Comprehensive study with thorough evaluation |

> [!TIP]
> **Realistic publication strategy:** Target **AISec workshop @ ACM CCS** (deadline usually ~August) or **SaTML** (IEEE Conference on Secure and Trustworthy Machine Learning). Both actively seek RAG security work and are receptive to strong empirical contributions.

---

## 10. Narrower Research Questions — Novel and Achievable

### 🏆 Top Recommendation

> **"Detecting RAG Corpus Poisoning via Dense-Sparse Retrieval Disagreement"**

**Core idea:** When a document is retrieved by the dense (vector) retriever but NOT by the sparse (BM25) retriever for the same query, this "disagreement" is a strong signal that the document may have been adversarially optimized for the embedding space.

**Why this is novel:**
- PoisonedRAG and HotFlip-style attacks optimize for embedding similarity, NOT keyword overlap.
- BM25 acts as a natural "second opinion" that is fundamentally different from dense retrieval.
- Nobody has formally studied this disagreement as a detection signal.

**Why this is achievable:**
- Requires no model training — purely based on retrieval analysis.
- BM25 + dense retrieval are standard, easy to implement.
- Clear experimental protocol: inject poisons → measure disagreement → evaluate detection.

**Expected output:** A paper showing that Dense-Sparse Disagreement Score achieves X% detection rate with Y% FPR, with comparison against perplexity filtering, embedding outlier detection, and RAGuard.

---

### Alternative Focused Questions (ranked by novelty × feasibility):

| # | Research Question | Novelty | Feasibility | Notes |
|---|------------------|---------|-------------|-------|
| 1 | Dense-Sparse Disagreement as poisoning signal (above) | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ | **Top pick** |
| 2 | "Can cross-encoder rerankers serve as poisoning detectors?" — Score gap between bi-encoder and cross-encoder as anomaly signal | ⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ | Very implementable |
| 3 | "How does chunking strategy affect poisoning resilience?" — Compare fixed, semantic, and sentence-based chunking against PoisonedRAG | ⭐⭐⭐ | ⭐⭐⭐⭐⭐ | Practical contribution |
| 4 | "Ensemble defense for RAG: combining cheap signals" — Perplexity + embedding outlier + BM25 disagreement as a voting ensemble | ⭐⭐⭐⭐ | ⭐⭐⭐⭐ | Strong paper potential |
| 5 | "Retrieval diversity as a defense: can MMR-based retrieval resist poisoning?" — Test if Maximum Marginal Relevance reduces ASR | ⭐⭐⭐ | ⭐⭐⭐⭐⭐ | Quick experiment |

---

## Suggested 6-Month Timeline

| Month | Phase | Deliverables |
|-------|-------|-------------|
| **Month 1** | Literature review + environment setup | Reading list complete; RAG pipeline running; PoisonedRAG attack reproduced |
| **Month 2** | Implement baseline attacks | Working PoisonedRAG, naive IPI, blocker doc attacks on NQ/HotpotQA |
| **Month 3** | Implement defense mechanisms | Dense-Sparse Disagreement detector + 2 baseline defenses implemented |
| **Month 4** | Comprehensive experiments | Full evaluation matrix: 3 attacks × 3 defenses × 3 datasets × multiple poison ratios |
| **Month 5** | Analysis + paper writing | Results tables, figures, statistical significance tests; first paper draft |
| **Month 6** | Polish + submit | Final paper; thesis document; presentation preparation |

> [!CAUTION]
> **Common BTP mistake:** Spending 4 months building and 2 months rushing experiments/writing. Flip it: finish implementation by Month 3 and spend 3 months on rigorous evaluation and writing. **The experiments and analysis ARE the contribution**, not the code.
