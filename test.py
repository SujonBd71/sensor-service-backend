# from typing import Collection
# import pymongo
# from pymongo import MongoClient
# client = pymongo.MongoClient("LocalHost", 27017)
# client = MongoClient('mongodb://localhost:27017/')
# db = client.SensorDB

# lightCol = db["testDB"]

# ls = lightCol.find({})

# for document in ls:
#         print(document)

# mydict = { "name": "John", "address": "Highway 37" }

# x = lightCol.insert_one(mydict)


# ls = lightCol.find({})

# print()
# for document in ls:
#         print(document)


# mydict = { "name": "John", "address": "Highway 37" }

# x = lightCol.insert_one(mydict)


# ls = lightCol.find({})

# print()
# for document in ls:
#         print(document)


import paho.mqtt.client as mqtt

try:
    client = mqtt.Client()
except:
    print("Couldn create mqtt client")