import streamlit as st

DOCUMENTS = [
    "Python is a popular programming language.",
    "Streamlit is used to build web apps quickly.",
    "RAG stands for Retrieval-Augmented Generation.",
    "Llama 3 is a powerful large language model.",
    "Arize AI helps monitor machine learning models."
]

def simple_vector_search(query, docs, top_k=2):
    results = []
    query_words = query.lower().split()
    for doc in docs:
        score = sum(word in doc.lower() for word in query_words)
        if score > 0:
            results.append((score, doc))
    results.sort(reverse=True)
    return [doc for _, doc in results[:top_k]]

def mock_llm_generate(prompt):
    return "This is a mock answer based on retrieved documents."

def rag_pipeline(user_question):
    retrieved_docs = simple_vector_search(user_question, DOCUMENTS)
    context = "\n".join(retrieved_docs)
    prompt = f"Context:\n{context}\nQuestion: {user_question}\nAnswer:"
    answer = mock_llm_generate(prompt)
    return answer

def main():
    st.title("Simple GenAI Chatbot with RAG")
    user_input = st.text_input("Ask your question here:")
    if user_input:
        response = rag_pipeline(user_input)
        st.write("**Answer:**", response)

if __name__ == "__main__":
    main()
