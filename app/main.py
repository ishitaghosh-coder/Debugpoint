def format_citations(points):
    """Requirement 5: Citing retrieved evidence."""
    if not points: return "No sources cited."
    return "\n".join([f"- Source: {p.metadata['source']}" for p in points])

def uncertainty_check(score):
    """Requirement 6: Acknowledge uncertainty."""
    if score < 0.6:
        return "⚠️ Warning: Low confidence evidence."
    return "✅ High confidence evidence."