import paho.mqtt.client as mqtt
import time
import subprocess

# import Adafruit_DHT
# sensor = Adafruit_DHT.DHT22
pin = 4

test = "test/"
# test = ""


Broker = "192.168.1.151"
temp_pub_topic = test + "living_room/weather";
hum_pub_topic = "living_room/weather/humidity";


def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))

def on_message(client, userdata, msg):
    message = str(msg.payload)
    print(msg.topic+" "+message)

def on_publish(mosq, obj, mid):
    print("")

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.on_publish = on_publish

client.connect(Broker, 1883, 60);

def ToFarentHiet(c):
    return c * 9/5 + 32 
  

while True:
    client.loop_start()
    import random
    import json
    time.sleep(2);
    humidity, temperature = random.randrange(0,100),random.randrange(0,200)
    temperature = round(temperature, 4);
    humidity = round(humidity, 4);
    
    temperature = ToFarentHiet(temperature)
    payload=json.dumps({"temp": temperature,"hum":  humidity})

    print(type(payload))
    print(payload)
    
    client.publish(temp_pub_topic, payload);

    
