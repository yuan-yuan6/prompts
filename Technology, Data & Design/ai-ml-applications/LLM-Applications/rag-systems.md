---
category: ai-ml-applications/LLM-Applications
last_updated: 2025-11-12
title: RAG (Retrieval Augmented Generation) Systems
tags:
- ai-ml
- llm
- rag
- vector-search
- knowledge-base
use_cases:
- Building AI systems that answer questions from private knowledge bases
- Creating chatbots with access to company documentation
- Developing intelligent search and Q&A over large document collections
- Reducing LLM hallucinations with source-grounded responses
related_templates:
- ai-ml-applications/LLM-Applications/llm-application-development.md
- ai-ml-applications/LLM-Applications/prompt-engineering-workflows.md
- ai-ml-applications/AI-Product-Development/ai-data-strategy.md
industries:
- technology
- finance
- healthcare
- retail
- manufacturing
type: template
difficulty: intermediate
slug: rag-systems
---

# RAG (Retrieval Augmented Generation) Systems Template

## Purpose
Build production-ready RAG systems that combine vector search with LLMs to provide accurate, source-grounded answers from your private knowledge base while minimizing hallucinations.

## Quick Start

**Need to build a RAG system quickly?** Use this streamlined approach:

### Minimal Example
```python
# Simple RAG implementation
from anthropic import Anthropic
import chromadb

# 1. Setup vector DB
client = chromadb.Client()
collection = client.create_collection("docs")

# 2. Index documents
docs = ["Doc 1 content...", "Doc 2 content...", "Doc 3 content..."]
collection.add(documents=docs, ids=["1", "2", "3"])

# 3. RAG query function
def rag_query(question: str) -> str:
    # Retrieve relevant docs
    results = collection.query(query_texts=[question], n_results=3)
    context = "\n\n".join(results["documents"][0])

    # Generate answer with context
    llm = Anthropic()
    response = llm.messages.create(
        model="claude-sonnet-4-5-20250929",
        max_tokens=1024,
        messages=[{
            "role": "user",
            "content": f"""Answer this question based on the context provided.

Context:
{context}

Question: {question}

Answer based only on the context. If the answer isn't in the context, say so."""
        }]
    )
    return response.content[0].text

# Use it
answer = rag_query("What is the refund policy?")
```

### When to Use This
- Building Q&A systems over internal documentation
- Creating customer support chatbots with knowledge bases
- Developing AI assistants for specialized domains (legal, medical, technical)
- Enabling semantic search over large document collections
- Reducing hallucinations with source-grounded generation

### Basic 5-Step Workflow
1. **Prepare Data** - Collect, clean, and chunk your documents
2. **Create Embeddings** - Generate vector embeddings and index them
3. **Implement Retrieval** - Build semantic search to find relevant content
4. **Generate Answers** - Use LLM to synthesize answers from retrieved context
5. **Iterate & Improve** - Optimize retrieval quality and answer accuracy

---

## Template

