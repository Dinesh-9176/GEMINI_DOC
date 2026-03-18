import json
from openai import OpenAI
import logging
import os



tools = [
    {
        "type": "function",
        "function": {
            "name": "get_current_temperature",
            "description": "Gets the current temperature for a given location.",
            "parameters": {
                "type": "object",
                "properties": {
                    "location": {
                        "type": "string",
                        "description": "The city name, e.g. San Francisco",
                    },
                },
                "required": ["location"],
            },
        },
    }
]



client = OpenAI(
    base_url="http://localhost:11434/v1",
    api_key = "ollama"
)


response = client.chat.completions.create(
    model="qwen3:0.6b",
    messages=[{"role": "user", "content": "What's the temperature in London?"}],
    tools=tools,
    tool_choice="auto",
)



message = response.choices[0].message

if message.tool_calls:
    for tool_call in message.tool_calls:
        print(f"Function to call: {tool_call.function.name}")
        print(f"Arguments: {tool_call.function.arguments}")
else:
    print("No function call found in the response.")
    print(message.content)