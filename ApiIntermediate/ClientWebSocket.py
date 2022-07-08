import ast
import websockets
import requests
from dotenv import load_dotenv
from os import getenv
from utils.logger_base import log
from requests.structures import CaseInsensitiveDict
from busypie import wait, SECOND

load_dotenv()
URL_SEND = getenv("URL_CRUD")
URL_WEBSOCKET = getenv("URL_WEBSOCKET")
SECRET = getenv("SECRET_WEBSOCKET")
USERNAME = getenv("SUPERADMIN")
PASSWORD = getenv("PSWD_ADMIN")


def request_token():
    headers_get = CaseInsensitiveDict()
    print(USERNAME)
    print(PASSWORD)
    headers_get["username"] = "admin"
    headers_get["password"] = "admin123"
    response_token = requests.get(URL_SEND + "token/", headers=headers_get)
    log.debug(response_token.json())
    return response_token


async def save_register_with_device():
    await_token()
    token = dict(request_token().json())
    async with websockets.connect(URL_WEBSOCKET, extra_headers={"Authorization": SECRET}) as websocket:
        headers = CaseInsensitiveDict()
        headers["Authorization"] = f"Bearer {token['token']}"
        while True:
            message = await websocket.recv()
            js = ast.literal_eval(message)
            x = requests.post(URL_SEND, json=js, headers=headers)
            log.debug(x.status_code)
            log.debug(x.text)


def await_token():
    wait().at_most(15, SECOND).poll_interval(3, SECOND).with_description('dont get the token').until(
        lambda: request_token().status_code == 200)
