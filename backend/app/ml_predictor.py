import joblib
import numpy as np

model = joblib.load("anomaly_model.pkl")

def predict_anomaly(data):
    values = np.array([[data["temperature"], data["humidity"], data["vibration"]]])
    prediction = model.predict(values)[0]
    return "ANOMALY" if prediction == -1 else "NORMAL"
