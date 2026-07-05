from crewai import Agent
from langchain.tools import BaseTool
from langchain_groq import ChatGroq
from tavily import TavilyClient
import os
from dotenv import load_dotenv

load_dotenv()

llm = ChatGroq(
    model="groq/llama-3.3-70b-versatile",
    api_key=os.getenv("GROQ_API_KEY")
)

class TavilySearchTool(BaseTool):
    name: str = "Web Search"
    description: str = "Search the web for information about a topic"

    def _run(self, query: str) -> str:
        client = TavilyClient(api_key=os.getenv("TAVILY_API_KEY"))
        results = client.search(query=query, max_results=5)
        output = ""
        for r in results["results"]:
            output += f"Title: {r['title']}\nURL: {r['url']}\nContent: {r['content']}\n\n"
        return output

search_tool = TavilySearchTool()

researcher = Agent(
    role="Market Research Specialist",
    goal="Search the web and gather detailed information about the given topic",
    backstory="You are an expert market researcher who finds accurate and relevant information from the web.",
    tools=[search_tool],
    llm=llm,
    verbose=True
)