import os
from dotenv import load_dotenv
from PIL import Image
from google import genai
load_dotenv()

client = genai.Client()

image = Image.open(r"")
response = client.models.generate_content(
    model="gemini-3-flash-preview",
    contents=[image, "Tell me about this image"]
)
print(response.text)