```
You are an expert in building Retrieval Augmented Generation (RAG) systems. Help me design and implement a RAG system for [USE_CASE] using [DATA_SOURCES] to answer [QUERY_TYPES] for [USERS] with [QUALITY_REQUIREMENTS].

SYSTEM CONTEXT:
Project Overview:
- System name: [SYSTEM_NAME]
- Primary use case: [USE_CASE]
- Users: [USER_TYPE_AND_COUNT]
- Query volume: [QUERIES_PER_DAY]
- Quality target: [ACCURACY_REQUIREMENTS]
- Latency target: [MAX_RESPONSE_TIME]

Data Sources:
- Document types: [PDF/MARKDOWN/HTML/DATABASE/API]
- Document count: [NUMBER_OF_DOCUMENTS]
- Total size: [DATA_SIZE]
- Update frequency: [HOW_OFTEN_DATA_CHANGES]
- Languages: [LANGUAGES]
- Structure: [STRUCTURED/UNSTRUCTURED/MIXED]

Technical Stack:
- LLM: [CLAUDE/GPT4/GEMINI/OTHER]
- Embedding model: [EMBEDDING_MODEL]
- Vector database: [PINECONE/WEAVIATE/CHROMA/PGVECTOR]
- Backend: [PYTHON/NODE/OTHER]
- Infrastructure: [CLOUD_PROVIDER]

### 1. DATA PREPARATION

Document Collection:
- Sources: [LIST_ALL_DATA_SOURCES]
  - Internal docs: [CONFLUENCE/NOTION/SHAREPOINT]
  - Support tickets: [ZENDESK/INTERCOM]
  - Knowledge base: [EXISTING_KB]
  - Product docs: [TECHNICAL_DOCUMENTATION]
  - Other: [ADDITIONAL_SOURCES]

Data Cleaning:
```python
def clean_document(doc: str) -> str:
    """Clean and normalize documents"""
    # Remove noise
    doc = remove_headers_footers(doc)
    doc = remove_boilerplate(doc)

    # Normalize formatting
    doc = normalize_whitespace(doc)
    doc = fix_encoding_issues(doc)

    # Extract text from special formats
    if is_table(doc):
        doc = table_to_markdown(doc)

    return doc
```

Document Chunking Strategy:
```python
def chunk_document(doc: str, method: str = "semantic") -> list[str]:
    """
    Split documents into optimal chunks for retrieval

    Methods:
    - fixed: Fixed size chunks (e.g., 512 tokens)
    - semantic: Split on semantic boundaries (paragraphs, sections)
    - hybrid: Combine both approaches
    """

    if method == "fixed":
        # Simple fixed-size chunks
        chunk_size = 512  # tokens
        overlap = 50      # token overlap between chunks
        return fixed_size_chunks(doc, chunk_size, overlap)

    elif method == "semantic":
        # Split on semantic boundaries
        sections = split_on_headers(doc)
        chunks = []
        for section in sections:
            # Further split long sections
            if len(section) > MAX_SECTION_LENGTH:
                chunks.extend(split_paragraphs(section))
            else:
                chunks.append(section)
        return chunks

    elif method == "hybrid":
        # Semantic split first, then size-constrain
        semantic_chunks = semantic_chunking(doc)
        final_chunks = []
        for chunk in semantic_chunks:
            if len(chunk) > MAX_CHUNK_SIZE:
                final_chunks.extend(
                    fixed_size_chunks(chunk, MAX_CHUNK_SIZE, OVERLAP)
                )
            else:
                final_chunks.append(chunk)
        return final_chunks
```

Chunking Best Practices:
- Chunk size: [OPTIMAL_SIZE_FOR_YOUR_USE_CASE]
  - Typical: 256-512 tokens
  - Longer for technical docs (512-1024)
  - Shorter for chat messages (128-256)
- Overlap: [OVERLAP_SIZE]
  - Typical: 10-20% of chunk size
  - Preserves context across boundaries
- Boundaries: [HOW_TO_DETERMINE_SPLITS]
  - Respect semantic units (paragraphs, sections)
  - Don't split code blocks, tables, lists
  - Preserve headings with their content

Metadata Enrichment:
```python
def enrich_chunk(chunk: str, doc_metadata: dict) -> dict:
    """Add metadata to chunks for better retrieval"""
    return {
        "text": chunk,
        "source_doc": doc_metadata["filename"],
        "doc_type": doc_metadata["type"],  # pdf, markdown, etc.
        "section": extract_section_title(chunk),
        "created_at": doc_metadata["created_at"],
        "updated_at": doc_metadata["updated_at"],
        "author": doc_metadata["author"],
        "tags": doc_metadata["tags"],
        "access_control": doc_metadata["permissions"],
        # Add domain-specific metadata
        "product": doc_metadata.get("product"),
        "version": doc_metadata.get("version"),
    }
```

### 2. EMBEDDING & INDEXING

Embedding Strategy:
```python
from sentence_transformers import SentenceTransformer

