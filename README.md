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


### 3. Retrieval-Augmented Generation (RAG)

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

## Model Selection


| Task | Model | Reason |
|-|-|-|
| Text Embedding | all-MiniLM-L6-v2 | Fast and lightweight embedding model |
| Answer Generation | Groq Llama model | Low latency and good reasoning ability |

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
(Add your Streamlit URL here)

GitHub Repository:
(Add your GitHub link here)

## Limitations

- The system provides gardening guidance only from the available knowledge base.
- It cannot replace professional agricultural experts.
- Accuracy depends on the quality of uploaded documents.