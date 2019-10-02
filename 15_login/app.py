#Team Hippo- Sophie Nichol, Manfred Tan, Calvin Chu
#SoftDev1 pd9
#K11 - Forms
#2019-09-25

from flask import Flask, render_template, request
app = Flask(__name__)


@app.route("/")
def checkcookies():
    if(request.cookies.get('username') == None):
        print('no cookies found: going to login')
        return render_template(
            'login.html'
        )
    else:
        print('nothinh')
    return "hello"


@app.route("/login")
def login():
    return "hello"


if __name__ == "__main__":
    app.debug = True # Automatically updates project with save file
    app.run()
