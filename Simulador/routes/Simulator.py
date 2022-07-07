from fastapi import APIRouter, WebSocket, Depends, Header
from starlette import status
from utils.ElectronicDevice import ElectronicDevice
from dotenv import load_dotenv
from os import getenv

load_dotenv()
secret = getenv("SECRET_KEY")
simulator = APIRouter()


async def validate_token(websocket: WebSocket, Authorization: str = Header(None)):
    if Authorization is None:
        await websocket.close(code=status.WS_1008_POLICY_VIOLATION)
    elif Authorization != secret:
        await websocket.close(code=status.WS_1008_POLICY_VIOLATION)
    else:
        return Authorization


@simulator.websocket('/metrics')
async def websocket_send_metric(websocket: WebSocket, Authorization: str = Depends(validate_token)):
    await websocket.accept()
    electronic = ElectronicDevice()
    while True:
        data = electronic.generateValue()
        await websocket.send_text(str(data))
