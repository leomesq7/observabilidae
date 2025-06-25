import re
from datetime import datetime
import numpy as np
from sklearn.ensemble import IsolationForest
import pandas as pd

LOG_FILE = 'data/app.log'

def preprocess_logs():
    data = []
    log_pattern = r'(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}) (\w+) (.+)'
    
    with open(LOG_FILE, 'r') as file:
        for line in file:
            match = re.match(log_pattern, line)
            if match:
                timestamp_str, level, message = match.groups()
                timestamp = datetime.strptime(timestamp_str, '%Y-%m-%d %H:%M:%S')
                hour = timestamp.hour
                level_num = {"INFO": 0, "DEBUG": 1, "WARN": 2, "ERROR": 3}.get(level, -1)
                message_length = len(message)
                slow_query = int('Query executed in' in message and int(message.split()[-1][:-2]) > 100)
                data.append([hour, level_num, message_length, slow_query])
    
    df = pd.DataFrame(data, columns=['hour', 'level_num', 'message_length', 'slow_query'])
    return df

def detect_anomalies(df):
    model = IsolationForest(contamination=0.05, random_state=42)
    model.fit(df)
    anomalies = model.predict(df)
    anomaly_indices = np.where(anomalies == -1)[0]
    anomaly_logs = df.iloc[anomaly_indices]
    return anomaly_logs

def analyze_logs():
    df = preprocess_logs()
    anomaly_logs = detect_anomalies(df)

    print("\n=== Detected Anomalies ===")
    if not anomaly_logs.empty:
        for index, row in anomaly_logs.iterrows():
            print(f"Anomaly at hour {row['hour']}: Level {row['level_num']}, Message Length {row['message_length']}, Slow Query {row['slow_query']}")
    else:
        print("No anomalies detected.")
    
    print("\n=== Log Summary ===")
    print(df.describe())

if __name__ == '__main__':
    analyze_logs()
