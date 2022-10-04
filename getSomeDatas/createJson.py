import sqlite3
import json
DATABASE = "/home/pi/pri_prg/dht11_python_db/getSomeDatas/dateTempHumi.db"

dic = {}
conn = sqlite3.connect(DATABASE)
cur = conn.cursor()

cur.execute("SELECT COUNT(date) FROM data")
dates = cur.fetchall()

cur.execute("SELECT COUNT(temp) FROM data")
temps = cur.fetchall()

cur.execute("SELECT COUNT(humi) FROM data")
humis = cur.fetchall()

print(dates)
print(temps)
print(humis)