# Choose embedding model
# Options:
# - OpenAI text-embedding-3-large (3072 dims)
# - Cohere embed-english-v3.0 (1024 dims)
# - sentence-transformers/all-MiniLM-L6-v2 (384 dims)
# - Voyage AI voyage-2 (1024 dims)

model = SentenceTransformer('[EMBEDDING_MODEL]')

def embed_chunks(chunks: list[dict]) -> list[dict]:
    """Generate embeddings for chunks"""
    texts = [c["text"] for c in chunks]

    # Batch embedding for efficiency
    embeddings = model.encode(
        texts,
        batch_size=32,
        show_progress_bar=True,
        normalize_embeddings=True  # For cosine similarity
    )

    # Attach embeddings to chunks
    for chunk, embedding in zip(chunks, embeddings):
        chunk["embedding"] = embedding.tolist()

    return chunks
```

Vector Database Setup:
```python
# Example: Using Chroma
import chromadb

def setup_vector_db():
    """Initialize vector database"""
    client = chromadb.PersistentClient(path="./chroma_db")

    collection = client.get_or_create_collection(
        name="[COLLECTION_NAME]",
        metadata={
            "description": "[DESCRIPTION]",
            "embedding_model": "[MODEL_NAME]"
        },
        embedding_function=chromadb.utils.embedding_functions.SentenceTransformerEmbeddingFunction(
            model_name="[MODEL_NAME]"
        )
    )

    return collection

def index_documents(collection, chunks: list[dict]):
    """Index chunks in vector database"""
    collection.add(
        documents=[c["text"] for c in chunks],
        metadatas=[{k: v for k, v in c.items() if k != "text"} for c in chunks],
        ids=[c["id"] for c in chunks]
    )
```

Indexing Pipeline:
```python
def build_index(documents: list[str]):
    """Complete indexing pipeline"""

    # 1. Clean documents
    cleaned = [clean_document(doc) for doc in documents]

    # 2. Chunk documents
    chunks = []
    for doc, metadata in zip(cleaned, doc_metadata):
        doc_chunks = chunk_document(doc)
        chunks.extend([
            enrich_chunk(chunk, metadata)
            for chunk in doc_chunks
        ])

    # 3. Generate embeddings
    embedded_chunks = embed_chunks(chunks)

    # 4. Index in vector DB
    collection = setup_vector_db()
    index_documents(collection, embedded_chunks)

    # 5. Create traditional search index (optional)
    create_bm25_index(chunks)  # For hybrid search

    print(f"Indexed {len(chunks)} chunks from {len(documents)} documents")
```

### 3. RETRIEVAL IMPLEMENTATION

Basic Semantic Search:
```python
def semantic_search(
    query: str,
    collection,
    top_k: int = 5
) -> list[dict]:
    """Retrieve relevant chunks using semantic search"""

    results = collection.query(
        query_texts=[query],
        n_results=top_k,
        include=["documents", "metadatas", "distances"]
    )

    return [
        {
            "text": doc,
            "metadata": meta,
            "score": 1 - dist  # Convert distance to similarity
        }
        for doc, meta, dist in zip(
            results["documents"][0],
            results["metadatas"][0],
            results["distances"][0]
        )
    ]
```

Advanced Retrieval Techniques:

**Hybrid Search (Semantic + Keyword):**
```python
def hybrid_search(
    query: str,
    vector_db,
    keyword_index,
    top_k: int = 5,
    alpha: float = 0.7  # Weight for semantic vs keyword
) -> list[dict]:
    """Combine semantic and keyword search"""

    # Semantic search
    semantic_results = semantic_search(query, vector_db, top_k * 2)

    # Keyword search (BM25)
    keyword_results = keyword_index.search(query, top_k * 2)

    # Combine with weighted scoring
    combined = {}
    for result in semantic_results:
        combined[result["id"]] = {
            "chunk": result,
            "score": alpha * result["score"]
        }

    for result in keyword_results:
        if result["id"] in combined:
            combined[result["id"]]["score"] += (1 - alpha) * result["score"]
        else:
            combined[result["id"]] = {
                "chunk": result,
                "score": (1 - alpha) * result["score"]
            }

    # Sort by combined score
    ranked = sorted(
        combined.values(),
        key=lambda x: x["score"],
        reverse=True
    )

    return [r["chunk"] for r in ranked[:top_k]]
