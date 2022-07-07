from dotenv import load_dotenv
from jwt import encode, decode, exceptions
from datetime import datetime, timedelta
from os import getenv
from fastapi.responses import JSONResponse

load_dotenv()


def get_token(data: dict):
    return encode(payload={**data}, key=getenv('SECRET'), algorithm="HS256")


def validate_token(token, output=False):
    try:
        if output:
            return decode(token, key=getenv("SECRET"), algorithms="HS256")
        decode(token, key=getenv("SECRET"), algorithms="HS256")
    except exceptions.DecodeError:
        return JSONResponse(content={"message": "invalid token"}, status_code=401)
    except exceptions.ExpiredSignatureError:
        return JSONResponse(content={"message": "token expired"}, status_code=401)
