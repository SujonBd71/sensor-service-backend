import paho.mqtt.client as mqtt
import time
import subprocess
import json

# import Adafruit_DHT
# sensor = Adafruit_DHT.DHT22
pin = 4


Broker = "192.168.1.151"
temp_pub_topic = "living_room/weather"
hum_pub_topic = "living_room/weather/humidity"


def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))

def on_message(client, userdata, msg):
    print(msg.topic)
    print(msg.payload) # <- do you mean this payload = {...} ?
    payload = json.loads(msg.payload) # you can use json.loads to convert string to json


def on_publish(mosq, obj, mid):
    print("")

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.on_publish = on_publish

client.connect(Broker, 1883, 60);
client.subscribe(temp_pub_topic, qos=1)

def ToFarentHiet(c):
    return c * 9/5 + 32 

client.loop_start()
  
while(True):
    pass


    
