import RPi.GPIO as GPIO
from DHT11 import dht11
import time
import datetime
import sqlite3

# initialize GPIO
GPIO.setwarnings(True)
GPIO.setmode(GPIO.BCM)

# read data using pin 14
instance = dht11.DHT11(pin=14)

DATABASE = "/var/www/html/dht11_python_db/getSomeDatas/dateTempHumi.db"

conn = sqlite3.connect(DATABASE)
cur = conn.cursor()
#----起動時DB作成---
cur.execute("CREATE TABLE IF NOT EXISTS data (id,date, temp, humi)")
#----起動時のDBの行数を取得---
cur.execute("SELECT COUNT(*) FROM data")
numOfRecords = cur.fetchall() #numOfRecordsに現在のレコード数を代入
id = numOfRecords[0][0] + 1 #次にインサートする時のid番号を設定
now = datetime.datetime.now()

try:
	result = instance.read()
	if result.is_valid(): #DHT11から正しくデータを取得できたら
		print("Last valid input: " + str(datetime.datetime.now()))
		print("Temperature: %-3.1f C" % result.temperature)
		print("Humidity: %-3.1f %%" % result.humidity)
        #----DBの行数を取得---
        cur.execute("SELECT COUNT(*) FROM data")
        numOfRecords = cur.fetchall() #numOfRecordsに現在のレコード数を代入
        if numOfRecords[0][0] < 720: #-----行数が720未満だったら普通にデータをインサート-----
            cur.execute("INSERT INTO data VALUES (?, ?, ?, ?)", [id, now.strftime("%H:%M"), result.temperature, result.humidity]])
            id = id + 1
            conn.commit()
        else: #----既に行数が720ある場合---
            id = 720
            cur.execute("DELETE FROM data WHERE id=1") #idが１の行を削除
            for i in range(1,720): #-----idを前に詰める----
                cur.execute("UPDATE data SET id = ? WHERE id= ?", [i, i+1])
            cur.execute("INSERT INTO data VALUES (?, ?, ?, ?)", [id, now.strftime("%H:%M"), result.temperature, result.humidity])
            conn.commit()

except KeyboardInterrupt:
	print("Cleanup")
	GPIO.cleanup()

conn.close()