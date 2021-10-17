import paho.mqtt.client as mqtt
import time
import subprocess
import json

# import Adafruit_DHT
# sensor = Adafruit_DHT.DHT22
pin = 4

test = "test/"
Broker = "192.168.1.151"
temp_pub_topic = test + "living_room/weather"
hum_pub_topic = "living_room/weather/humidity"


def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))

def on_message(client, userdata, msg):
    topic=msg.topic
    m_decode=str(msg.payload.decode("utf-8","ignore"))
    print("data Received type",type(m_decode))
    # m_in=json.loads(m_decode) #decode json data
    print(type(m_decode))
    if type(m_decode) == "json":
        m_in=json.loads(m_decode) #decode json data
    else:
        m_in = m_decode

    print(type(m_in))
    print(m_in)




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


    
