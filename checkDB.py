import sqlite3
DATABASE = "dateTempHumi.db"

conn = sqlite3.connect(DATABASE)
cur = conn.cursor()

cur.execute("SELECT * FROM data")
dates = cur.fetchall()
print(dates)