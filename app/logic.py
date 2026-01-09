import ollama
from qdrant_client import QdrantClient

class RAGBrain:
    def __init__(self):
        # Connects to the Ollama app running on your Windows
        self.client = ollama.Client(host='http://localhost:11434')
        self.qdrant = QdrantClient(path="local_database_storage")

    def adaptive_search(self, query):
        """Requirement 8: Adaptive retrieval if evidence is weak."""
        results = self.qdrant.query(collection_name="knowledge_base", query_text=query, limit=3)
        return results if results else None

    def detect_conflicts(self, context):
        """Requirement 7: Present conflicts to the user."""
        prompt = f"Find contradictions between these sources. Explain why they disagree:\n{context}"
        return self.client.generate(model='gemma3:4b', prompt=prompt)['response']