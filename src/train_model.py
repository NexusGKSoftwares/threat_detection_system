from sklearn.ensemble import IsolationForest
from sklearn.preprocessing import StandardScaler
import joblib

def train_model(dataframe):
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(dataframe)

    model = IsolationForest(n_estimators=100, contamination=0.05)
    model.fit(X_scaled)

    joblib.dump(model, 'models/threat_model.pkl')
    joblib.dump(scaler, 'models/scaler.pkl')
    print("[+] Model and scaler saved.")
