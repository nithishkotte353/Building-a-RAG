def search(query, model, index, documents, filenames, top_k=3):
    query_embedding = model.encode([query])
    distances, indices = index.search(query_embedding, top_k)
    results = [(documents[idx], filenames[idx]) for idx in indices[0]]
    return results
