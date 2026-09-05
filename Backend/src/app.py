from fastapi import FastAPI
from pydantic import BaseModel
from src.Graph.graph import workFlow
from fastapi.middleware.cors import CORSMiddleware


app=FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173", "http://localhost:3000"],# Add your frontend URL
    allow_credentials=True,
    allow_methods=["*"],# Allows all HTTP methods (POST, GET, etc.)
    allow_headers=["*"],# Allows all headers
    
)
agent=workFlow()

class ChatRequest(BaseModel):
    course:str
    question:str


@app.post('/chat')
def chat(request:ChatRequest):
    result=agent.invoke({        
        'course':request.course,
        'conversation':[
            ('human',request.question)
            ]
    })
    return {
        "answer": result["conversation"][-1].content
    }

