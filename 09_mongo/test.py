import json
import pymongo
from pymongo import MongoClient
from pprint import pprint # pprint library is used to make the output look more pretty
from bson.json_util import loads
import bson

client = MongoClient("mongodb://admin:password@167.172.25.9/restaurants") # defaults to port 27017
db = client['restaurants']
cursor =  db.test.find({})

''' Testing Mongo methods
for document in cursor:
    print(document)
print(db.test.count())
'''

def convertDates():
    f = open('primer-dataset.json','r')
    filedata = f.read()
    f.close()

    newdata = filedata.replace("$date","gdate")

    f = open('primer-dataset2.json','w')
    f.write(newdata)
    f.close()
#convertDates()

def addData(fileName):
    with open(fileName) as json_file:
        data = json.load(json_file)
        store = data[0]
        grades = store['grades']
        #print(grades)
        for document in data:
            db.list.insert(document)
addData('primer-dataset2.json')


def testAdd():
    db.test.insert({'test3':'from py'})



#ingest()
#addData()
#testAdd()
