import os
from google import genai
from google.genai import types
from dotenv import load_dotenv
import requests
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)


load_dotenv()

image_path = "https://goo.gle/instrument-img"
image_bytes = requests.get(image_path).content
image = types.Part.from_bytes(
  data=image_bytes, mime_type="image/jpeg"
)

client = genai.Client()

logger.info("Generating content")
response = client.models.generate_content(
    model="gemini-3-flash-preview",
    contents=["What is this image?", image],
)


logger.info(response.text)