from crewai import Agent
from llm_config import llm

question_agent = Agent(
    role="User Question Generator",
    goal="Generate at least 15 realistic user questions grouped into categories",
    backstory="You are an expert product analyst who anticipates real customer questions.",
    llm=llm,
    memory=True,
    verbose=True
)
