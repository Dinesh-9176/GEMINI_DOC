# Session Management

This folder contains an example (`session_resumption.py`) of using **session resumption** with the Gemini Live API.

## Overview
The script demonstrates how to resume a previous Live API session using a session handle. This allows conversations to be paused and continued later without losing context. The server periodically sends resumption updates containing a handle that can be saved and reused.

## Usage
Run the script using `uv` from the project root:
```bash
uv run LIVE_API/SESSION_MANAGEMENT/session_resumption.py
```
