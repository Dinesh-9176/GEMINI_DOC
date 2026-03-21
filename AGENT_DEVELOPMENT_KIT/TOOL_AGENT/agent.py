from google.adk.agents import LlmAgent  
from google.adk.models.lite_llm import LiteLlm  


def get_capital_city(country: str) -> str:
  """Retrieves the capital city for a given country."""

  capitals = {"france": "Paris", "japan": "Tokyo", "canada": "Ottawa"}
  return capitals.get(country.lower(), f"Sorry, I don't know the capital of {country}.")


root_agent = LlmAgent(
    model=LiteLlm(model="ollama_chat/qwen3:0.6b"),
    name="TOOL_AGENT",
    enable_thinking=True,
    description="Answers user questions about the capital city of a given country.",
    instruction="""You are a rigid tool-testing agent. 
    1. You MUST call the get_capital_city tool for EVERY country mentioned.
    2. If the tool returns "Sorry, I don't know...", you MUST repeat that exact message to the user.
    3. NEVER provide a capital city from your own memory, even if you are 100% sure of it.
    4. If it's not in the tool, you don't know it. Period.""",
    tools=[get_capital_city] 
)