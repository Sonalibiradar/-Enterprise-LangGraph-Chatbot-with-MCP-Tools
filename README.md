# FastAPI OpenAI Agentic Vector Retrieval Starter Kit

A lightweight, enterprise-ready template for building **FastAPI** agents that leverage **OpenAI Function Calling** to dynamically pull context from a vector database (**Pinecone**).

## Project Setup

1. **Clone & Initialize**
   ```bash
   git init
   git add .
   git commit -m "Initial commit: FastAPI Agentic RAG architecture"
   ```

2. **Configure Environment**
   ```bash
   cp .env.example .env
   # Populate your OPENAI_API_KEY and PINECONE_API_KEY inside .env
   ```

3. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Boot Up Server**
   ```bash
   uvicorn app.main:app --reload
   ```
   Open your browser to `http://127.0.0.1:8000/docs` to interact with Swagger UI.
