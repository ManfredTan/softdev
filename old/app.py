

from flask import Flask, render_template
app = Flask(__name__)


@app.route("/")
def hello_world():
    print("Main page loaded") # Prints out something on load/reload in console
    return "New test page!"

@app.route("/form")
def makeForm():
    return render_template('foo.html',
    )

if __name__ == "__main__":
    app.debug = True # Automatically updates project with save file
    app.run()
