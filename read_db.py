import sqlite3
import os

# Make sure we look in the same folder
folder = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(folder, "monitor_data.db")

connection = sqlite3.connect(db_path)
cursor = connection.cursor()

# Query the NEW table name 'v2_stats'
cursor.execute("SELECT COUNT(*) FROM v2_stats")
count = cursor.fetchone()[0]

cursor.execute("SELECT MAX(cpu_usage) FROM v2_stats")
max_val = cursor.fetchone()[0]

print(f"✅ Verified: {count} logs found in the database.")
print(f"🔥 Peak CPU recorded: {max_val}%")

connection.close()
