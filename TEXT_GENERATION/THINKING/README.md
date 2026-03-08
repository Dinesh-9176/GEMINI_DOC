# Model Thinking Capabilities

This folder contains an example (`thinking.py`) demonstrating how to extract the intermediate reasoning from the model before it produces a final answer.

## Overview
Using `ThinkingConfig(include_thoughts=True)` with the `gemini-3-flash-preview` model, the script asks a complex math question. It then separately extracts and prints the internal "Thought summary" and the final "Answer".

## Usage
Run the script using `uv` from the project root:
```bash
uv run TEXT_GENERATION/THINKING/thinking.py
```
