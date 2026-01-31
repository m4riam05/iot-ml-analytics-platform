from fastapi import FastAPI
from app.mqtt_client import start_mqtt
from app.database import engine, Base

app = FastAPI()

@app.on_event("startup")
def startup_event():
    Base.metadata.create_all(bind=engine)
    start_mqtt()

@app.get("/")
def read_root():
    return {"message": "IoT ML Backend Running"}
