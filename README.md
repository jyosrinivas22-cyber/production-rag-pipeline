# Assignment 2: Production-Grade RAG Pipeline with Advanced Chunking & Multi-Tier Caching

Problem-1

## Overview

Retrieval Augmented Generation (RAG) is a system design pattern used to improve Large Language Model (LLM) responses by retrieving relevant information from external documents before generating answers.

Traditional RAG systems rely on fixed-size chunking which may break the relationship between document sections and paragraphs. This implementation improves context preservation and retrieval accuracy.

---

## Problem with Traditional RAG Pipelines

Traditional RAG systems typically split documents into fixed-size chunks.

Example:

Document:

Artificial Intelligence is the science of building intelligent machines.
Machine Learning is a subset of Artificial Intelligence.
Deep Learning is a subset of Machine Learning.

Fixed chunking may create:

Chunk 1
Artificial Intelligence is the science of building intelligent machines.

Chunk 2
Machine Learning is a subset of Artificial Intelligence.

Chunk 3
Deep Learning is a subset of Machine Learning.

If a user asks:

"What is Artificial Intelligence?"

The retriever might only return:

"Machine Learning is a subset of Artificial Intelligence."

The context of the whole section is lost.

This leads to:

incomplete answers

incorrect responses

poor retrieval quality

Solution: Intelligent Document Chunking

To solve this problem, this system introduces:

Parent-Child Chunking

Sliding Window Chunking

These strategies help maintain document structure and context.

Parent-Child Chunking

  Parent-Child Chunking creates a hierarchical relationship between chunks.

Two levels exist:

Parent Chunk
Large section containing complete context.

Child Chunk
Smaller segments used for retrieval.

Example Document:

Artificial Intelligence
AI is the science of building intelligent machines.
Machine Learning is a subset of AI.
Deep Learning is a subset of Machine Learning.

Parent Chunk:

Artificial Intelligence
AI is the science of building intelligent machines.
Machine Learning is a subset of AI.
Deep Learning is a subset of Machine Learning.

Child Chunks:

Child 1
AI is the science of building intelligent machines.

Child 2
Machine Learning is a subset of AI.

Child 3
Deep Learning is a subset of Machine Learning.

Retrieval happens on child chunks, but the system sends the parent chunk to the LLM.

This ensures the model receives the full context.

Additional Chunking Strategy: Sliding Window Chunking

Sliding Window Chunking is a chunking strategy used to preserve context between parts of a document when it is split into smaller segments. Instead of dividing the text into completely separate chunks, this method creates overlapping chunks, where some portion of the previous chunk is included in the next one. This overlap helps maintain the relationship between sentences and ensures that important information near chunk boundaries is not lost. As a result, the retrieval system can find more relevant content during similarity search, and the Large Language Model (LLM) receives better contextual information to generate accurate responses.

Justification for Choosing Sliding Window Chunking

Sliding Window Chunking was selected as an additional chunking strategy because it helps preserve contextual continuity between adjacent chunks of text. In traditional fixed-size chunking, important information may be lost at chunk boundaries, which can reduce retrieval accuracy. Sliding window chunking solves this problem by creating overlapping chunks, where a portion of the previous chunk is included in the next chunk. This overlap ensures that related sentences remain connected across chunks, improving semantic understanding during similarity search. As a result, the retriever can identify more relevant information, and the Large Language Model (LLM) receives richer context for generating accurate responses. When combined with Parent–Child Chunking, this strategy improves both hierarchical context preservation and sequential text continuity, making the RAG pipeline more effective for real-world production systems.

Problem-2

Introduction

In a typical RAG pipeline, every user query triggers a full process including query embedding, vector database retrieval, reranking, and LLM response generation. This can be computationally expensive and slow, especially when users ask similar or repeated queries.

To improve efficiency and reduce unnecessary processing, the system implements a three-tier caching architecture between the user query and the retrieval pipeline. The caching system stores previously processed queries and retrieved information so that repeated queries can be answered quickly without repeating the entire pipeline.

The three caching layers are:

• Tier 1 – Exact Cache
• Tier 2 – Semantic Cache
• Tier 3 – Retrieval Cache
<img width="196" height="299" alt="image" src="https://github.com/user-attachments/assets/c8932bc1-1700-4f3e-a54e-c064ea4f0e39" />

Tier 1 – Exact Cache

The Exact Cache stores previously asked queries along with their responses. When a new query arrives, the system first checks if the exact same query already exists in the cache.

If an exact match is found, the cached response is returned immediately.

Example:

User Query:
What is Artificial Intelligence?

If this query was already asked earlier, the system directly returns the cached answer without performing retrieval or LLM generation.

Benefits:

• Fastest response time
• No vector database search
• No LLM call

Tier 2 – Semantic Cache

If no exact match is found, the system checks the semantic cache. In this layer, the query is converted into an embedding and compared with previously stored query embeddings using cosine similarity.

If the similarity score is above a predefined threshold, the system returns the cached response.

Example:

Previous Query:
What is Artificial Intelligence?

New Query:
Explain Artificial Intelligence.

Although the queries are not identical, they have the same meaning. If the similarity score is high, the cached answer is returned.

Benefits:

• Handles similar queries with different wording
• Reduces redundant retrieval and LLM calls

Tier 3 – Retrieval Cache

If no semantic match is found, the system checks the retrieval cache. This cache stores document chunks that were retrieved previously from the vector database.

If relevant chunks already exist in the cache, the system skips the vector database search and sends the cached chunks directly to the LLM for response generation.

Example:

Query:
Applications of AI in healthcare

If relevant chunks were already retrieved earlier, the system reuses them and directly calls the LLM.

Benefits:

• Reduces vector database queries
• Improves system performance

Full Pipeline Execution

If none of the caching layers contain the query or relevant data, the system executes the complete RAG pipeline.

Steps:

1.Query embedding generation

2. Vector database search

3/ Retrieve relevant document chunks

4. Reranking of retrieved chunks

5. LM response generation

6. Store results in cache for future querie

Example Query Walkthrough

User asks:

What is Machine Learning?

Step 1
System checks exact cache → No match

Step 2
System checks semantic cache → Similar query found

Step 3
System returns cached response without running retrieval or LLM

Justification

The three-tier caching system significantly improves the efficiency of the RAG pipeline by reducing redundant computations. Exact cache handles repeated queries, semantic cache handles similar queries with different wording, and retrieval cache avoids repeated vector database searches. This layered caching strategy improves response time, reduces computational cost, and enhances scalability, making the system suitable for production environments.

-

