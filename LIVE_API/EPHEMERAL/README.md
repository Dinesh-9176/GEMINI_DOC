# Ephemeral Tokens

This folder contains an example (`ephemeral_creation.py`) of creating **ephemeral authentication tokens** for the Gemini Live API.

## Overview
The script generates a short-lived, single-use token that can be safely passed to a client application (e.g., a browser) to start a Live API session without exposing your main API key. The token is configured with usage limits and expiration times for security.

## Usage
Run the script using `uv` from the project root:
```bash
uv run LIVE_API/EPHEMERAL/ephemeral_creation.py
```
