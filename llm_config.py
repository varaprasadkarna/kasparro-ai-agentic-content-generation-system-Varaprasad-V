from crewai import LLM
import os

llm = LLM(
    model="openrouter/meta-llama/llama-3-70b-instruct",
    api_key=os.getenv("OPENROUTER_API_KEY"),
    base_url="https://openrouter.ai/api/v1",
    temperature=0.4,
)
