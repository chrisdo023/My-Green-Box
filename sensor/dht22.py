import adafruit_dht, requests, time, datetime, json

dht_device = adafruit_dht.DHT22(4)

while True:
    try:
        temperature_c = dht_device.temperature
        temperature_f = temperature_c * (9/5) + 32
        humidity = dht_device.humidity
        
        data = {
            'Temperature': "{0:0.1f}".format(temperature_f),
            'Humidity': "{0:0.1f}".format(humidity),
            'CreatedAt': datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }

        response = requests.post('http://127.0.0.1:5000/post', data=data)
        log = "[" + datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") + "] - " + json.loads(response.text)["status"] +"\n"
    except:
        log = "[" + datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") + "] - Exception" + "\n"
        continue
    finally:
        f = open("DHT22-Log.txt", "a")
        f.write(log)
        f.close() 

    time.sleep(5)   
