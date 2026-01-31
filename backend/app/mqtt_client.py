from app.database import SessionLocal
from app.models import SensorData
from app.ml_predictor import predict_anomaly
import paho.mqtt.client as mqtt
import json

BROKER = "localhost"
PORT = 1883
TOPIC = "iot/sensor/data"

def on_connect(client, userdata, flags, rc, properties=None):
    print("Backend connected to MQTT Broker!")
    client.subscribe(TOPIC)

def on_message(client, userdata, msg):
    data = json.loads(msg.payload.decode())
    
    status = predict_anomaly(data)
    print(f"Received Data: {data} → {status}")

    db = SessionLocal()
    sensor_entry = SensorData(
        temperature=data["temperature"],
        humidity=data["humidity"],
        vibration=data["vibration"],
        status=status
    )
    db.add(sensor_entry)
    db.commit()
    db.close()

def start_mqtt():
    client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
    client.on_connect = on_connect
    client.on_message = on_message
    client.connect(BROKER, PORT, 60)
    client.loop_start()
