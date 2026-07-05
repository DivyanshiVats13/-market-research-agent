from crewai import Crew, Task
from agents.researcher import researcher, search_tool
from agents.analyst import analyst
from agents.reporter import reporter

def run_research(topic: str) -> str:

    research_task = Task(
        description=f"Search the web and find specific, accurate information about: {topic}. Find actual names, links, tools, papers, or products — whatever is most relevant to the query.",
        expected_output="A detailed list of findings with specific names, URLs, descriptions, and data points.",
        agent=researcher,
        tools=[search_tool]
    )

    analysis_task = Task(
        description=f"Review the research findings about: {topic}. Organize and filter the most relevant and useful information for the user.",
        expected_output="A clean, organized summary of the most relevant findings.",
        agent=analyst,
        context=[research_task]
    )

    report_task = Task(
        description=f"""Write a direct, helpful response about: {topic}.
        
        Rules:
        - If the user wants tools/products: list them with name, description, and link
        - If the user wants papers: list them with title, authors, and link  
        - If the user wants market analysis: write a structured report
        - Always use bullet points and be specific
        - Never write a generic executive summary if the user wants a specific list
        - Match your response format to what the user actually asked for""",
        expected_output="A direct, specific, well-formatted markdown response that answers exactly what the user asked.",
        agent=reporter,
        context=[analysis_task]
    )

    crew = Crew(
        agents=[researcher, analyst, reporter],
        tasks=[research_task, analysis_task, report_task],
        verbose=True
    )

    result = crew.kickoff()
    return str(result)