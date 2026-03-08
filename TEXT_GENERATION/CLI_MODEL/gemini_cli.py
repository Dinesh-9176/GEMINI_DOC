import os
from dotenv import load_dotenv
from google import genai
from google.genai import types
from PIL import Image
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

load_dotenv()

client = genai.Client()

chat = client.chats.create(
    model="gemini-3-flash-preview",
    config=types.GenerateContentConfig(
        system_instruction="You are a helpful AI assistant.",
        thinking_config=types.ThinkingConfig(thinking_level="low")
    )
)

while True:

    logger.info("\nGEMINI CLI ASSISTANT")
    logger.info("1 Chat with AI")
    logger.info("2 Analyze Image")
    logger.info("3 Reasoning Question")
    logger.info("4 Exit")

    choice = input("Select option: ").lower()

    if choice == "end" or choice == "4":
        logger.info("Session ended.")
        break

    
    elif choice == "1":

        while True:
            msg = input("You (type 'end' to stop chat): ")

            if msg.lower() == "end":
                break

            try:
                stream = chat.send_message_stream(msg)

                logger.info("Gemini: ")

                for chunk in stream:
                    if chunk.text:
                        logger.info(chunk.text)

            except Exception as e:
                logger.error(f"\n[API Error]: {e}")

    
    elif choice == "2":

        path = input("Enter image path (or 'end'): ")

        if path.lower() == "end":
            continue

        img = Image.open(path)

        try:
            response = client.models.generate_content(
                model="gemini-3-flash-preview",
                contents=["Describe this image", img]
            )

            logger.info("\nGemini:", response.text)
        except Exception as e:
            logger.info("\n[API Error]: {e}")

    
    elif choice == "3":

        q = input("Enter reasoning question (or 'end'): ")

        if q.lower() == "end":
            continue

        try:
            response = client.models.generate_content(
                model="gemini-3-flash-preview",
                contents=q,
                config=types.GenerateContentConfig(
                    thinking_config=types.ThinkingConfig(
                        thinking_level="low"
                    )
                )
            )

            logger.info("\nGemini:", response.text)
        except Exception as e:
            logger.info("\n[API Error]: {e}")