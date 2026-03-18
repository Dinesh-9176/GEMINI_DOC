import os
from dotenv import load_dotenv
from google import genai
import logging


load_dotenv()


logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)


client = genai.Client()
logger.info("Generating content")
response = client.models.generate_content_stream(
    model="gemini-3-flash-preview",
    contents=["Explain how AI works"]
)
for chunk in response:
    logger.info(chunk.text)