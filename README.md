# Production Grade RAG Pipeline

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

3. Solution: Intelligent Document Chunking

To solve this problem, this system introduces:

Parent-Child Chunking

Sliding Window Chunking

These strategies help maintain document structure and context.

4. Parent-Child Chunking

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



<img width="196" height="299" alt="image" src="https://github.com/user-attachments/assets/c8932bc1-1700-4f3e-a54e-c064ea4f0e39" />





