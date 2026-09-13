import json
import openai
from app.config import settings
from app.vector_store import query_vector_store

client = openai.OpenAI(api_key=settings.OPENAI_API_KEY)

# Define the RAG retrieval tool for the OpenAI Assistant / Chat Completion
tools_definition = [
    {
        "type": "function",
        "function": {
            "name": "query_vector_store",
            "description": "Searches the vector database for internal company documentation, knowledge base items, and technical records regarding user queries.",
            "parameters": {
                "type": "object",
                "properties": {
                    "query_text": {
                        "type": "string",
                        "description": "The specific semantic query to look up in the vector knowledge base."
                    }
                },
                "required": ["query_text"]
            }
        }
    }
]

def run_agentic_workflow(user_message: str) -> str:
    messages = [
        {"role": "system", "content": "You are an advanced agentic assistant. You must proactively query your vector database tool whenever you need accurate, up-to-date context or knowledge base facts to answer the user's question. Synthesize the retrieved records seamlessly into your answers."},
        {"role": "user", "content": user_message}
    ]
    
    # First turn
    response = client.chat.completions.create(
        model="gpt-4o",
        messages=messages,
        tools=tools_definition,
        tool_choice="auto"
    )
    
    response_message = response.choices[0].message
    
    # Check if the agent decided to query the vector store
    if response_message.tool_calls:
        messages.append(response_message)
        
        for tool_call in response_message.tool_calls:
            if tool_call.function.name == "query_vector_store":
                arguments = json.loads(tool_call.function.argv or tool_call.function.arguments)
                retrieved_context = query_vector_store(arguments.get("query_text"))
                
                # Append tool results
                messages.append({
                    "role": "tool",
                    "tool_call_id": tool_call.id,
                    "name": "query_vector_store",
                    "content": json.dumps({"retrieved_knowledge": retrieved_context})
                })
        
        # Second turn with vector data context
        final_response = client.chat.completions.create(
            model="gpt-4o",
            messages=messages
        )
        return final_response.choices[0].message.content
        
    return response_message.content
