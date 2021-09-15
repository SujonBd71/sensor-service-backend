from MQTT  import MongoDb

class MQTTRepo():
    def __init__(self, mqttBroker) -> None:

        self.db = MongoDb.MongoDb()
        self.db.connect()
        self.db.find()
        
        self.topicToSubscriber = {}
        self.MqttBroker = mqttBroker
    
        

    def addSubscriber(self, subscriber, topic):
        self.MqttBroker.subscribe(topic)
        
    def removeSubscriber():
        pass
    def publish():
        pass

