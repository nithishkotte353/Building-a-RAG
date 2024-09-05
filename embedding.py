from sentence_transformers import SentenceTransformer

def generate_embeddings(documents):
    # Load a pre-trained embedding model
    model = SentenceTransformer('all-MiniLM-L6-v2')
    
    # Generate embeddings for each document
    embeddings = model.encode(documents, show_progress_bar=True)
    return embeddings, model
