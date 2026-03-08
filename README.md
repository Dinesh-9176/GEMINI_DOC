# Gemini API Quick Start

This repository contains practical examples for the **Text Generation** capabilities of the Gemini API completed today.

## Getting Started

### 1. Clone the Repository
```bash
git clone <your-repository-url>
cd GEMINI_QUICK_START
```

### 2. Environment Setup
You will need a Gemini API key. Create a `.env` file in the root directory and add your key:
```ini
GEMINI_API_KEY=your_api_key_here
```

### 3. Install Packages
This project uses `uv` for lightning-fast dependency management. To install the required packages (`google-genai`, `logging`, `pillow`, `python-dotenv`), run:
```bash
uv sync
```

Alternatively, commands can be launched directly via `uv run` which handles dependencies automatically:
```bash
uv run TEXT_GENERATION/CLI_MODEL/gemini_cli.py
```

## Folder Structure

- `TEXT_GENERATION/`
  - `CLI_MODEL/`: Interactive console application combining chat, vision, and reasoning capabilities.
  - `MULTIMODAL/`: Examples for generating text from multimodal inputs (text + images).
  - `MULTI_TURN/`: Examples for maintaining conversation history for chat interactions.
  - `STREAMING/`: Examples for receiving responses in real-time chunks.
  - `SYSTEM_INSTRUCTION/`: Examples for setting system-level behavior guidelines for the model.
  - `THINKING/`: Examples for utilizing the model's built-in reasoning and thinking capabilities.
