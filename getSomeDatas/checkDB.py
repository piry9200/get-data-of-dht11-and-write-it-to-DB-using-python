import sqlite3
DATABASE = "/home/pi/pri_prg/dht11_python_db/getSomeDatas/dateTempHumi.db"

conn = sqlite3.connect(DATABASE)
cur = conn.cursor()

cur.execute("SELECT * FROM data")
dates = cur.fetchall()
for date in dates:
    print(date)

cur.execute("SELECT COUNT(*) FROM data")
count = cur.fetchall()
print(f"行数:{count[0][0]}")

conn.close()