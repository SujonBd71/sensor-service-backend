import paho.mqtt.client as paho
import json

def on_subscribe(client, userdata, mid, granted_qos):
    print("Subscribed: "+str(mid)+" "+str(granted_qos))

def on_message(client, userdata, msg):
    print(msg.topic+" "+str(msg.qos)+" "+str(msg.payload))    
    topic=msg.topic
    m_decode=str(msg.payload.decode("utf-8","ignore"))
    print("data Received type",type(m_decode))
    print("data Received",m_decode)
    print("Converting from Json to Object")
    if type(m_decode) == "json":
        m_in=json.loads(m_decode) #decode json data
    else:
        m_in = m_decode
    print(type(m_in))
    print(m_in)

client = paho.Client()
client.on_subscribe = on_subscribe
client.on_message = on_message
client.connect("192.168.1.50", 1883)
# client.subscribe("test/data", qos=1)
client.subscribe("stat/living_room_light/POWER") 

client.loop_forever()
