from dotenv import load_dotenv
from sqlalchemy import create_engine, MetaData
from os import getenv

load_dotenv()
engine = create_engine(
    f"{getenv('DBMS')}+{getenv('DEPENDENCY_DBMS')}://{getenv('USER')}:{getenv('PASSWORD')}@{getenv('HOST')}:{getenv('PORT')}/{getenv('DATABASE')}")

meta = MetaData()
conn = engine.connect()
