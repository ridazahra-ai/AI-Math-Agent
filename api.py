from fastapi import FastAPI
from pydantic import BaseModel
from agent import chat

app = FastAPI(
    title="AI Math Agent API",
    description="AI-powered Math Agent built using FastAPI, LangChain, Gemini and SymPy.",
    version="1.0.0"
)

class Question(BaseModel):
    question: str

@app.get("/")
def home():
    return {
        "message": "AI Math Agent API",
        "docs": "/docs",
        "version": "1.0.0"
    }

@app.get("/health")
def health():
    return {
        "status": "healthy"
    }

@app.post("/solve")
def solve(data: Question):
    response = chat(data.question)
    return {
        "answer": response
    }
