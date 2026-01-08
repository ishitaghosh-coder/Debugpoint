import base64
from typing import List, Dict

def format_citations(retrieved_points: List) -> str:
    """Requirement 5: Clear referencing of sources used for generation."""
    citations = []
    for point in retrieved_points:
        # Extract metadata from Qdrant payload
        source_id = point.id
        modality = point.payload.get("type", "unknown")
        page = point.payload.get("page_number", "N/A")
        
        ref = f"[Source {source_id}: {modality.upper()} (Page {page})]"
        citations.append(ref)
    
    return "\n".join(citations)

def encode_image_to_base64(image_path: str) -> str:
    """Requirement 1: Helper to process images for MLLM reasoning."""
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode('utf-8')

def calculate_uncertainty_flag(score: float, threshold: float = 0.7) -> Dict:
    """Requirement 6: Assess strength of evidence and acknowledge uncertainty."""
    is_uncertain = score < threshold
    status = "Low Confidence" if is_uncertain else "Verified Fact"
    
    return {
        "is_uncertain": is_uncertain,
        "confidence_label": status,
        "warning_msg": "Note: Evidence is fragmented. Response may contain inferred assumptions." if is_uncertain else ""
    }

def clean_markdown_table(raw_text: str) -> str:
    """Requirement 1: Structural cleanup for text extracted from scans/PDFs."""
    # Logic to ensure tables extracted by Docling are readable by the LLM
    return raw_text.strip().replace("\n\n", "\n")
def format_sources(points):
    # Requirement 5: Clearly reference sources [cite: 14]
    return "\n".join([f"- [{p.payload['source']}] ({p.payload['type']})" for p in points])

def get_confidence_warning(score):
    # Requirement 6: Acknowledge uncertainty [cite: 15]
    if score < 0.7:
        return "⚠️ Disclaimer: Response based on low-confidence or inferred data."
    return ""