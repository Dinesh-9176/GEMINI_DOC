from google.adk.agents import Agent
from google.adk.models.lite_llm import LiteLlm

import random

# Tool 1: Roll Dice (8 sides)
def roll_die() -> int:
    """Roll an 8-sided die and return the result."""
    return random.randint(1, 8)


# Tool 2: Check Prime
def check_prime(number: int) -> str:
    """Check if a number is prime."""
    if number < 2:
        return f"{number} is not a prime number"

    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return f"{number} is not a prime number"

    return f"{number} is a prime number"


# Agent Definition
root_agent = Agent(
    model=LiteLlm(model="ollama_chat/gemma3:latest"),
    name="dice_agent",
    description=(
        "An agent that can roll an 8-sided dice and check prime numbers."
    ),
    instruction="""
You are a smart assistant.

- If user asks to roll a dice → use roll_die
- If user asks about prime → use check_prime
- Always explain results clearly
""",
    tools=[roll_die, check_prime],
)


# Run Agent
if __name__ == "__main__":
    print("Dice Agent Running (type 'exit' to quit)\n")

    while True:
        user_input = input("You: ")

        if user_input.lower() == "exit":
            break

        response = root_agent.invoke(user_input)

        print("Agent:", response)