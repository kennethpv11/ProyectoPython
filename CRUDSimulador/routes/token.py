from fastapi import APIRouter, Header
from fastapi.responses import JSONResponse
from config.DbHandler import conn
from models.Dao.AdminDao import admin
from utils.jwt.jwt_handler import validate_token, get_token
from starlette.status import HTTP_200_OK, HTTP_403_FORBIDDEN

token = APIRouter()


@token.get("/")
def generate_token(username: str = Header(None), password: str = Header(None)):
    if username == None or password == None:
        return JSONResponse(status_code=HTTP_403_FORBIDDEN, content="forhiben")
    else:
        result = conn.execute(admin.select().where(admin.c.user == username)).first()
        if result:
            response = validate_token(result[1], output=True)
            if isinstance(response, JSONResponse):
                return response
            else:
                if response['password'] == password:
                    return JSONResponse(status_code=HTTP_200_OK, content={"token": get_token({'password': password})})
                else:
                    return JSONResponse(status_code=HTTP_403_FORBIDDEN, content="forhiben")
        else:
            return JSONResponse(status_code=HTTP_403_FORBIDDEN, content="forhiben")
