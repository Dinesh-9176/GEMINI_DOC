# WebSocket Streaming Server

This folder contains an example (`websocket.py`) of a real-time AI chat server using WebSockets and the OpenAI-compatible API (via Ollama).

## Overview
The script starts a WebSocket server on `ws://localhost:8765`. When a client connects and sends a message, the server streams the AI response back token-by-token in real-time, sending an `[END]` marker when the response is complete. It uses the `qwen3:0.6b` model through Ollama's local API.

## Usage
Run the script using `uv` from the project root:
```bash
uv run LIVE_API/WEBSOCKETS/websocket.py
```
