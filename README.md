# 🌱 AI Home Gardening Assistant

## Project Description

AI Home Gardening Assistant is an Agentic AI application designed to provide gardening support using Retrieval-Augmented Generation (RAG).

The system helps users get information about plant care, diseases, watering requirements, and fertilizer recommendations using a domain-specific gardening knowledge base.

The application uses multiple AI agents that collaborate to analyze user questions, retrieve relevant information, and generate helpful gardening answers.


## System Architecture


User
 |
 v
Streamlit Interface
 |
 v
Agent Controller
 |
 +----------------+
 |                |
Planning Agent    Knowledge Agent
 |                |
 |                v
 |          Chroma Vector DB
 |                |
 +---------> Groq LLM
                 |
                 v
          Gardening Answer

## Agentic AI Design Patterns


### 1. Router Pattern

Location:
agent_controller.py

The controller decides which agent should handle the user query.


### 2. Planning Pattern

Location:
agents/planning_agent.py

The planning agent breaks the user request into smaller steps:
- Identify problem
- Search knowledge
- Generate solution


### 3. Tool-use Pattern

Location:
agents/knowledge_agent.py

The knowledge agent uses the Chroma vector database as a retrieval tool.
It searches the gardening knowledge base before generating the final answer.
  


### 4.  Retrieval-Augmented Generation (RAG)

Location:
agents/knowledge_agent.py

The agent retrieves relevant gardening information from the vector database before generating an answer.

## Agent Communication Flow


User Question

↓

Controller Agent

↓

Planning Agent

↓

Knowledge Agent

↓

Vector Database

↓

Groq LLM

↓

Final Response


## Agent Communication Protocol

The agents exchange information during the problem-solving process.

Planning Agent sends the task details to the Knowledge Agent.

Example message:

{
 "task": "Find gardening information",
 "action": "Retrieve relevant documents"
}

Knowledge Agent returns the retrieved information:

{
 "context": "Relevant plant care information",
 "result": "Generated gardening recommendation"
}

This communication allows multiple agents to collaborate and produce a better response.



## RAG Pipeline


Documents
(20+ gardening PDFs)

↓

PDF Loader

↓

Text Chunking

↓

HuggingFace Embeddings

↓

Chroma Vector Database

↓

Similarity Search

↓

Groq LLM

↓

Answer

## Model Selection Strategy

| Task | Model | Provider | Reason for Selection |
|---|---|---|---|
| Text Embedding | all-MiniLM-L6-v2 | HuggingFace | Fast and lightweight embedding model suitable for semantic search. |
| Answer Generation | Llama model | Groq | Low latency, good reasoning ability, and suitable for generating gardening recommendations. |

The embedding model is selected because it provides efficient vector representation with low computational requirements.

The Groq Llama model is selected for final response generation because it provides faster inference and good quality answers for user queries.


## Technologies

- Python
- Streamlit
- LangChain
- ChromaDB
- HuggingFace Embeddings
- Groq API
- GitHub


## Deployment

The application is deployed using Streamlit Community Cloud.

Live Demo:
https://home-gardening-agent-bzc3rcefecfnyu7e4vziig.streamlit.app/

GitHub Repository:
https://github.com/thushathusha310-cyber/Home-Gardening-Agent

## Limitations

- The system provides gardening guidance only from the available knowledge base.
- It cannot replace professional agricultural experts.
- Accuracy depends on the quality of uploaded documents.
