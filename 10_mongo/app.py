# Manfred Tan
# SoftDev1 pd1
# k#10
# 2020-29-02

from flask import Flask, render_template, Response
from urllib.request import urlopen
import json
import math
import pymongo
from pymongo import MongoClient
from pprint import pprint # pprint library is used to make the output look more pretty

client = MongoClient("mongodb://admin:password@167.71.190.132/locations") # defaults to port 27017
db = client['locations']
cursor =  db.continents.find({})

app = Flask(__name__) #create instance of class Flask

#for document in cursor:
#    print(document['lat'])
#print(db.continents.count())


@app.route("/")
def nothing():
    return render_template("map.html",
        mapLink = createMapLink(30.333472,-81.470448))

def getAddress(lat,long):
    ''' Given coordinates, returns a relevant address '''
    base = 'http://www.mapquestapi.com/geocoding/v1/reverse?'
    key = 'key=7ZvhGRQZvEJ7JuZDl1Oz3SeAX36eGAa6'
    location = '&location=' + str(lat) + "," + str(long)
    link = urlopen(base + key + location)
    response = link.read()
    data = json.loads( response )
    print("---")
    #print(data)
    results = data["results"][0]
    locations = results['locations'][0]
    street = locations['street']
    city = locations['adminArea5']
    state = locations['adminArea3']
    zip = locations['postalCode']
    country = locations['adminArea1']
    print("Street: " + street)
    print("city: " + city)
    print("state: " + state)
    print("zip: " + zip)
    print("country: " + country)

#getAddress(30.333472,-81.470448)
#getAddress(51.706288839123,-74.685126811391)
#getAddress(19.91667,52)

def createMapLink(lat, long):
    ''' Given coordinates, returns a relevant image link '''
    base = 'https://www.mapquestapi.com/staticmap/v5/map?'
    key = 'key=7ZvhGRQZvEJ7JuZDl1Oz3SeAX36eGAa6'
    center = '&center=' + str(lat) + "," + str(long)
    size = '&size=600,400@2x'
    link = base + key + center + size
    return link

#createMapLink(30.333472,-81.470448)


def distanceBetween(x1,y1,x2,y2):
     d = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
     return d
#print(distanceBetween(0, 0, 3, 4))

def closestContinent(latMeteor, longMeteor):
    dist = 99999.9
    closestAbv = ""
    for document in cursor:
        lat = document['lat']
        long = document['long']
        next = distanceBetween(lat, long, latMeteor, longMeteor)
        if (next < dist):
            dist = next
            closestAbv = document['abv']
    return closestAbv

print(closestContinent(8.0,30.0))

#if __name__ == "__main__":
#    app.debug = False
#    app.run()
