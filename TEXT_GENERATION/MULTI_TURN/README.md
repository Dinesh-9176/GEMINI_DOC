# Multi-Turn Chat

This folder contains an example (`multi-turn.py`) of creating a stateful conversation with the Gemini API.

## Overview
Using `client.chats.create()`, the script automatically manages the history of a conversation. It demonstrates sending sequential messages and retrieving the whole chat history, allowing the model to recall previous turns (e.g., remembering "2 dogs").

## Usage
Run the script using `uv` from the project root:
```bash
uv run TEXT_GENERATION/MULTI_TURN/multi-turn.py
```
