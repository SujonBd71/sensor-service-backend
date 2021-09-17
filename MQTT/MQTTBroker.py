
import paho.mqtt.client as mqtt

class MQTTBroker():
    def __init__(self, ip, port) -> None:
        try:
            self.ip = ip
            self.port = port
            self.client = mqtt.Client()
            self.client.on_connect = self.on_connect
            # self.client.on_message = self.on_message
            self.client.on_subscribe = self.on_subscribe

            print("Client created")

        except:
            print("Couldn create mqtt client")
    
    def set_messageHandler(self, cb):
        self.client.on_message = cb


    
    def on_connect(self, client, userdata, flags, rc):
        print("connected")
        # self.client.subscribe("stat/living_room_light/POWER", qos=1) 

        pass

   
    def on_message(self, client, userdata, msg):
        print("#############")
        print(msg.topic+" "+str(msg.qos)+" "+str(msg.payload))  

    def on_subscribe(self,client, userdata, mid, granted_qos):
        print("Subscribed: "+str(mid)+" "+str(granted_qos))
    
    def subscribe(self, topic):
        # self.client.subscribe(topic) 
        print("subscribing")
        self.client.subscribe("stat/living_room_light/POWER", qos=1) 

    def publish(self, topic, msg):
        pass
    
    def connect(self):
        self.client.connect("192.168.1.151", 1883, 60)
    
    def loopStart(self):
        self.client.loop_start()
    
# def on_connect(client, userdata, flags, rc):
#     # client.subscribe("$SYS/#")
#     print("Connected")
#     print(client)
#     print(userdata)
#     print(rc)

# def on_message(client, userdata, msg):
#     # Do something
#     pass

broker = MQTTBroker("192.168.1.151", 1883)
# broker.connect()

def getBroker():
    return broker