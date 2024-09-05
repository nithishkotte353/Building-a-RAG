from data_loader import load_pdfs
from embedding import generate_embeddings
from indexer import build_index
from search import search
from rag_pipeline import generate_answer_with_sources

def main():
    # Load PDFs
    pdf_folder = 'pdfs'
    documents, filenames = load_pdfs(pdf_folder)

    # Generate Embeddings
    embeddings, model = generate_embeddings(documents)

    # Build Index
    index = build_index(embeddings)

    # Example Query
    query = "What is the role of attention mechanism in transformers?"

    # Search and Generate Answer
    results = search(query, model, index, documents, filenames)
    answer, sources = generate_answer_with_sources(query, results)

    print(f"Answer: {answer['answer']}")
    print("Sources:")
    for i, source in enumerate(sources):
        print(f"Source {i+1}: {source}")

if __name__ == "__main__":
    main()
