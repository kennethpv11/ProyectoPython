from fastapi import FastAPI
from routes.CrudSimulador import simulator
from dotenv import load_dotenv
from os import getenv
from utils.jwt.jwt_handler import get_token
from routes.token import token

load_dotenv()
USER = getenv("SUPERADMIN")
PASSWORD = get_token({'password': getenv("PSWD_ADMIN")})
app = FastAPI()
app.include_router(simulator)
app.include_router(token, prefix='/token')



