# Gemini API Quick Start

This repository contains practical examples for the **Text Generation** capabilities of the Gemini API completed today.

## Getting Started

### 1. Clone the Repository
```bash
git clone https://github.com/Dinesh-9176/GEMINI_DOC.git
cd GEMINI_QUICK_START
```

### 2. Environment Setup
You will need a Gemini API key. Create a `.env` file in the root directory and add your key:
```ini
GEMINI_API_KEY=your_api_key_here
```

### 3. Install Packages
This project uses `uv` for dependency management. To install the required packages (`google-genai`, `logging`, `pillow`, `python-dotenv`), run:
```bash
uv sync
```

Alternatively, commands can be launched directly via `uv run` which handles dependencies automatically:
```bash
uv run TEXT_GENERATION/CLI_MODEL/gemini_cli.py
```

## Folder Structure

- **[AGENT_DEVELOPMENT_KIT](file:///c:/Users/dines/OneDrive/Desktop/GEMINI_QUICK_START/AGENT_DEVELOPMENT_KIT/)**: Advanced multi-agent frameworks, MCP integration, and OpenAPI tools.
  - `LOOP_AGENT/`, `PARALLEL_AGENT/`, `SEQUENTIAL_AGENT/`: Multi-agent orchestration patterns.
  - `MCP_TOOLS/`, `CUSTOM_MCP_TOOLS/`: Model Context Protocol integrations.
  - `OPENAPI/`, `AUTHENTICATION/`: REST API integration and security examples.

- **[TEXT_GENERATION](file:///c:/Users/dines/OneDrive/Desktop/GEMINI_QUICK_START/TEXT_GENERATION/)**: Core Gemini text capabilities.
  - `CLI_MODEL/`: Interactive console application.
  - `MULTIMODAL/`: Text and vision combining examples.
  - `MULTI_TURN/`: Chat history and conversation persistence.
  - `STREAMING/`: Real-time response generation.
  - `THINKING/`: Utilizing built-in model reasoning.

- **[IMAGE_GENERATION](file:///c:/Users/dines/OneDrive/Desktop/GEMINI_QUICK_START/IMAGE_GENERATION/)**: Image creation and analysis.
  - `IMAGE_GENERATION/`: Generating images from text.
  - `IMAGE_UNDERSTANDING/`: Vision analysis (Object Detection, Segmentation).
  - `STRUCTURED_OUTPUT/`: Enforcing JSON responses from vision models.

- **[AUDIO_GENERATION](file:///c:/Users/dines/OneDrive/Desktop/GEMINI_QUICK_START/AUDIO_GENERATION/)**: Speech synthesis and audio processing.
  - `SINGLE_SPEAKER/`, `MULTI_SPEAKER/`: Generating audio with one or more voices.

- **[LIVE_API](file:///c:/Users/dines/OneDrive/Desktop/GEMINI_QUICK_START/LIVE_API/)**: Real-time interaction with low-latency Gemini models.
  - `GROUNDING/`, `SESSION_MANAGEMENT/`, `WEBSOCKETS/`: Advanced live session features.

- **[FASTAPI](file:///c:/Users/dines/OneDrive/Desktop/GEMINI_QUICK_START/FASTAPI/)**: Implementing RESTful APIs with FastAPI.
  - `GET/`, `POST/`, `PUT/`, `DELETE/`: Standard HTTP methods examples.

- **[PYDANTIC](file:///c:/Users/dines/OneDrive/Desktop/GEMINI_QUICK_START/PYDANTIC/)**: Data modeling and validation using Pydantic.
  - `BASIC/`, `GENERIC_MODEL/`, `NESTED_MODEL/`, `VALIDATION_ERROR/`: Comprehensive schema examples.

- **[OLLAMA](file:///c:/Users/dines/OneDrive/Desktop/GEMINI_QUICK_START/OLLAMA/)**: Running local LLMs (like Qwen) and integrating them with ADK.
