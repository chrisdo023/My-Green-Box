import Adafruit_DHT, requests, time, datetime

DHT_SENSOR = Adafruit_DHT.DHT22
DHT_PIN = 4

while True:
    humidity, temperature = Adafruit_DHT.read_retry(DHT_SENSOR, DHT_PIN)

    if humidity is not None and temperature is not None:
        print("Temp={0:0.1f}*C  Humidity={1:0.1f}%".format(temperature, humidity))
        try:
            data = {
                'Temperature': int("{0:0.1f}".format(temperature)),
                'Humidity': int("{0:0.1f}".format(humidity)),
                'CreatedAt': datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            }
            response = requests.post('http://127.0.0.1:5000/post', data=data)

            log = "[" + datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") + "] - " + json.loads(response.text)["status"] +"\n"
        except:
            log = "[" + datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") + "] - Failed send temperature and humidity data" + "\n"
        finally:
            f = open("DHT22-Log.txt", "a")
            f.write(log)
            f.close()        
    else:
        f = open("DHT22-Log.txt", "a")
        f.write("[" + datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") + "] - Failed to retrieve data from temperature and humidity sensor")
        f.close()