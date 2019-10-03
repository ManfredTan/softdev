#Team We Love John Homework - Manfred Tan and Connor Oh
#SoftDev1 pd9
#K15 - login
#2019-10-02

from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)


@app.route("/")
def checkcookies():
    if(request.cookies.get('username') == None):
        print('no cookies found: going to login page')
        return render_template(
            'login.html'
        )
    else:
        print('Cookies Found')
    return url_for("welcome")


@app.route("/login")
def login():
    return "recieved login information"

@app.route("/welcome")
def welcome():
    return "welcome you have logged in. moonlight ah."

if __name__ == "__main__":
    app.debug = True # Automatically updates project with save file
    app.run()
