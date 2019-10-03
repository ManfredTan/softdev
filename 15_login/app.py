#Team We Love John Homework - Manfred Tan and Connor Oh
#SoftDev1 pd9
#K15 - login
#2019-10-02

from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)


@app.route("/")
def checkcookies():
    print(request.cookies.get('username'))
    if(request.cookies.get('username') == None):
        print('no cookies found: going to login page')
        return render_template(
            'login.html'
        )
    else:
        print('Cookies Found')
    return url_for("welcome")


@app.route("/login", methods=["POST"])
def login():
    #print(request.args) -> returns query string (GET method), which is empty because we use POST method
    #print(request.args["username"])
    #print(request.args["password"])

    print(request.form) #returns values in forms with POST method
    print(request.form["username"]) #prints value in username
    print(request.form["password"]) #prints value in password

    return "received login information"

@app.route("/welcome")
def welcome():
    return "welcome you have logged in. moonlight ah."

if __name__ == "__main__":
    app.debug = True # Automatically updates project with save file
    app.run()
