# FastAPI OpenAI Agentic Vector Retrieval Starter Kit

A lightweight, enterprise-ready template for building **FastAPI** agents that leverage **OpenAI Function Calling** to dynamically pull context from a vector database (**Pinecone**).

## 🗂️ Project Blueprint & Execution Flow

fastapi-openai-agent/
├── app/
│   ├── config.py          # Safely handles settings using pydantic-settings
│   ├── vector_store.py    # OpenAI embedding creation & Pinecone vector database query execution
│   ├── agent.py           # Core agent logic loop with native OpenAI tool-definition/resolution 
│   └── main.py            # FastAPI implementation providing clean endpoints & interactive Swagger docs
├── .env.example           # Clean blueprint for environment configurations
├── requirements.txt       # Version-locked package manifest
└── README.md              # Setup manual and operational guidelines




 Client Request          +-------------------+          Tool Loop
  (User Message) -------> |   FastAPI App     |              |
                          +---------+---------+              |
                                    |                        v
                                    v              +-------------------+
                          +-------------------+    | OpenAI Embeddings |

                          | OpenAI Agent Loop | <--+-------------------+
                          +---------+---------+              |
                                    |                        v
                                    v              +-------------------+
                             Final Response        |  Pinecone Search  |
                                    +------------> +-------------------+



## 🛠️ Key Technical Highlights Inside This Layout

app/vector_store.py: Manages operational communication with the vector environment. It abstracts away the process of parsing the user’s conversational criteria, calling text-embedding-3-small to transform textual prompts into deterministic vectors, and pulling matching document records with descriptive metadata hooks.

app/agent.py: Declares query_vector_store as a viable structural tool configuration. It launches an automated conversational step: if the model judges that internal resources are required, it halts processing, outputs a tool invocation command request, waits for your backend vector lookup to supply data payload context, and continues generating with enhanced ground truth data.

app/main.py: Exposes a robust asynchronous endpoint (/api/v1/agent/chat) packaged cleanly alongside full validation schema parsing handling through Pydantic.


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
