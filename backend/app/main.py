from fastapi import FastAPI
from app.mqtt_client import start_mqtt

app = FastAPI()

@app.on_event("startup")
def startup_event():
    start_mqtt()

@app.get("/")
def read_root():
    return {"message": "IoT ML Backend Running"}
