from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from app.agent import run_agentic_workflow

app = FastAPI(
    title="FastAPI Agentic Vector RAG API",
    description="An OpenAI function-calling agent capable of navigating Pinecone vector data dynamically.",
    version="1.0.0"
)

class QueryRequest(BaseModel):
    message: str

class QueryResponse(BaseModel):
    answer: str

@app.post("/api/v1/agent/chat", response_model=QueryResponse)
async def chat_with_agent(payload: QueryRequest):
    try:
        result = run_agentic_workflow(payload.message)
        return QueryResponse(answer=result)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/health")
def health_check():
    return {"status": "healthy"}
