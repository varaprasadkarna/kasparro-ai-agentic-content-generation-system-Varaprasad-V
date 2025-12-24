from crewai import Agent
from llm_config import llm


question_agent = Agent(
    role="User Question Generator",
    goal="Generate at least 15 categorized user questions about a product",
    backstory="Expert product analyst anticipating real customer concerns",
    memory=True,
    llm=llm,
    verbose=True
)
