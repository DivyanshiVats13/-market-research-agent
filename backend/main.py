import os
os.environ["CREWAI_DISABLE_CACHE"] = "true"

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from agents.crew import run_research

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

class ResearchRequest(BaseModel):
    topic: str

@app.get("/")
def root():
    return {"message": "Market Research Agent API is running"}

@app.post("/research")
def research(request: ResearchRequest):
    result = run_research(request.topic)
    return {"report": result}