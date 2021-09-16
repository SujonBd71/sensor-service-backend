import pymongo
from pymongo import MongoClient

class MongoDb():
    def __init__(self) -> None:
        self.client = None
    def connect(self):

        self.client = pymongo.MongoClient("LocalHost", 27017)
        # self.client = MongoClient('mongodb://localhost:27017/')
        db = self.client.SensorDB

    def find(self, dbName = "SensorDB", collection = "testDB", query = {}):
        db = self.client.SensorDB
        lightCol = db[collection]
        ls = lightCol.find({})

        print()
        for document in ls:
            print(document)
        return ls
        
