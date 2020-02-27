
import json
from pymongo import MongoClient
# pprint library is used to make the output look more pretty
from pprint import pprint
# connect to MongoDB, change the << MONGODB URL >> to reflect your own connection string
client = MongoClient("mongodb://admin:password@167.172.25.9/restaurants")
db=client.admin
restaurants = db['restaurants']
# Issue the serverStatus command and print the results
serverStatusResult=db.command("serverStatus")
pprint(serverStatusResult)


def addData():
    with open('primer-dataset.json') as f:
        file_data = json.load(f)
    collection_currency.insert_many(file_data)




addData()
