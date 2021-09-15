
import paho.mqtt.client as mqtt

class MQTTBroker():
    def __init__(self, ip, port) -> None:
        try:
            self.ip = ip
            self.port = port
            self.client = mqtt.Client()
            self.client.on_connect = self.on_connect
            self.client.on_message = self.on_message

        except:
            print("Couldn create mqtt client")
    
    def on_connect(client, userdata, flags, rc):
        print("connected")
        pass

    def on_message():
        pass

    def subcribe(self, topic, msg):
        pass
    
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