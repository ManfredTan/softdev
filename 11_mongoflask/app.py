# Manfred Tan and Pratham Rawat
#SoftDev2 pd1
#K11 - Mongo and flask
#2020-03-05

from flask import Flask, render_template, request
from urllib.request import urlopen, Request
import json
from pymongo import MongoClient
from meteorite import *

app = Flask(__name__) #create instance of metClass Flask
client = MongoClient('localhost', 27017)  # default mongo port is 27017
database = client["11_mongoflask"]

@app.route("/")
def home():
    return render_template('home.html')

@app.route("/houseofrep")
def houseofrep():
    return render_template("houseofreps.html")

@app.route("/processHouseQuery")
def processHouseQuery():
    print(request.args.get('party'))
    print(request.args.get('gender'))
    queryOutput = database.government.find({"$and": [{"party":request.args.get('party')}, {"person.gender_label":request.args.get('gender')}]})
    outputList = list()
    print("IT WORKED")
    for official in queryOutput:
        print(official)
        outputList.append(official)
    return render_template("houseofreps.html", output = outputList)



@app.route("/meteorite")
def meteorite():
    return render_template("meteorite.html")

@app.route("/foundLandings")
def foundLandings():
    return render_template("foundLandings.html")

@app.route("/location")
def location():
    return render_template("location.html")

@app.route("/metClass")
def metClass():
    return render_template("metClass.html")

@app.route("/processFoundLandings")
def processMeteoriteQuery():
    print(request.args.get('foundLandings')) # foundLandings
    output = meteorites_found()
    print(output)
    return render_template("foundLandings.html", output = output)

@app.route("/processLocation")
def processLocation():
    print(request.args.get('location'))
    location = request.args.get('location')
    output = meteorite_fell_near(request.args.get('location'))
    print(output)
    return render_template("location.html", output = output, location = location)

@app.route("/processClass")
def processClass():
    print(request.args.get('metClass'))
    metClass = request.args.get('metClass')
    output = meteorites_with_class(request.args.get('metClass'))
    print(output)
    return render_template("metClass.html", output = output, metClass = metClass)

if __name__ == "__main__":
    app.debug = True # Automatically updates project with save file
    app.run()
