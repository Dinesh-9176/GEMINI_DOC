import os
from google import genai
from dotenv import load_dotenv
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)


load_dotenv()

client = genai.Client()

my_file = client.files.upload(file=r"C:\Users\dines\OneDrive\Desktop\GEMINI_QUICK_START\Schematic.jpeg")

response = client.models.generate_content(
    model="gemini-3-flash-preview",
    contents=[my_file, "Caption this image."],
)

logger.info(response.text)