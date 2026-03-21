# Tool Agent (Strict Testing)

This module demonstrates a simple `LlmAgent` with strict instructions for tool usage.

## Features
- **Local Python Tool**: Uses a custom function (`get_capital_city`) as a tool.
- **Strict Instructions**: The agent is instructed NEVER to use its own memory and ONLY rely on the tool output for information.
- **Thinking Enabled**: Uses `enable_thinking=True` for better reasoning before tool calls.

## Example
The agent is configured to use the Qwen model via Ollama to answer questions about capital cities based on a limited local dictionary.
