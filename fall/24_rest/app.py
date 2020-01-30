# Manfred Tan, Jude Rizzo
# SoftDev1 pd9
# k#24 - REST API
# 2019-11-12

from flask import Flask, render_template
from urllib.request import urlopen
import json
app = Flask(__name__) #create instance of class Flask

@app.route("/")
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
    app.debug = True
    app.run()