```

**Query Expansion:**
```python
def expand_query(query: str, llm) -> list[str]:
    """Generate query variations for better retrieval"""

    prompt = f"""Generate 3 variations of this query that capture the same intent:

Original query: {query}

Provide variations that:
1. Rephrase using different terminology
2. Add relevant context
3. Ask from different angle

Return as JSON array of strings."""

    response = llm.complete(prompt)
    variations = json.loads(response)

    return [query] + variations
```

**Reranking:**
```python
def rerank_results(
    query: str,
    results: list[dict],
    reranker_model
) -> list[dict]:
    """Rerank results using cross-encoder"""

    # Create query-document pairs
    pairs = [[query, r["text"]] for r in results]

    # Score with reranker (more accurate than embedding similarity)
    scores = reranker_model.predict(pairs)

    # Attach scores and sort
    for result, score in zip(results, scores):
        result["rerank_score"] = score

    return sorted(results, key=lambda x: x["rerank_score"], reverse=True)
```

**Metadata Filtering:**
```python
def filtered_search(
    query: str,
    collection,
    filters: dict,
    top_k: int = 5
) -> list[dict]:
    """Search with metadata filters"""

    # Example filters:
    # - product: "Product A"
    # - doc_type: "user_manual"
    # - created_after: "2024-01-01"

    results = collection.query(
        query_texts=[query],
        n_results=top_k,
        where=filters,  # Metadata filters
        include=["documents", "metadatas", "distances"]
    )

    return results
```

### 4. ANSWER GENERATION

RAG Prompt Template:
```python
RAG_SYSTEM_PROMPT = """You are a helpful AI assistant that answers questions based on provided context.

Instructions:
1. Answer the question using ONLY information from the context
2. If the answer isn't in the context, say "I don't have enough information to answer that"
3. Cite sources by referencing the source document
4. If multiple sources have relevant info, synthesize them
5. Be direct and concise
6. Never make up information

Output format:
[Your answer]

Sources: [List of source documents]
"""

def generate_rag_answer(
    query: str,
    retrieved_docs: list[dict],
    llm
) -> dict:
    """Generate answer using retrieved context"""

    # Format context
    context_parts = []
    for i, doc in enumerate(retrieved_docs, 1):
        context_parts.append(
            f"[Source {i}: {doc['metadata']['source_doc']}]\n{doc['text']}"
        )
    context = "\n\n".join(context_parts)

    # Create prompt
    user_prompt = f"""Context:
{context}

Question: {query}

Provide a clear, accurate answer based on the context above."""

    # Generate answer
    response = llm.messages.create(
        model="claude-sonnet-4-5-20250929",
        max_tokens=1024,
        system=RAG_SYSTEM_PROMPT,
        messages=[{"role": "user", "content": user_prompt}]
    )

    answer = response.content[0].text

    return {
        "answer": answer,
        "sources": [doc["metadata"]["source_doc"] for doc in retrieved_docs],
        "retrieved_docs": retrieved_docs
    }
```

Advanced Generation Techniques:

**Citation Generation:**
```python
CITATION_PROMPT = """Answer the question and cite specific sources.

Format your answer with inline citations like this:
"The refund window is 30 days [1]. However, extended warranties have a 90-day window [2]."

Context:
{context}

Question: {query}

Answer with inline citations [1], [2], etc. Then list sources at the end."""
```

**Multi-Step Reasoning:**
```python
def multi_step_rag(query: str, vector_db, llm):
    """Break complex questions into steps"""

    # Step 1: Decompose question
    decomposition = llm.complete(f"""
    Break this complex question into simpler sub-questions:
    {query}

    Return as JSON array of sub-questions.
    """)
    sub_questions = json.loads(decomposition)

    # Step 2: Answer each sub-question
    sub_answers = []
    for sub_q in sub_questions:
        docs = semantic_search(sub_q, vector_db)
        answer = generate_rag_answer(sub_q, docs, llm)
        sub_answers.append(answer)

    # Step 3: Synthesize final answer
    synthesis_prompt = f"""
    Original question: {query}

    Sub-question answers:
    {format_sub_answers(sub_answers)}

    Synthesize a comprehensive answer to the original question.
    """

    final_answer = llm.complete(synthesis_prompt)
    return final_answer
