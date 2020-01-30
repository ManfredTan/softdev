<<<<<<< HEAD
import csv
import random

from flask import Flask, render_template
app = Flask(__name__)

dictionary = {}
def sol():
    with open("occupations.csv","r") as oldcsv:
        csvRead = csv.reader(oldcsv)
        next(csvRead)
        for row in csvRead:
            dictionary[row[0]] = float(row[1])
    rand = random.randint(1,998) * 0.1
    tempsum = 0
    print(dictionary)
    print(dictionary.values())
    for key in dictionary.keys():
        tempsum += dictionary[key]
        if rand <= tempsum:
            return key
=======
from flask import Flask, render_template
app = Flask(__name__)

coll = [0,1,1,2,3,5,8]
>>>>>>> 18f5f1aac061fbeb8ba9316231e2cc6f63d47e16

@app.route("/")
def hello_world():
    print("Main page loaded") # Prints out something on load/reload in console
    return "New test page!"

<<<<<<< HEAD
@app.route("/occupyflaskst")
def newpage():
    name = sol()
    keys = list(dictionary.keys())
    return render_template('site.html',
    titulo = "Team Gold Introduction",
    job = name,
    col1 = keys,
    col2 = list(dictionary.values()),
    lengthnum = range(len(keys))
=======
@app.route("/my_foist_template")
def newpage():
    return render_template('site.html',
    foo = "foooo",
    collection= coll
>>>>>>> 18f5f1aac061fbeb8ba9316231e2cc6f63d47e16
    )

if __name__ == "__main__":
    app.debug = True # Automatically updates project with save file
    app.run()
