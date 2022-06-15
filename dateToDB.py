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

DATABASE = "dateTempHumi.db"

conn = sqlite3.connect(DATABASE)
cur = conn.cursor()
cur.execute("CREATE TABLE IF NOT EXISTS data (id,date, temp, humi)") #初回時テーブル作成

cur.execute("SELECT COUNT(*) FROM data")
count_row = cur.fetchall() #行数を取得　リストにタプルが入っている形式で取得
if count_row[0][0] == 0: #行数が0(初回時)だったらidは1から始める。
	id = 1
else: #すでにデータがあるときは既にある行数に1を足した行数からデータを入力
	id = count_row[0][0] + 1

try:
	while True:
		result = instance.read()
		if result.is_valid():
			print("Last valid input: " + str(datetime.datetime.now()))
			print("Temperature: %-3.1f C" % result.temperature)
			print("Humidity: %-3.1f %%" % result.humidity)
			cur.execute(f"INSERT INTO data VALUES (?, ?, ?, ?)", [id, str(datetime.datetime.now()), result.temperature, result.humidity])
			id = id + 1
			conn.commit()

	time.sleep(6)

except KeyboardInterrupt:
	print("Cleanup")
	GPIO.cleanup()

conn.close()