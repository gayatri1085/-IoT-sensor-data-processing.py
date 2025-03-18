1. Imports `pandas`, `sqlite3`, `random`, and `time` to handle data, database operations, sensor simulation, and periodic execution.  

2. Generates random temperature readings between **20°C and 30°C**, with a **10% chance of an anomaly** where the temperature spikes by 10-20°C.  

3. Creates an SQLite database (`sensor_data.db`) and a table `sensor_readings` to store timestamps and temperature readings if it does not already exist.  

4. Inserts new sensor data into the database using SQL queries, ensuring each reading is recorded with a timestamp.  

5. Fetches all stored temperature readings and detects anomalies by filtering values **above 28°C** for abnormal conditions.  

6. Runs an **infinite loop** that generates, stores, and analyzes sensor data, updating every **5 seconds** to simulate real-time monitoring.  

7. Uses `pandas.read_sql_query()` to retrieve sensor readings from the database and process them for anomaly detection.  

8. Prints detected anomalies when temperature readings exceed **28°C**, providing real-time alerts of unusual conditions.  

9. Handles **keyboard interrupts (Ctrl+C)** gracefully by stopping the loop and closing the database connection safely.  

10. Ensures the script runs **only when executed directly**, preventing unintended execution when imported into other programs.
