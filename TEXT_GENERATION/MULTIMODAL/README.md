# Multimodal Generation

This folder provides an example (`multimodal.py`) on how to use the Gemini API to analyze both text and images simultaneously.

## Overview
The script loads an image using `PIL.Image` and passes it alongside a text prompt (`Tell me about this image`) to the `gemini-3-flash-preview` model. 

## Usage
Run the script using `uv` from the project root:
```bash
uv run TEXT_GENERATION/MULTIMODAL/multimodal.py
```
*(Make sure to specify a valid image path inside the script before running).*
