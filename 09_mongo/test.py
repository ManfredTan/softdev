import json
import pymongo
from pymongo import MongoClient
from pprint import pprint # pprint library is used to make the output look more pretty
from bson.json_util import loads


client = MongoClient("mongodb://admin:password@167.172.25.9/restaurants") # defaults to port 27017
db = client['restaurants']
cursor =  db.test.find({})

''' Testing Mongo methods
for document in cursor:
    print(document)
print(db.test.count())
'''

def convertDates(fileName):
    with open(fileName, 'w') as json_file:
        data = json.load(json_file)
        #for store in data:
        store = data[0]
        grades = store['grades']
        #print(grades)
        for review in grades:
            date = review['date']
            stringDate = date['$date']
            date.gdate

            date['$date'] = stringDate
                #print(stringDate)
                #print("=====")
        #for document in data:
            #db.list.insert(document)
convertDates('primer-dataset.json')

def addData(fileName):
    with open(fileName) as json_file:
        data = json.load(json_file)
        store = data[0]
        grades = store['grades']
        #print(grades)
        for review in grades:
            date = review['date']
            jsonDate = date['$date']
            print(jsonDate)
            print("=====")
        #for document in data:
            #db.list.insert(document)
#addData('primer-dataset.json')


def testAdd():
    db.test.insert({'test3':'from py'})

#def addData():
#    with open('primer-dataset.json') as f:
#        file_data = json.load(f)
#    collection_currency.insert_many(file_data)
#    return null
def ingest(f):
    with open('primer-dataset.json') as _f:
        return loads(f'[{",".join(map(lambda s: s[:-1], _f))}]')

#ingest()
#addData()
#testAdd()
