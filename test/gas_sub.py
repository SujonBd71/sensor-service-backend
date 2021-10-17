import paho.mqtt.client as mqtt
import time
import subprocess
import json

# import Adafruit_DHT
# sensor = Adafruit_DHT.DHT22
pin = 4


Broker = "192.168.1.151"
temp_pub_topic = "kichen/sensors/gas/MQ2"
hum_pub_topic = "living_room/weather/humidity"


def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))

def on_message(client, userdata, msg):
    # print(msg.topic)
    # print(msg.payload) # <- do you mean this payload = {...} ?
    # payload = json.loads(msg.payload)
    # print(payload)

    # print("#############")
    # print(msg.topic+" "+str(msg.qos)+" "+str(msg.payload))

    # #cache
    # y = json.load(str(msg.payload))
    # print(y)
    topic=msg.topic
    m_decode=(msg.payload.decode("utf-8","ignore"))
    print("data Received type",type(m_decode))
    print("data Received",m_decode)
    print("Converting from Json to Object")
    # m_in=json.loads(m_decode) #decode json data
    print(type(m_decode))
    if type(m_decode) == "json":
        print("json type")
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


    
