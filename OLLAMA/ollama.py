from openai import OpenAI
import os

client = OpenAI(
    base_url="http://localhost:11434/v1",
    api_key=os.getenv("OLLAMA_API_KEY")
)

response = client.chat.completions.create(
    model="qwen3:0.6b",
    messages=[
        {"role": "user", "content": "what is vlsi"}
    ]
)

print(response.choices[0].message.content)