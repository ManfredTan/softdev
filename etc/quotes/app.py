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
    link = urlopen("http://quotes.rest/qod")
    #print(data.geturl())
    response = link.read()
    data = json.loads( response )
    content = data['contents']
    quotes = content['quotes']
    temp = quotes[0]
    quote = temp['quote']
    author = temp['author']

    print(temp)
    return(quote + ' by ' + author)


if __name__ == "__main__":
    app.debug = True
    app.run()
