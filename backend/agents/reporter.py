from crewai import Agent
from langchain_groq import ChatGroq
import os
from dotenv import load_dotenv

load_dotenv()

llm = ChatGroq(
    model="groq/llama-3.1-8b-instant",
    api_key=os.getenv("GROQ_API_KEY")
)

reporter = Agent(
    role="Report Writer",
    goal="Write a clear, structured and professional market research report based on the analysis",
    backstory="You are an expert business writer who creates compelling and well-structured reports for executives.",
    llm=llm,
    verbose=True
)