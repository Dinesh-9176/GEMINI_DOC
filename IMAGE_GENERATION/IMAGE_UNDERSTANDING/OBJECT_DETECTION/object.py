import os
from dotenv import load_dotenv
from google import genai
from google.genai import types
from PIL import Image
import json
import logging 

load_dotenv()

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

client = genai.Client()
prompt = "Detect the all boxes in the image. The box_2d should be [ymin, xmin, ymax, xmax] normalized to 0-1000."

image = Image.open(r"C:\Users\dines\OneDrive\Desktop\GEMINI_QUICK_START\Schematic.jpeg")

config = types.GenerateContentConfig(
  response_mime_type="application/json"
  )

response = client.models.generate_content(model="gemini-3-flash-preview",
                                          contents=[image, prompt],
                                          config=config
                                          )

width, height = image.size
bounding_boxes = json.loads(response.text)

converted_bounding_boxes = []
for bounding_box in bounding_boxes:
    abs_y1 = int(bounding_box["box_2d"][0]/1000 * height)
    abs_x1 = int(bounding_box["box_2d"][1]/1000 * width)
    abs_y2 = int(bounding_box["box_2d"][2]/1000 * height)
    abs_x2 = int(bounding_box["box_2d"][3]/1000 * width)
    converted_bounding_boxes.append([abs_x1, abs_y1, abs_x2, abs_y2])

logger.info(f"Image size: {width}, {height}")
logger.info(f"Bounding boxes: {converted_bounding_boxes}")
