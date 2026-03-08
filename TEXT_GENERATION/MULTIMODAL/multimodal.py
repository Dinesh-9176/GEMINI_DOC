import os
from dotenv import load_dotenv
from PIL import Image
from google import genai
import logging

load_dotenv()
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)
logger.info("Creating client")
client = genai.Client()
logger.info("Opening image")
image = Image.open(r"")
logger.info("Generating content")
response = client.models.generate_content(
    model="gemini-3-flash-preview",
    contents=[image, "Tell me about this image"]
)
logger.info(response.text)