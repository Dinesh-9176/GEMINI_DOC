from google.adk.agents import Agent
from google.adk.tools import google_search  
from google.adk.models.lite_llm import LiteLlm

root_agent = Agent(
   model=LiteLlm(model="ollama_chat/qwen3:0.6b"),
   name="basic_search_agent",
   description="Agent to answer questions using Google Search.",
   instruction="You are an expert researcher. You always stick to the facts.",
   tools=[google_search]
)