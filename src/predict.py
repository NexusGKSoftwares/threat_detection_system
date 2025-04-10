import joblib
import pandas as pd

def load_model():
    model = joblib.load('models/threat_model.pkl')
    scaler = joblib.load('models/scaler.pkl')
    return model, scaler

def predict_realtime(new_data_path):
    df = pd.read_csv(new_data_path)
    model, scaler = load_model()
    
    X_scaled = scaler.transform(df)
    predictions = model.predict(X_scaled)
    df['anomaly'] = predictions
    df['anomaly'] = df['anomaly'].apply(lambda x: "Anomaly" if x == -1 else "Normal")
    df.to_csv("data/preprocessed/predictions.csv", index=False)
    print("[+] Predictions saved.")

