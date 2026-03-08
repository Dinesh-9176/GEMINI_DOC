import os
from dotenv import load_dotenv
from google import genai
import logging

load_dotenv()


logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)
logger.info("Creating client")


client = genai.Client()


chat = client.chats.create(model="gemini-3-flash-preview")


logger.info("first message")
response = chat.send_message("I have 2 dogs in my house.")
logger.info(response.text)


logger.info("second message")
response = chat.send_message("How many paws are in my house?")
logger.info(response.text)


logger.info("getting history")
for message in chat.get_history():
    logger.info(f"role - {message.role}: {message.parts[0].text}")
