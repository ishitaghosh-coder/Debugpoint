# 🛡️ CHAKRAVYUH 1.0: Multimodal RAG System
**Problem Statement ID:** GITACVPS004  
**Team Name:** Debugpoint

## 📌 Overview
[cite_start]This system is a robust Multimodal Retrieval-Augmented Generation (RAG) pipeline designed to ingest, store, and reason across heterogeneous data sources including Text (PDF), Images (Scans/Diagrams), and Audio (WAV)[cite: 23, 24, 27]. 

[cite_start]Unlike standard chatbots, this system prioritizes **integrity over superficial quality**, explicitly acknowledging data gaps and contradictions[cite: 13, 65].

## 🏗️ System Architecture
[cite_start]The architecture is modular and non-monolithic to ensure failure-tolerant operation[cite: 44, 49].



### Key Components:
1. [cite_start]**Unified Multimodal Storage**: All formats are mapped into a single knowledge representation in Qdrant, preventing format silos[cite: 28, 29].
2. [cite_start]**Intent-Aware Controller**: Analyzes user queries to determine which modalities are relevant, adjusting retrieval depth accordingly[cite: 32, 33].
3. [cite_start]**Adaptive Retrieval Loop**: If initial evidence is low-confidence, the system automatically triggers additional search cycles with justification[cite: 40, 41].

## 🧠 Reasoning & Safety Strategy
### 1. Conflict Detection (Requirement 7)
[cite_start]When sources contradict each other (e.g., a PDF text vs. a diagram), the system detects the discrepancy and presents multiple interpretations instead of a single, potentially false answer[cite: 38, 39].

### 2. Uncertainty Awareness (Requirement 6)
[cite_start]The system distinguishes between verified facts and inferred assumptions, explicitly flagging results that rely on low-quality or noisy evidence[cite: 36, 37].

### 3. Hallucination Suppression (Requirement 9)
[cite_start]If adequate evidence is unavailable across all modalities, the system is programmed to refuse the answer and state exactly what information is missing[cite: 42, 43].

## 🚀 Getting Started
### Prerequisites
- Docker & Docker Compose
- Local Ollama instance (Gemma 3 or Phi-4)

### Installation
1. Clone the repository:
   ```bash
   git clone [https://github.com/ishitaghosh-coder/Debugpoint.git](https://github.com/ishitaghosh-coder/Debugpoint.git)