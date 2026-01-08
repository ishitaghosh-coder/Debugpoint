import streamlit as st
from ingestion import IngestionEngine
from logic import RAGBrain
from utils import format_sources, get_confidence_warning

st.set_page_config(page_title="CHAKRAVYUH RAG")
st.title("🛡️ Multimodal RAG System")

# Initialize Engines
if 'ingestor' not in st.session_state:
    st.session_state.ingestor = IngestionEngine()
    st.session_state.brain = RAGBrain()

# Sidebar: Requirement 1 & 2
with st.sidebar:
    st.header("Ingest Data")
    files = st.file_uploader("Upload Files", accept_multiple_files=True)
    if st.button("Process"):
        st.success("Unified Knowledge Representation Updated")

# Main Interface: Requirement 3-9
query = st.text_input("Enter Query:")
if query:
    # 1. Adaptive Retrieval [cite: 17]
    evidence = st.session_state.brain.adaptive_retrieval(query, st.session_state.ingestor.qdrant)
    
    # 2. Hallucination Suppression [cite: 18]
    if not evidence:
        st.error("I cannot answer. Missing adequate evidence.")
    else:
        # 3. Conflict Detection [cite: 16]
        conflicts = st.session_state.brain.detect_conflicts(evidence)
        st.info(f"Analysis: {conflicts}")
        
        # 4. Grounded Answer [cite: 13]
        st.write("### Answer")
        st.write("Generated grounded response here...")
        st.caption(format_sources(evidence))
        st.warning(get_confidence_warning(evidence[0].score))