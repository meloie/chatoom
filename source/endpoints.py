import asyncio
import aioredis

from starlette.websockets import WebSocket, WebSocketDisconnect
from starlette.authentication import requires

from . import settings


@requires("authenticated")
async def chat_room(websocket: WebSocket) -> None:
    await websocket.accept()
    name = websocket.user.username
    try:
        await asyncio.gather(
            send_messages(name, websocket), recieve_messages(websocket)
        )
    except (EOFError, WebSocketDisconnect):
        await websocket.close()


async def send_messages(name: str, websocket: WebSocket):
    redis = await aioredis.create_redis(settings.REDIS_URL)
    while True:
        msg = await websocket.receive_text()
        if not msg:
            raise EOFError("exit msg")
        await redis.publish_json("channel", {"name": name, "msg": msg})


async def recieve_messages(websocket: WebSocket):
    redis = await aioredis.create_redis(settings.REDIS_URL)
    subscriber = await redis.subscribe("channel")
    channel = subscriber[0]
    while True:
        msg = await channel.get_json()
        await websocket.send_text(f'{msg["name"]}: {msg["msg"]}')
