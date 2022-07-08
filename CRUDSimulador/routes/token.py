from fastapi import APIRouter, Header
from fastapi.responses import JSONResponse
from utils.jwt.jwt_handler import validate_token, get_token
from starlette.status import HTTP_200_OK, HTTP_403_FORBIDDEN
from os import getenv
from dotenv import load_dotenv

load_dotenv()
token = APIRouter()


@token.get("/")
def generate_token(username: str = Header(None), password: str = Header(None)):
    if username == None or password == None:
        return JSONResponse(status_code=HTTP_403_FORBIDDEN, content="forhiben")
    else:
        if username == getenv("SUPERADMIN") and password == getenv("PSWD_ADMIN"):
            return JSONResponse(status_code=HTTP_200_OK, content={"token": get_token({'password': password})})
        else:
            return JSONResponse(status_code=HTTP_403_FORBIDDEN, content="forhiben")
