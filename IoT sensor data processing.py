"""
IoT Sensor Data Processing Pipeline
Author: Gayatri

This script simulates real-time temperature sensor data,
stores it in a SQLite database, and performs basic anomaly detection.
"""

import pandas as pd
import sqlite3
import random
import time


def generate_sensor_data():
    """Simulate sensor temperature data."""
    temperature = random.uniform(20.0, 30.0)

    # Inject anomaly with 10% probability
    if random.random() < 0.1:
        temperature += random.uniform(10.0, 20.0)

    return {
        "timestamp": pd.Timestamp.now().isoformat(),
        "temperature": round(temperature, 2)
    }


def create_database(db_name="sensor_data.db"):
    """Create SQLite database and table."""
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS sensor_readings (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            timestamp TEXT,
            temperature REAL
        )
    """)

    conn.commit()
    return conn


def insert_data(conn, data):
    """Insert sensor data into database."""
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO sensor_readings (timestamp, temperature)
        VALUES (?, ?)
    """, (data["timestamp"], data["temperature"]))
    conn.commit()


def detect_anomalies(df, threshold=28.0):
    """Detect temperature anomalies."""
    return df[df["temperature"] > threshold]


def main():
    conn = create_database()

    print("Starting IoT Sensor Data Processing...")
    print("Press CTRL+C to stop.\n")

    try:
        while True:
            sensor_data = generate_sensor_data()
            insert_data(conn, sensor_data)

            print("Inserted:", sensor_data)

            df = pd.read_sql("SELECT * FROM sensor_readings", conn)
            anomalies = detect_anomalies(df)

            if not anomalies.empty:
                print("\n⚠️ Anomalies detected:")
                print(anomalies.tail(), "\n")

            time.sleep(5)

    except KeyboardInterrupt:
        print("\nStopping the data processing pipeline.")

    finally:
        conn.close()
        print("Database connection closed.")


if __name__ == "__main__":
    main()
