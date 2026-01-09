import os
from docling.document_converter import DocumentConverter
from qdrant_client import QdrantClient

class IngestionEngine:
    def __init__(self):
        # Path creates a local folder; no Docker server needed
        self.qdrant = QdrantClient(path="local_database_storage")
        self.converter = DocumentConverter()

    def process_file(self, file_path):
        result = self.converter.convert(file_path)
        content = result.document.export_to_markdown()
        
        # Metadata fulfills Requirement 5 (Citations)
        self.qdrant.add(
            collection_name="knowledge_base",
            documents=[content],
            metadata=[{"source": os.path.basename(file_path), "type": "multimodal"}]
        )