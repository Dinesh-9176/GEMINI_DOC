from google import genai
from pydantic import BaseModel, Field
from typing import Literal
import logging
from dotenv import load_dotenv


load_dotenv()

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)


class Feedback(BaseModel):
    sentiment: Literal["positive", "neutral", "negative"]
    summary: str

client = genai.Client()
prompt = "The new UI is incredibly intuitive and visually appealing. Great job. Add a very long summary to test streaming!"

response_stream = client.models.generate_content_stream(
    model="gemini-3-flash-preview",
    contents=prompt,
    config={
        "response_mime_type": "application/json",
        "response_json_schema": Feedback.model_json_schema(),
    },
)

for chunk in response_stream:
    logger.info(chunk.candidates[0].content.parts[0].text)