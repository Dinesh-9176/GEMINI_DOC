import asyncio
import websockets

async def chat():

    uri = "ws://localhost:8765"

    async with websockets.connect(uri, ping_timeout=None) as websocket:

        while True:

            message = input("You: ")

            await websocket.send(message)

            print("AI: ", end="", flush=True)

            while True:

                response = await websocket.recv()

                if response == "[END]":
                    print()
                    break

                print(response, end="", flush=True)

asyncio.run(chat())