# Manfred Tan, Brandon Chen
# SoftDev1 pd9
# k#25 - REST
# 2019-11-13

from flask import Flask, render_template
from urllib.request import urlopen
import json
app = Flask(__name__) #create instance of class Flask

@app.route("/")
def trivia():
    link = urlopen("https://opentdb.com/api.php?amount=1&difficulty=medium&type=multiple")
    #print(data.geturl())
    response = link.read()
    data = json.loads( response )

    results = data['results'][0] # enters into the list, which contains info
    question = results['question']
    correctAns = results['correct_answer']
    wrongAns = results['incorrect_answers'] # 0,1,2

    print(wrongAns[0])
    return(render_template('trivia.html',
        question = question,
        correctAns = correctAns,
        wrongAns = wrongAns))


if __name__ == "__main__":
    app.debug = True
    app.run()
