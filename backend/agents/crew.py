from crewai import Crew, Task
from agents.researcher import researcher, search_tool
from agents.analyst import analyst
from agents.reporter import reporter

def run_research(topic: str) -> str:

    research_task = Task(
        description=f"Search the web and gather detailed information about: {topic}",
        expected_output="A detailed summary of findings including key players, trends, and data points.",
        agent=researcher,
        tools=[search_tool]
    )

    analysis_task = Task(
        description=f"Analyze the research findings about: {topic}. Identify key insights, opportunities, and threats.",
        expected_output="A structured analysis with key insights, market opportunities, and recommendations.",
        agent=analyst,
        context=[research_task]
    )

    report_task = Task(
        description=f"Write a professional market research report about: {topic}",
        expected_output="A complete markdown report with sections: Executive Summary, Key Findings, Market Insights, Opportunities, and Conclusion.",
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