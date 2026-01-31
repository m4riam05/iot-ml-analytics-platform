import pandas as pd
import random
from sklearn.ensemble import IsolationForest
import joblib

# Generate fake normal data
data = {
    "temperature": [random.uniform(22, 32) for _ in range(500)],
    "humidity": [random.uniform(45, 65) for _ in range(500)],
    "vibration": [random.uniform(0.1, 0.5) for _ in range(500)]
}

df = pd.DataFrame(data)

model = IsolationForest(contamination=0.05)
model.fit(df)

joblib.dump(model, "anomaly_model.pkl")
print("Model trained and saved!")
