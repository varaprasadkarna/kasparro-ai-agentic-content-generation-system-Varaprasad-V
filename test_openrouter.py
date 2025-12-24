from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(
    api_key=os.getenv("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"),
    base_url=os.getenv("https://openrouter.ai/api/v1")
)

response = client.chat.completions.create(
    model=os.getenv("OPENAI_MODEL"),
    messages=[{"role": "user", "content": "Say OK"}]
)

print(response.choices[0].message.content)
