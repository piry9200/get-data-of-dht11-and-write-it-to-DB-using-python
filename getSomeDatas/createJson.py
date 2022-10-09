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

dictOfDate = {}
for i in range(0,numOfdate[0][0]):
	dictOfDate[i] = dates[i][0]

dictOfTemp = {}
for i in range(0, numOftemp[0][0]):
	dictOfTemp[i] = str(temps[i][0]) + '°C'

dictOfHumi = {}
for i in range(0, numOftemp[0][0]):
	dictOfHumi[i] = str(humis[i][0]) + '%'

# dictOfAll={date : dictOfDate,         {[date、temperature、humidityをキーにもち]、[それぞれの要素に「idをキーに持ち,値を要素として持つ」オブジェクト]}
#            temperature : dictOfTemp
#            humidity : dictOfHumi
#           }
# with open("/home/pi/pri_prg/dht11_python_db/getSomeDatas/jsonOfAll.json","w")as f:
#	json.dump(dictOfAll, f, ensure_ascii=False, indent=4)

print(dictOfDate)
print(dictOfTemp)
print(dictOfHumi)

with open("/home/pi/pri_prg/dht11_python_db/getSomeDatas/jsonOfdate.json","w")as f:
	json.dump(dictOfDate, f, ensure_ascii=False, indent=4)

with open("/home/pi/pri_prg/dht11_python_db/getSomeDatas/jsonOftemp.json","w")as f:
        json.dump(dictOfTemp, f, ensure_ascii=False, indent=4)

with open("/home/pi/pri_prg/dht11_python_db/getSomeDatas/jsonOfhumi.json","w")as f:
        json.dump(dictOfHumi, f, ensure_ascii=False, indent=4)  