import paho.mqtt.client as mqtt
import time
import json
import random

BROKER = "localhost"
PORT = 1883
TOPIC = "iot/sensor/data"

client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)

# Try connecting until broker is available
while True:
    try:
        client.connect(BROKER, PORT, 60)
        print("Connected to MQTT Broker!")
        break
    except:
        print("Broker not available, retrying in 3 seconds...")
        time.sleep(3)

print("IoT Device Simulator Started...")

while True:
    data = {
        "temperature": round(random.uniform(20, 40), 2),
        "humidity": round(random.uniform(40, 80), 2),
        "vibration": round(random.uniform(0.0, 1.0), 3)
    }

    payload = json.dumps(data)
    client.publish(TOPIC, payload)

    print(f"Sent: {payload}")
    time.sleep(3)
