from fastapi import FastAPI, WebSocket
from dotenv import load_dotenv
from os import getenv
from ClientWebSocket import save_register_with_device
app = FastAPI()
load_dotenv()
URL_WEBSOCKET = getenv("URL_WEBSOCKET")


@app.on_event('startup')
async def connect_with_websocket():
    await save_register_with_device()
