import faiss
import numpy as np

def build_index(embeddings):
    # Convert embeddings to a numpy array
    embedding_matrix = np.array(embeddings)

    # Build the FAISS index
    index = faiss.IndexFlatL2(embedding_matrix.shape[1])  # L2 distance
    index.add(embedding_matrix)
    
    return index
