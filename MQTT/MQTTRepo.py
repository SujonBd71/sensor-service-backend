class MQTTRepo():
    def __init__(self, mqttBroker) -> None:

        #load from DB
        

        self.topicToSubscriber = {}
        self.MqttBroker = mqttBroker
    
        

    def addSubscriber(self, subscriber, topic):
        self.MqttBroker.subscribe(topic)
        
    def removeSubscriber():
        pass
    def publish():
        pass

