from langchain_chroma import Chroma
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_groq import ChatGroq
from dotenv import dotenv_values


# Load API key from .env
config = dotenv_values(".env")
GROQ_API_KEY = config["GROQ_API_KEY"]


def knowledge_agent(question):

    embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )

    vectorstore = Chroma(
        persist_directory="vectorstore",
        embedding_function=embeddings
    )

    # Search relevant information from PDFs
    docs = vectorstore.similarity_search(question, k=3)

    if docs:

        context = "\n\n".join(
            [doc.page_content for doc in docs]
        )

        # Groq LLM
        llm = ChatGroq(
            groq_api_key=GROQ_API_KEY,
            model_name="llama-3.1-8b-instant"
        )

        prompt = f"""
You are a helpful Home Gardening Assistant.

Answer the user's question using the provided gardening knowledge.

Knowledge:
{context}

Question:
{question}

Give a simple and practical gardening answer.
"""

        response = llm.invoke(prompt)

        return response.content

    else:
        return "No relevant gardening information found."