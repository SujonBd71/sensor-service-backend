from MQTT  import MongoDb
from . import MQTTBroker

class MQTTRepo():
    def __init__(self, mqttBroker) -> None:

        self.db = MongoDb.MongoDb()
        self.db.connect()
        self.db.find()
        
        self.topicToSubscriber = {}
        self.MqttBroker = mqttBroker
    
        
    def LoadLights(self):
        ls = self.db.find(collection="lights_light")
        


    def LoadSensors(self):
        pass


    def addSubscriber(self, subscriber, topic):
        self.MqttBroker.subscribe(topic)
        
    def removeSubscriber():
        pass
    def publish():
        pass


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
