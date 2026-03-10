import os
import logging
from dotenv import load_dotenv
from google import genai
from google.genai import types

load_dotenv()

logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

client = genai.Client()

model_name = "gemini-2.5-flash"


def weather(city):
    return f"The weather in {city} is sunny."


weather_tool = types.Tool(
    function_declarations=[
        {
            "name": "weather",
            "description": "Get weather for a city",
            "parameters": {
                "type": "object",
                "properties": {
                    "city": {"type": "string"}
                },
                "required": ["city"]
            }
        }
    ]
)

prompt = "What is the weather in Chennai?"

response = client.models.generate_content(
    model=model_name,
    contents=prompt,
    config=types.GenerateContentConfig(
        tools=[weather_tool]
    )
)

logger.info(response.json)