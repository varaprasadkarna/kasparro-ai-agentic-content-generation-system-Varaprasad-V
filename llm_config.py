import os
from crewai import LLM
from dotenv import load_dotenv

load_dotenv()

llm = LLM(
    model=os.getenv("OPENAI_MODEL"),
    temperature=0.4
)
