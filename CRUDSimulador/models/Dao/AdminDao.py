from sqlalchemy import Table, Column, String
from config.DbHandler import meta, engine

admin = Table('loging', meta,
              Column('user', String(255), unique=True, nullable=False),
              Column('password',String(255) , nullable=False)
              )

meta.create_all(engine)


