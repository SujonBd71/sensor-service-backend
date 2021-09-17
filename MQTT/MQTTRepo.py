
from MQTT  import MongoDb
from . import MQTTBroker

class MQTTRepo():
    def __init__(self, mqttBroker) -> None:
        self.db = MongoDb.MongoDb()

        self.db.connect()
        # self.db.find()
        
        self.topicToSubscriber = {}
        self.topics = {}
        self.mqttBroker = mqttBroker
        self.mqttBroker.set_messageHandler(self.on_message)
        self.mqttBroker.connect()
        self.mqttBroker.loopStart()
    
        
    def LoadLights(self):
        ls = self.db.find(collection="lights_light")

        
        for l in ls:
            print(l["stat_topic"])
            self.addSubscriber(l["stat_topic"])


    def LoadSensors(self):
        pass


    def addSubscriber(self,  topic):
        self.mqttBroker.subscribe(topic)
        
    def removeSubscriber():
        pass
    def publish():
        pass

    def on_message(self, client, userdata, msg):
        print("#############")
        print(msg.topic+" "+str(msg.qos)+" "+str(msg.payload))

        #cache
        self.topics[msg.topic] =   str(msg.payload)

    
repo = None

def createTopicRepo():
    broker = MQTTBroker.getBroker()
    global repo
    repo = MQTTRepo(broker)


def getRepo():
    global repo
    if not repo :
        createTopicRepo()
    return repo
