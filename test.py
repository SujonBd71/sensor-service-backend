from typing import Collection
import pymongo
from pymongo import MongoClient
client = pymongo.MongoClient("LocalHost", 27017)
client = MongoClient('mongodb://localhost:27017/')
db = client.SensorDB

lightCol = db["Lights"]

ls = lightCol.find({})

for document in ls:
        print(document)

