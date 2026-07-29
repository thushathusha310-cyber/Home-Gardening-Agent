from langchain_chroma import Chroma
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_groq import ChatGroq
from dotenv import load_dotenv
import os


load_dotenv()

GROQ_API_KEY = os.getenv("GROQ_API_KEY")


def knowledge_agent(question):

    embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )

    if not os.path.exists("vectorstore/chroma.sqlite3"):
        from create_vectorstore import create_vectorstore
        create_vectorstore()

    vectorstore = Chroma(
        persist_directory="vectorstore",
        embedding_function=embeddings
    )

    docs = vectorstore.similarity_search(question, k=1)

    if docs:

        context = "\n\n".join(
            [doc.page_content for doc in docs]
        )

        llm = ChatGroq(
            groq_api_key=GROQ_API_KEY,
            model_name="llama-3.1-8b-instant",
            temperature=0.2
        )

        prompt = f"""
You are a Home Gardening Assistant.

Answer the user's question using the knowledge provided.

Rules:
- Give a short answer.
- Do not mention page numbers.
- Do not mention book names.
- Do not copy the source text.
- Summarize in your own words.
- Give practical gardening advice.
- Use simple English.

Knowledge:
{context}

Question:
{question}

Answer:
"""

        response = llm.invoke(prompt)

        return response.content

    else:
        return "No relevant gardening information found."