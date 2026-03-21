from google.adk.agents import LlmAgent  
from google.adk.models.lite_llm import LiteLlm  
  
root_agent = LlmAgent(  
    name="qwen_agent",  
    model=LiteLlm(model="ollama_chat/qwen3:0.6b"),  
    instruction="You are a helpful assistant.",  
)

