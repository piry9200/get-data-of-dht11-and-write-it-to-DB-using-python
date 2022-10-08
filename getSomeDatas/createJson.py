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
	dictOftemp[i] = str(temps[i][0]) + '°C'

dictOfhumi = {}
for i in range(0, numOftemp[0][0]):
	dictOfhumi[i] = str(humis[i][0]) + '%'

print(dictOfdate)
print(dictOftemp)
print(dictOfhumi)

with open("/home/pi/pri_prg/dht11_python_db/getSomeDatas/jsonOfdate.json","w")as f:
	json.dump(dictOfdate, f, ensure_ascii=False, indent=4)

with open("/home/pi/pri_prg/dht11_python_db/getSomeDatas/jsonOftemp.json","w")as f:
        json.dump(dictOftemp, f, ensure_ascii=False, indent=4)

with open("/home/pi/pri_prg/dht11_python_db/getSomeDatas/jsonOfhumi.json","w")as f:
        json.dump(dictOfhumi, f, ensure_ascii=False, indent=4)  