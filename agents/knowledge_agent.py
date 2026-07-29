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


    # Create vectorstore if it does not exist
    if not os.path.exists("vectorstore/chroma.sqlite3"):
        from create_vectorstore import create_vectorstore
        create_vectorstore()


    vectorstore = Chroma(
        persist_directory="vectorstore",
        embedding_function=embeddings
    )


    # Search relevant information
    docs = vectorstore.similarity_search(question, k=3)


    if docs:

        context = "\n\n".join(
            [doc.page_content for doc in docs]
        )


        llm = ChatGroq(
            groq_api_key=GROQ_API_KEY,
            model_name="llama-3.1-8b-instant"
        )


        prompt = f"""
You are a helpful AI Home Gardening Assistant.

Answer the user's gardening question using the provided knowledge.

Instructions:
- Give a simple and clear answer.
- Do not mention PDF pages or document names.
- Do not copy the knowledge directly.
- Summarize the important information.
- Provide possible causes and practical solutions.
- Use bullet points when explaining steps.
- Keep the answer easy for beginners to understand.

Knowledge:
{context}

User Question:
{question}

Answer:
"""


        response = llm.invoke(prompt)

        return response.content


    else:
        return "No relevant gardening information found."