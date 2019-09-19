# Manfred Tan
# SoftDev1 pd9
# k#08 - Flask App
# 2019-09-18

from flask import Flask
app = Flask(__name__) #create instance of class Flask

@app.route("/") #assign following fxn to run when root route requested
def hello_world():
    print(__name__) #where will this go? in terminal!
    return "No hablo queso!" #this goes on web page

@app.route("/about")
def about():
    return "This is for k#08 homework."

@app.route("/creator")
def creator():
    return "Created by Manfred Tan"

@app.route("/easteregg")
def easterEgg():
    return "You have found the secret treasure!"


if __name__ == "__main__":
    app.debug = True
    app.run()





# NOTES

# Decorator - By definition, a decorator is a function
# that takes another function and extends the behavior
# of the latter function without explicitly modifying it.

# functions are "first-class objects". They can be passed and used as args

#
