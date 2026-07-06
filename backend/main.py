import os
os.environ["CREWAI_DISABLE_PROMPT_CACHING"] = "true"

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from dotenv import load_dotenv
from tavily import TavilyClient
from groq import Groq

load_dotenv()

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
    topic = request.topic
    
    # Agent 1: Researcher - search the web
    tavily = TavilyClient(api_key=os.getenv("TAVILY_API_KEY"))
    search_results = tavily.search(query=topic, max_results=8)
    
    context = ""
    for r in search_results["results"]:
        context += f"Title: {r['title']}\nURL: {r['url']}\nContent: {r['content']}\n\n"
    
    # Agent 2 & 3: Analyst + Reporter - generate report
    groq_client = Groq(api_key=os.getenv("GROQ_API_KEY"))
    
    response = groq_client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {
                "role": "system",
                "content": "You are a knowledgeable research assistant. Based on the web search results, answer the user's question directly and conversationally, like you're explaining it to a colleague. Skip formal report structure (no 'Introduction', 'Conclusion', numbered sections). Use markdown for clarity (bold, bullet points, links) where it genuinely helps, but keep it natural and to the point. Be specific with names, numbers, and links when relevant"
            },
            {
                "role": "user", 
                "content": f"Topic: {topic}\n\nWeb Search Results:\n{context}\n\nAnswer the topic/question directly and conversationally, using the search results above."
            }
        ],
        max_tokens=2000
    )
    
    report = response.choices[0].message.content
    return {"report": report}