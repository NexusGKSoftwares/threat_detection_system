import pandas as pd

def preprocess_log_data(log_df):
    # Example: extracting timestamp, source IP, event type
    log_df['timestamp'] = pd.to_datetime(log_df['timestamp'])
    log_df['hour'] = log_df['timestamp'].dt.hour
    log_df['is_brute_force'] = log_df['event'].apply(lambda x: 1 if 'failed login' in x.lower() else 0)
    return log_df
