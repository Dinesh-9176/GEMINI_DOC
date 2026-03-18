import asyncio
import websockets
from openai import OpenAI

client = OpenAI(
    base_url="http://localhost:11434/v1",
    api_key="ollama"
)

async def handler(websocket):

    print("Client connected")

    async for message in websocket:

        print("User:", message)

        response = client.chat.completions.create(
            model="qwen3:0.6b",
            messages=[{"role": "user", "content": message}],
            stream=True
        )
       
        for chunk in response:

            if chunk.choices[0].delta.content:
                token = chunk.choices[0].delta.content
                await websocket.send(token)

        await websocket.send("[END]")


async def main():

    server = await websockets.serve(
        handler,
        "localhost",
        8765,
        ping_timeout=None  # prevents timeout during long generations
    )

    print("WebSocket server running on ws://localhost:8765")

    await server.wait_closed()


asyncio.run(main())