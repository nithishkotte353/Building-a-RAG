from transformers import pipeline  # type: ignore

def generate_answer(query, results):
    # Load a pre-trained LLM for question answering (QA)
    qa_pipeline = pipeline("question-answering")
    
    context = " ".join([result for result, _ in results])
    answer = qa_pipeline(question=query, context=context)
    return answer

def generate_answer_with_sources(query, results):
    qa_pipeline = pipeline("question-answering")
    context = " ".join([result for result, _ in results])
    answer = qa_pipeline(question=query, context=context)
    sources = [filename for _, filename in results]
    return answer, sources[:3]  # Top 3 sources
