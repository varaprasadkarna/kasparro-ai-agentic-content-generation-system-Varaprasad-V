from crewai import Task
from agents.question_agent import question_agent


question_task = Task(
    description="""
    Generate AT LEAST 15 realistic user questions grouped into categories
    such as Usage, Ingredients, Safety, Skin Type, Pricing, etc.

    Rules:
    - Use ONLY the provided product data
    - Do NOT hallucinate ingredients
    - Output STRICT JSON
    """,
    agent=question_agent,
    expected_output="""
    JSON object with category names as keys
    and each value being a list of questions.
    Minimum 15 total questions.
    """
)
