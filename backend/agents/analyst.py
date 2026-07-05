from crewai import Agent
from langchain_groq import ChatGroq
import os
from dotenv import load_dotenv

load_dotenv()

llm = ChatGroq(
    model="groq/llama-3.3-70b-versatile",
    api_key=os.getenv("GROQ_API_KEY")
)

analyst = Agent(
    role="Business Analyst",
    goal="Analyze the research data and extract key insights, trends, and opportunities",
    backstory="You are a sharp business analyst who transforms raw research into actionable insights.",
    llm=llm,
    verbose=True
)