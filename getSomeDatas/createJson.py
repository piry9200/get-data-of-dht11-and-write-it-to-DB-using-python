import sqlite3
import json
DATABASE = "/home/pi/pri_prg/dht11_python_db/getSomeDatas/dateTempHumi.db"

dic = {}
conn = sqlite3.connect(DATABASE)
cur = conn.cursor()

cur.execute("SELECT date FROM data")
dates = cur.fetchall()
cur.execute("SELECT COUNT(date) FROM data")
numOfdate = cur.fetchall()

cur.execute("SELECT temp FROM data")
temps = cur.fetchall()
cur.execute("SELECT COUNT(temp) FROM data")
numOftemp = cur.fetchall()

cur.execute("SELECT humi FROM data")
humis = cur.fetchall()
cur.execute("SELECT COUNT(humi) FROM data")
numOfhumi = cur.fetchall()

dictOfdate = {}
for i in range(0,numOfdate[0][0]):
	dictOfdate[i] = dates[i][0]

dictOftemp = {}
for i in range(0, numOftemp[0][0]):
	dictOftemp[i] = temps[i][0]

dictOfhumi = {}
for i in range(0, numOftemp[0][0]):
	dictOfhumi[i] = humis[i][0]

print(dates)
print(temps)
print(humis)
print()
print(dictOfdate)
print(dictOftemp)
print(dictOfhumi)