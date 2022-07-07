from sqlalchemy import Table, Column, String, TIMESTAMP, FLOAT, Integer
from config.DbHandler import meta, engine

MeasureDao = Table('register', meta,
                   Column('id', Integer, primary_key=True, autoincrement=True),
                   Column('Device', String(255)),
                   Column('Measure', String(255)),
                   Column('Magnitude', FLOAT),
                   Column('Timestamp', TIMESTAMP)
                   )

meta.create_all(engine)
