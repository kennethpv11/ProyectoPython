import sqlalchemy
from fastapi import FastAPI
from routes.CrudSimulador import simulator
from config.DbHandler import conn
from models.Dao.AdminDao import admin
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


def insert_admin():
    try:
        data = {'user': USER, 'password': PASSWORD}
        conn.execute(admin.insert().values(data))
        return True
    except sqlalchemy.exc as e:
        return False
    except Exception:
        return False


@app.on_event('startup')
def create_admin():
    result = False
    while result:
        result = insert_admin()