```

**Confidence Scoring:**
```python
def answer_with_confidence(query: str, retrieved_docs: list[dict], llm) -> dict:
    """Generate answer with confidence score"""

    prompt = f"""Answer this question based on the context, and provide a confidence score (0-100).

Context:
{format_context(retrieved_docs)}

Question: {query}

Output format (JSON):
{{
  "answer": "your answer",
  "confidence": 85,
  "reasoning": "why this confidence level",
  "gaps": ["what information is missing, if any"]
}}"""

    response = llm.complete(prompt)
    result = json.loads(response)

    # Adjust confidence based on retrieval quality
    avg_retrieval_score = np.mean([d["score"] for d in retrieved_docs])
    if avg_retrieval_score < 0.7:
        result["confidence"] *= 0.8  # Reduce confidence for poor retrieval

    return result
```

### 5. EVALUATION & OPTIMIZATION

Retrieval Evaluation:
```python
def evaluate_retrieval(test_queries: list[dict]) -> dict:
    """
    Evaluate retrieval quality

    test_queries = [
        {
            "query": "What is the refund policy?",
            "relevant_doc_ids": ["doc_123", "doc_456"]
        },
        ...
    ]
    """

    metrics = {
        "precision": [],
        "recall": [],
        "mrr": [],  # Mean Reciprocal Rank
        "ndcg": []  # Normalized Discounted Cumulative Gain
    }

    for test in test_queries:
        results = semantic_search(test["query"], collection, top_k=10)
        retrieved_ids = [r["metadata"]["id"] for r in results]
        relevant_ids = set(test["relevant_doc_ids"])

        # Precision@k
        retrieved_relevant = set(retrieved_ids[:5]) & relevant_ids
        metrics["precision"].append(len(retrieved_relevant) / 5)

        # Recall
        metrics["recall"].append(len(retrieved_relevant) / len(relevant_ids))

        # MRR
        for i, doc_id in enumerate(retrieved_ids, 1):
            if doc_id in relevant_ids:
                metrics["mrr"].append(1 / i)
                break
        else:
            metrics["mrr"].append(0)

    return {k: np.mean(v) for k, v in metrics.items()}
```

End-to-End Evaluation:
```python
def evaluate_rag_system(test_cases: list[dict]) -> dict:
    """
    Evaluate complete RAG system

    test_cases = [
        {
            "query": "What is the refund policy?",
            "expected_answer": "30-day refund window...",
            "must_cite": ["refund_policy.pdf"]
        },
        ...
    ]
    """

    results = {
        "answer_accuracy": [],
        "citation_accuracy": [],
        "latency": [],
        "hallucination_rate": []
    }

    for test in test_cases:
        start = time.time()

        # Get answer
        docs = semantic_search(test["query"], collection)
        answer_data = generate_rag_answer(test["query"], docs, llm)

        latency = time.time() - start

        # Evaluate answer quality (use LLM-as-judge)
        accuracy = evaluate_answer(
            answer_data["answer"],
            test["expected_answer"]
        )

        # Check citations
        cited_correctly = all(
            source in answer_data["sources"]
            for source in test["must_cite"]
        )

        # Check for hallucinations
        hallucinated = contains_info_not_in_sources(
            answer_data["answer"],
            docs
        )

        results["answer_accuracy"].append(accuracy)
        results["citation_accuracy"].append(int(cited_correctly))
        results["latency"].append(latency)
        results["hallucination_rate"].append(int(hallucinated))

    return {k: np.mean(v) for k, v in results.items()}
