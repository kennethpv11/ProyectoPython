import ast
import websockets
import requests
from dotenv import load_dotenv
from os import getenv
from utils.logger_base import log
from requests.structures import CaseInsensitiveDict

load_dotenv()
URL_SEND = getenv("URL_CRUD")
URL_WEBSOCKET = getenv("URL_WEBSOCKET")
SECRET = getenv("SECRET_WEBSOCKET")
USERNAME = getenv("SUPERADMIN")
PASSWORD = getenv("PSWD_ADMIN")


def request_token():
    try:
        headers_get = CaseInsensitiveDict()
        headers_get["username"] = "admin"
        headers_get["password"] = "admin123"
        response_token = requests.get(URL_SEND + "token/", headers=headers_get)

        return dict(response_token.json())
    except Exception:
        return None


async def save_register_with_device():
    async with websockets.connect(URL_WEBSOCKET, extra_headers={"Authorization": SECRET}) as websocket:
        token = None
        while token is None:
            token = request_token()
            
        headers = CaseInsensitiveDict()
        headers["Authorization"] = f"Bearer {token['token']}"
        while True:
            message = await websocket.recv()
            js = ast.literal_eval(message)
            x = requests.post(URL_SEND, json=js, headers=headers)
            log.debug(x.status_code)
            log.debug(x.text)
