import streamlit as st
from search import search
from rag_pipeline import generate_answer_with_sources
from data_loader import load_pdfs
from embedding import generate_embeddings
from indexer import build_index
import faiss

# Load and prepare the documents
pdf_folder = 'pdfs'
documents, filenames = load_pdfs(pdf_folder)
embeddings, model = generate_embeddings(documents)

# Build FAISS index
dimension = embeddings.shape[1]
index = faiss.IndexFlatL2(dimension)
index.add(embeddings)

# Streamlit UI
st.title('Research Paper Answer Bot')

query = st.text_input("Enter your query:")

if st.button('Search'):
    if query:
        results = search(query, model, index, documents, filenames)
        answer, sources = generate_answer_with_sources(query, results)
        
        st.write(f"**Answer:** {answer['answer']}")
        
        st.write("**Sources:**")
        for i, source in enumerate(sources):
            st.write(f"Source {i+1}: {source}")

# Feedback mechanism
feedback = st.radio("Was this answer helpful?", ("Yes", "No"))
if feedback == "No":
    st.text_area("Please provide your feedback to help us improve:")