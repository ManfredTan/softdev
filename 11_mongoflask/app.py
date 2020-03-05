# Manfred Tan
#SoftDev2 pd1
#K11 - Mongo and flask
#2020-03-05

from flask import Flask, render_template
from urllib.request import urlopen, Request
import json
app = Flask(__name__) #create instance of class Flask


@app.route("/")
def home():
    return render_template('home.html')

@app.route("/meteorite")
def meteorite():
    return None

@app.route("/houseofrep")
def houseofrep():
    return "hello"


@app.route("/auth")
def authenticate():
    print(app)
    print(request)
    print(request.headers)
    #print(request.method)
    print(request.args)
    #print(request.form)
    #print(cgi.FieldStorage )
    return render_template("output.html",
                               username = request.args["data"],
                               method = request.method)

if __name__ == "__main__":
    app.debug = True # Automatically updates project with save file
    app.run()
