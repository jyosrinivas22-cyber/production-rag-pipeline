# Production Grade RAG Pipeline

## Overview

This project implements a **Production-Grade Retrieval Augmented Generation (RAG) Pipeline** with advanced document chunking strategies and caching mechanisms.

Traditional RAG systems rely on fixed-size chunking which may break the relationship between document sections and paragraphs. This implementation improves context preservation and retrieval accuracy.

---

## Problem Statement

Traditional RAG pipelines split documents into fixed-size chunks.

This causes:

- Loss of document context
- Retrieval of incomplete fragments
- Lower quality LLM responses

To solve this, this project implements **intelligent document chunking strategies**.

---

# Intelligent Document Chunking

## Parent–Child Chunking

Parent–Child Chunking divides documents into two levels:

**Parent Chunks**
Large sections of a document that preserve context.

**Child Chunks**
Smaller segments used for vector similarity search.

Retrieval happens on **child chunks**, while the **parent chunk is passed to the LLM**.

### Flow

## RAG Pipeline Architecture

+---------------------------+
|      Source Documents     |
|      (PDF / Text Data)    |
+---------------------------+
              |
              v
+---------------------------+
|     Document Ingestion    |
|  Load and preprocess data |
+---------------------------+
              |
              v
+---------------------------+
|     Parent Chunking       |
|  Create large sections    |
|  to preserve context      |
+---------------------------+
              |
              v
+---------------------------+
|      Child Chunking       |
|  Smaller chunks used for  |
|  similarity retrieval     |
+---------------------------+
              |
              v
+---------------------------+
|  Sliding Window Chunking  |
| Overlapping chunks ensure |
| context continuity        |
+---------------------------+
              |
              v
+---------------------------+
|   Embedding Generation    |
| Convert text → vectors    |
+---------------------------+
              |
              v
+---------------------------+
|      Vector Database      |
| Store embeddings for      |
| similarity search         |
+---------------------------+
              |
              v
+---------------------------+
|        User Query         |
+---------------------------+
              |
              v
+---------------------------+
|      Query Embedding      |
+---------------------------+
              |
              v
+---------------------------+
|     Similarity Search     |
| Retrieve relevant chunks  |
+---------------------------+
              |
              v
+---------------------------+
|   Retrieve Parent Chunk   |
| Provide full context      |
+---------------------------+
              |
              v
+---------------------------+
|      Multi-Tier Cache     |
| Query Cache + Retrieval   |
+---------------------------+
              |
              v
+---------------------------+
|       LLM Generation      |
| Generate final response   |
+---------------------------+
              |
              v
+---------------------------+
|        Final Answer       |
+---------------------------+

## Sliding Window Chunking

Sliding Window Chunking creates overlapping chunks.

Example:

Chunk 1 → Sentence 1, Sentence 2, Sentence 3  
Chunk 2 → Sentence 2, Sentence 3, Sentence 4  
Chunk 3 → Sentence 3, Sentence 4, Sentence 5  

This overlap preserves context between chunks.

---

# Multi-Tier Caching

To reduce redundant LLM calls, this pipeline implements caching.

### Query Cache
Stores previously asked queries and responses.

### Retrieval Cache
Stores retrieved document chunks.

### Benefits

- Faster responses
- Reduced API cost
- Lower latency

---

# Architecture Flow

## System Architecture Flow

+----------------------------+
|      Source Documents      |
|      (PDF / Text Files)    |
+----------------------------+
              |
              v
+----------------------------+
|     Document Ingestion     |
|  Load & preprocess text    |
+----------------------------+
              |
              v
+----------------------------+
|     Parent Chunking        |
|  Large contextual chunks   |
+----------------------------+
              |
              v
+----------------------------+
|      Child Chunking        |
|  Smaller searchable units  |
+----------------------------+
              |
              v
+----------------------------+
|  Sliding Window Chunking   |
|  Overlapping text segments |
+----------------------------+
              |
              v
+----------------------------+
|   Embedding Generation     |
|  Convert text to vectors   |
+----------------------------+
              |
              v
+----------------------------+
|     Vector Database        |
|  Store embeddings (index)  |
+----------------------------+
              |
              v
+----------------------------+
|        User Query          |
+----------------------------+
              |
              v
+----------------------------+
|     Query Embedding        |
+----------------------------+
              |
              v
+----------------------------+
|     Similarity Search      |
|   Retrieve child chunks    |
+----------------------------+
              |
              v
+----------------------------+
|   Retrieve Parent Context  |
+----------------------------+
              |
              v
+----------------------------+
|     Multi-Tier Cache       |
| Query Cache / Retrieval    |
+----------------------------+
              |
              v
+----------------------------+
|      LLM Generation        |
|   Generate final answer    |
+----------------------------+
              |
              v
+----------------------------+
|        Final Response      |
+----------------------------+

---

#

# Project Structure

production-rag-pipeline  
│  
├── README.md  
├── main.py  
├── chunking.py  
├── retriever.py  
├── cache.py  
├── requirements.txt  
└── data/sample.pdf

