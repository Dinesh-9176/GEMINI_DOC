import os
from google import genai
from google.genai import types
from dotenv import load_dotenv
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)


load_dotenv()

with open(r'C:\Users\dines\OneDrive\Desktop\GEMINI_QUICK_START\Schematic.jpeg', 'rb') as f:
    image_bytes = f.read()

client = genai.Client()
response = client.models.generate_content(
    model='gemini-3-flash-preview',
    contents=[
      types.Part.from_bytes(
        data=image_bytes,
        mime_type='image/jpeg',
      ),
      'Caption this image.'
    ]
)

logger.info(response.text)