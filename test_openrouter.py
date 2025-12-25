from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY"),
    base_url=os.getenv("OPENROUTER_BASE_URL")
)

response = client.chat.completions.create(
    model=os.getenv("OPENAI_MODEL"),
    messages=[{"role": "user", "content": "Say OK"}]
)

print(response.choices[0].message.content)
