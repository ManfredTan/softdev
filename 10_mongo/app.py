# Manfred Tan
# SoftDev1 pd1
# k#10
# 2020-29-02

from flask import Flask, render_template, Response
from urllib.request import urlopen
import json

app = Flask(__name__) #create instance of class Flask

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


def home():
    link = urlopen("https://api.nasa.gov/planetary/apod?api_key=AiLtoPDhFne6zBMXV5RI2yNqTHK3PKbm1HzOui0W")
    #print(data.geturl())
    response = link.read()
    data = json.loads( response )
    pic = data['url']
    date = data['date']
    explanation = data['explanation']
    print(response)
    return(render_template("index.html",
        explanation = explanation,
        date = date,
        pic = pic))



if __name__ == "__main__":
    app.debug = False
    app.run()