```

Optimization Strategies:
- **Chunk size tuning**: Test different chunk sizes on eval set
- **Retrieval tuning**: Adjust top_k, use hybrid search, query expansion
- **Prompt optimization**: Iterate on generation prompts
- **Reranking**: Add reranking step for better precision
- **Caching**: Cache embeddings and common queries

### 6. PRODUCTION DEPLOYMENT

Complete RAG Service:
```python
class RAGService:
    def __init__(self, collection, llm, config):
        self.collection = collection
        self.llm = llm
        self.config = config
        self.cache = {}  # Query cache

    async def query(self, question: str, filters: dict = None) -> dict:
        """Main RAG query endpoint"""

        # Check cache
        cache_key = hash((question, json.dumps(filters or {})))
        if cache_key in self.cache:
            return self.cache[cache_key]

        # Retrieve
        docs = await self.retrieve(question, filters)

        # Check retrieval quality
        if not docs or docs[0]["score"] < self.config["min_score"]:
            return {
                "answer": "I don't have enough information to answer that confidently.",
                "confidence": "low",
                "sources": []
            }

        # Generate
        result = await self.generate(question, docs)

        # Cache result
        self.cache[cache_key] = result

        # Log for monitoring
        self.log_query(question, docs, result)

        return result

    async def retrieve(self, query: str, filters: dict) -> list[dict]:
        """Retrieval with multiple strategies"""

        # Try hybrid search first
        if self.config["use_hybrid_search"]:
            results = hybrid_search(
                query,
                self.collection,
                self.keyword_index,
                top_k=self.config["top_k"]
            )
        else:
            results = semantic_search(
                query,
                self.collection,
                top_k=self.config["top_k"]
            )

        # Rerank if configured
        if self.config["use_reranking"]:
            results = rerank_results(query, results, self.reranker)

        return results

    async def generate(self, query: str, docs: list[dict]) -> dict:
        """Generate answer with safety checks"""

        result = generate_rag_answer(query, docs, self.llm)

        # Safety filtering
        result["answer"] = self.safety_filter(result["answer"])

        # Add confidence score
        result["confidence"] = self.calculate_confidence(docs, result)

        return result
```

Monitoring & Alerts:
```python
# Track key metrics
def log_rag_metrics(query, docs, result, latency):
    metrics = {
        "timestamp": datetime.now(),
        "query": query,
        "retrieval_score": np.mean([d["score"] for d in docs]),
        "num_docs_retrieved": len(docs),
        "answer_length": len(result["answer"]),
        "latency_ms": latency * 1000,
        "confidence": result.get("confidence"),
        "sources_count": len(result["sources"])
    }

    logger.info("rag_query", extra=metrics)

    # Alert on anomalies
    if latency > 5.0:
        alert("High RAG latency", metrics)
    if metrics["retrieval_score"] < 0.5:
        alert("Poor retrieval quality", metrics)
```

Data Updates:
```python
def incremental_update(new_documents: list[str]):
    """Add new documents without full reindex"""

    # Process new docs
    chunks = []
    for doc in new_documents:
        cleaned = clean_document(doc)
        doc_chunks = chunk_document(cleaned)
        chunks.extend(doc_chunks)

    # Generate embeddings
    embedded = embed_chunks(chunks)

    # Add to index
    collection.add(
        documents=[c["text"] for c in embedded],
        metadatas=[c["metadata"] for c in embedded],
        ids=[c["id"] for c in embedded]
    )

    print(f"Added {len(chunks)} new chunks to index")

def scheduled_reindex():
    """Periodic full reindex to maintain quality"""
    # Run weekly or monthly
    # Rebuild entire index from source documents
    # Useful if embedding model or chunking strategy changes
    pass
```
```

## Variables

