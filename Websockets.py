
import asyncio
import websockets
import time

async def packet_latency():
    uri = "ws://echo.websocket.org"  # Replace with your WebSocket server URI
    
    async with websockets.connect(uri) as websocket:
        while True:
            message = await websocket.recv()
            timestamp = int(message)
            current_time = int(time.time() * 1000)  # Convert to milliseconds
            latency = current_time - timestamp
            print(f"Packet Latency: {latency} ms")

if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(packet_latency())
