from fastapi import FastAPI
import os
from pydantic import BaseModel 
from agent.agentic_workflow import GraphBuilder
from fastapi.responses import JSONResponse
app= FastAPI()

class QueryRequest(BaseModel):
    query: str 
@app.post("/query")

async def query_travel_agent(query:QueryRequest):
    try: 
        print(query)
        graph = GraphBuilder(model_provider="groq") # We capture the model provider. 
        react_app=graph() 
        png_graph = react_app.get_graph().draw_mermaid_png()
        with open("my_graph.png", "wb") as f: 
            f.write(png_graph) # We save the Graph as a png file 

        print(f"Graph saved as 'my_graph.png' in {os.getcwd()}")
        # Assuming request is a pydantic object like: {"question":} "your text"}
        messages ={"messages": [query.question]}

        output = react_app.invoke(messages)

        if isinstance(output, dict) and "messages" in output:
            final_output = output["messages"][-1].content # Last AI response 
        else: 
            final_output = str(output)

        return {"answer": final_output}
    except Exception as e:
        return JSONResponse (status_code=500, content={"error": str(e)})
    # """ 
    # Endpoint to query the travel agent"""