### USE_CASE
Your specific RAG application use case.
**Examples:**
- "Customer support chatbot answering from help documentation"
- "Internal Q&A system for company policies and procedures"
- "Legal document analysis assistant"
- "Technical documentation search for software developers"

### DATA_SOURCES
Where your knowledge base content comes from.
**Examples:**
- "Confluence wiki (5,000 pages) + Zendesk tickets (50,000)"
- "Product manuals (PDF), API docs (Markdown), support articles (HTML)"
- "Internal reports (Word docs) + presentations (PowerPoint)"
- "Codebase documentation + README files + code comments"

### QUERY_TYPES
The kinds of questions users will ask.
**Examples:**
- "Factual questions about policies and procedures"
- "How-to questions about product features"
- "Troubleshooting questions about errors and issues"
- "Comparison questions (What's the difference between X and Y?)"

## Best Practices

### Data Preparation
1. **Clean thoroughly** - Remove noise, fix formatting, handle special characters
2. **Chunk intelligently** - Respect semantic boundaries, maintain context
3. **Enrich metadata** - Add source, date, author, category for filtering
4. **Test chunking** - Manually review samples to ensure quality
5. **Version your data** - Track what data was indexed when

### Retrieval
1. **Start with semantic, add hybrid** - Semantic search is good, hybrid is better
2. **Tune top_k** - Retrieve more than you need, rerank down
3. **Use metadata filters** - Pre-filter by date, category, access rights
4. **Monitor retrieval quality** - Track whether relevant docs are being found
5. **Handle edge cases** - Empty results, low-confidence retrieval

### Generation
1. **Ground in sources** - Emphasize using only provided context
2. **Enable citations** - Make it easy to verify answers
3. **Admit ignorance** - Better to say "I don't know" than hallucinate
4. **Provide confidence** - Help users gauge answer reliability
5. **Format for readability** - Structure answers clearly

### Production
1. **Cache aggressively** - Similar questions should hit cache
2. **Monitor everything** - Retrieval quality, generation quality, latency
3. **Incremental updates** - Add new docs without full reindex
4. **Access control** - Respect document permissions in retrieval
5. **Cost optimization** - Right-size embeddings and LLM model

## Common Pitfalls

❌ **Chunks too large/small** - Impacts retrieval quality significantly
✅ Instead: Test multiple chunk sizes on eval set, typically 256-512 tokens

❌ **Ignoring metadata** - Losing important document context
✅ Instead: Preserve source, date, author, section for better retrieval and citations

❌ **Only semantic search** - Missing exact keyword matches
✅ Instead: Use hybrid search (semantic + BM25) for better recall

❌ **No reranking** - Top retrieved chunks may not be most relevant
✅ Instead: Add reranking step for better precision

❌ **Hallucination not prevented** - LLM generates info not in sources
✅ Instead: Strong prompt instructions, post-generation verification

❌ **No retrieval threshold** - Answering even when no good matches
✅ Instead: Check retrieval scores, return "I don't know" if too low

❌ **Static knowledge base** - Data gets stale
✅ Instead: Regular updates, clear data freshness indicators

❌ **No evaluation** - Can't tell if changes help or hurt
✅ Instead: Build eval set, measure retrieval and generation quality

## Related Resources

**Vector Databases:**
- Pinecone - Managed vector database
- Weaviate - Open source vector search
- Chroma - Lightweight Python vector DB
- PgVector - Postgres extension

**Frameworks:**
- LangChain - RAG pipelines
- LlamaIndex - Document indexing and retrieval
- Haystack - NLP framework with RAG

**Embedding Models:**
- OpenAI text-embedding-3
- Cohere embed-v3
- Sentence Transformers
- Voyage AI embeddings

**Tools:**
- Unstructured.io - Document parsing
- Ragas - RAG evaluation framework
- LangSmith - RAG debugging

---

**Last Updated:** 2025-11-12
**Category:** AI/ML Applications > LLM Applications
**Difficulty:** Intermediate to Advanced
**Estimated Time:** 2-3 weeks for production-ready system
