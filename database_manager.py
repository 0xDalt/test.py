import sqlite3
import psutil
import time
from datetime import datetime
import os

# 1. Force the database to be in the EXACT same folder as this script
folder = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(folder, "monitor_data.db")

connection = sqlite3.connect(db_path)
cursor = connection.cursor()

# 2. We use 'v2_stats' to ensure we aren't using an old, broken table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS v2_stats (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        timestamp TEXT,
        cpu_usage REAL
    )
''')
connection.commit()

print(f"--- Saving to: {db_path} ---")
print("--- Logging started (Ctrl+C to stop) ---")

try:
    while True:
        cpu = psutil.cpu_percent(interval=1)
        now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        # 3. The column name 'cpu_usage' MUST match the CREATE TABLE above
        cursor.execute(
            "INSERT INTO v2_stats (timestamp, cpu_usage) VALUES (?, ?)", 
            (now, cpu)
        )
        connection.commit()

        print(f"[{now}] Logged: {cpu}%")
        time.sleep(5)

except KeyboardInterrupt:
    print("\n--- Stopping... ---")
    connection.close()
