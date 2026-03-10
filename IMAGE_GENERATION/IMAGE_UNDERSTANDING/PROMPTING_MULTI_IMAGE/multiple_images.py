import os
from google import genai
from google.genai import types
from dotenv import load_dotenv
import logging

load_dotenv()

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

client = genai.Client()

logger.info("Uploading first image")
image1_path = r"C:\Users\dines\OneDrive\Desktop\GEMINI_QUICK_START\Schematic.jpeg"
uploaded_file = client.files.upload(file=image1_path)


logger.info("Uploading second image")
image2_path = r"C:\Users\dines\OneDrive\Desktop\GEMINI_QUICK_START\Schematic.jpeg"
with open(image2_path, 'rb') as f:
    img2_bytes = f.read()

response = client.models.generate_content(

    model="gemini-3-flash-preview",
    contents=[
        "What is different between these two images?",
        uploaded_file,
        types.Part.from_bytes(
            data=img2_bytes,
            mime_type='image/png'
        )
    ]
)

logger.info(response.text)