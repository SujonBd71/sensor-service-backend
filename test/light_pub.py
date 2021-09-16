import paho.mqtt.client as paho
import time

def on_publish(client, userdata, mid):
    print(str(userdata)+ " mid: "+str(mid))
 
client = paho.Client()
client.on_publish = on_publish
client.connect("192.168.1.151", 1883)
client.loop_start()

while True:
    import random
    temperature = random.randrange(1, 10000)
    print("publishing: " + str(temperature))
    # (rc, mid) = client.publish("test/data", str(temperature), qos=1, retain=True)
    (rc, mid) = client.publish("cmnd/living_room_light/POWER", str("OFF"), qos=1, retain=True)
    time.sleep(10)
    