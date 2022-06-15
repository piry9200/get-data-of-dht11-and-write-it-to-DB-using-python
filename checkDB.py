import sqlite3
DATABASE = "dateTempHumi.db"

conn = sqlite3.connect(DATABASE)
cur = conn.cursor()

cur.execute("SELECT * FROM data")
dates = cur.fetchall()
print(dates)

cur.execute("SELECT COUNT(*) FROM data")
count = cur.fetchall()
print(f"行数:{count[0][0]}")