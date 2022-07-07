from fastapi import FastAPI
from routes.Simulator import simulator

app = FastAPI()
app.include_router(simulator)
