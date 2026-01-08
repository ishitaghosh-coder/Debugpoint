import os
from qdrant_client import QdrantClient
from ollama import Client as OllamaClient

class MultimodalEngine:
    def __init__(self):
        self.qdrant = QdrantClient(url=os.getenv("QDRANT_HOST", "http://qdrant:6333"))
        self.ollama = OllamaClient(host=os.getenv("OLLAMA_HOST", "http://ollama:11434"))
        self.model = "gemma3:4b" # Lightweight multimodal model [cite: 20]

    def unified_retrieval(self, query: str):
        """Unified Cross-Modal Retrieval [cite: 11]"""
        results = self.qdrant.search(
            collection_name="knowledge_base",
            query_text=query,
            limit=5
        )
        
        # Adaptive Retrieval Loop 
        avg_score = sum([r.score for r in results]) / len(results) if results else 0
        if avg_score < 0.65:
            # Trigger expanded search if confidence is low [cite: 15]
            results = self.qdrant.search(
                collection_name="knowledge_base",
                query_text=query,
                limit=10
            )
        return results, avg_score

    def analyze_conflicts(self, evidence):
        """Conflict Detection & Presentation """
        prompt = f"""Compare these sources for contradictions. 
        If text data contradicts image data (scans/diagrams), list them explicitly.
        Sources: {evidence}"""
        
        response = self.ollama.generate(model=self.model, prompt=prompt)
        return response['response']

    def generate_grounded_answer(self, query):
        evidence, score = self.unified_retrieval(query)
        
        # Hallucination Suppression: Refuse if no evidence 
        if score < 0.4:
            return "Insufficient evidence found to answer this query responsibly.", []

        conflicts = self.analyze_conflicts(evidence)
        
        # Evidence-Based Generation with Citations [cite: 13, 14]
        final_prompt = f"Query: {query}\nEvidence: {evidence}\nConflicts: {conflicts}\nAnswer with citations."
        answer = self.ollama.generate(model=self.model, prompt=final_prompt)
        
        return answer['response'], evidence