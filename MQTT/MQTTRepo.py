
from MQTT  import MongoDb
from . import MQTTBroker
import json
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

    def getStat(self, topic):
        if topic in self.topics:
            return self.topics[topic]
        return ""

    def LoadSensors(self):
        print("")
        print("##########################")
        print("##### Loading sensors #######")
        ls = self.db.find(collection="sensors_sensor")
        for l in ls:
            print(l["stat_topic"])
            self.addSubscriber(l["stat_topic"])

    def addSubscriber(self,  topic):
        self.mqttBroker.subscribe(topic)
        
    def removeSubscriber():
        pass
    def publish():
        pass

    def on_message(self, client, userdata, msg):
        print("#############")
        print(msg.topic+" "+str(msg.qos)+" "+str(msg.payload))

        m_decode=str(msg.payload.decode("utf-8","ignore"))
        m_in=json.loads(m_decode)

        #cache
        self.topics[msg.topic] =  m_in
        print(m_in)

    
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
