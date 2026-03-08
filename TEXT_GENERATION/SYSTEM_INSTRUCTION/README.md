# System Instructions

This folder shows how to configure the model's behavior using system instructions (`system_ins.py`).

## Overview
By utilizing `GenerateContentConfig(system_instruction=...)`, we instruct the `gemini-2.5-flash` model to adopt a specific persona—in this case, acting as a cat named "Neko". This heavily influences all generated text.

## Usage
Run the script using `uv` from the project root:
```bash
uv run TEXT_GENERATION/SYSTEM_INSTRUCTION/system_ins.py
```
