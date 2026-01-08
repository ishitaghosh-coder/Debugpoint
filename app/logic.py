from ollama import Client as OllamaClient
import os

class RAGBrain:
    def __init__(self):
        self.ollama = OllamaClient(host=os.getenv("OLLAMA_HOST"))
        self.model = "gemma3:4b" # Resource-constrained choice [cite: 20]

    def adaptive_retrieval(self, query, qdrant_client):
        # Requirement 8: Trigger additional cycles if confidence is low [cite: 17]
        results = qdrant_client.search(collection_name="knowledge_base", query_text=query, limit=3)
        
        if not results or results[0].score < 0.65:
            # Justify further retrieval [cite: 17]
            print("Confidence low. Expanding search scope...")
            results = qdrant_client.search(collection_name="knowledge_base", query_text=query, limit=6)
        
        return results

    def detect_conflicts(self, context):
        # Requirement 7: Present multiple interpretations if sources disagree [cite: 16]
        prompt = f"Analyze these sources for contradictions. If Fact A (Text) disagrees with Fact B (Image), list both:\n{context}"
        response = self.ollama.generate(model=self.model, prompt=prompt)
        return response['response']