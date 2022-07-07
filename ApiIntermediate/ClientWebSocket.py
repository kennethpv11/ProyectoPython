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


async def request_token():
    headers_get = CaseInsensitiveDict()
    print(USERNAME)
    print(PASSWORD)
    headers_get["username"] = "admin"
    headers_get["password"] = "admin123"
    response_token = requests.get(URL_SEND + "token/", headers=headers_get)
    log.debug(response_token)
    return dict(response_token.json())


async def save_register_with_device():
    token = await request_token()
    async with websockets.connect(URL_WEBSOCKET, extra_headers={"Authorization": SECRET}) as websocket:
        headers = CaseInsensitiveDict()
        headers["Authorization"] = f"Bearer {token['token']}"
        while True:
            message = await websocket.recv()
            js = ast.literal_eval(message)
            x = requests.post(URL_SEND, json=js, headers=headers)
            log.debug(x.status_code)
            log.debug(x.text)
