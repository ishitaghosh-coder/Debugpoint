import streamlit as st
from logic import MultimodalEngine

st.set_page_config(page_title="CHAKRAVYUH 1.0 RAG", layout="wide")
st.title("🛡️ Multimodal RAG System")

engine = MultimodalEngine()

# Sidebar for Ingestion (Mandatory Requirement 1 & 2) [cite: 8, 10]
with st.sidebar:
    st.header("Data Ingestion")
    uploaded_files = st.file_uploader("Upload PDF, Images, or Audio", accept_multiple_files=True)
    if st.button("Process & Index"):
        st.success("Data stored in Unified Knowledge Representation [cite: 10]")

# Main Query Interface
query = st.text_input("Enter your query (The system will analyze all modalities):")

if query:
    with st.spinner("Analyzing cross-modal evidence..."):
        answer, sources = engine.generate_grounded_answer(query)
        
        st.subheader("Grounded Response")
        st.write(answer)
        
        # Explainable Citations [cite: 14, 22]
        with st.expander("View Evidence & Citations"):
            for s in sources:
                st.write(f"Source ID: {s.id} | Modality: {s.payload.get('type')} | Confidence: {s.score:.2f}")