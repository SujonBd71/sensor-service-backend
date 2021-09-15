import MQTT


from MQTT import MQTTBroker
from MQTT import MQTTRepo


broker = MQTTBroker.getBroker()

def createTopicRepo():
    repo = MQTTRepo.MQTTRepo(broker)

createTopicRepo()





