# Streaming Output

This folder demonstrates how to stream responses (`stream.py`) from the Gemini API using `generate_content_stream`.

## Overview
Streaming is useful for minimizing perceived latency. Instead of waiting for the entire response to load, the script iterates over the incoming stream and prints partial responses (chunks) in real-time.

## Usage
Run the script using `uv` from the project root:
```bash
uv run TEXT_GENERATION/STREAMING/stream.py
```
