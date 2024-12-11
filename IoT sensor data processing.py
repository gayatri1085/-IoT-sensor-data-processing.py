import pandas as pd
import sqlite3
import random
import time

def generate_sensor_data():
    temperature = random.uniform(20.0, 30.0)
    if random.random() < 0.1:
        temperature += random.uniform(10.0, 20.0)
    return {'timestamp': pd.Timestamp.now(), 'temperature': temperature}

def create_database():
    conn = sqlite3.connect('sensor_data.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS sensor_readings (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            timestamp TEXT,
            temperature REAL
        )
    ''')
    conn.commit()
    return conn

def insert_data(conn, data):
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO sensor_readings (timestamp, temperature)
        VALUES (?, ?)
    ''', (data['timestamp'], data['temperature']))
    conn.commit()

def detect_anomalies(df):
    threshold = 28.0
    anomalies = df[df['temperature'] > threshold]
    return anomalies

def main():
    conn = create_database()
    
    try:
        while True:
            sensor_data = generate_sensor_data()
            insert_data(conn, sensor_data)
            print(f"Inserted data: {sensor_data}")

            df = pd.read_sql_query("SELECT * FROM sensor_readings", conn)
            anomalies = detect_anomalies(df)
            if not anomalies.empty:
                print("Anomalies detected:")
                print(anomalies)

            time.sleep(5)

    except KeyboardInterrupt:
        print("Stopping the data processing pipeline.")
    finally:
        conn.close()

if __name__ == "__main__":
    main()