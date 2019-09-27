#Team Hippo- Sophie Nichol, Manfred Tan, Calvin Chu
#SoftDev1 pd9
#K12: Echo Echo Echo
#2019-09-26

from flask import Flask, render_template, request
app = Flask(__name__)


@app.route("/")
def hello_world():
    print("Main page loaded") # Prints out something on load/reload in console
    return render_template('landing.html')


@app.route("/auth")
def authenticate():
    # TESTING:
    #print(app) --- <Flask 'app'>
    #print(request) --- <Request 'http://127.0.0.1:5000/auth?firstName=Manfred&lastName=Tan&band=imagine+dragons&Submit=Submit' [GET]>
    #print(request.headers) --- user info
    #print(request.method) --- GET
    #print(request.args["firstName"]) --- Manfred
    #print(request.form) --- ImmutableMultiDict([])
    #print(cgi.FieldStorage ) --- error

    name = request.args["name"]

    origin = request.args["planet"]

    topping = request.args["pizza"]

    return render_template("auth.html",
    name = name,
    origin = origin,
    topping = topping,
    method = request.method,

    )

if __name__ == "__main__":
    app.debug = True # Automatically updates project with save file
    app.run()
