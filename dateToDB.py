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

id = 1
DATABASE = "dateTempHumi.db"

conn = sqlite3.connect(DATABASE)
cur = conn.cursor()
cur.execute("CREATE TABLE IF NOT EXISTS data (id,date, temp, humi)")

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