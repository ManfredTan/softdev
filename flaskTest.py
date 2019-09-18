from flask import Flask

app = Flask(__name__) #create instance of class Flask

@app.route("/")

def hello_world():
    print(__name__) #where will this go?
    return "No hablo queso!"

if __name__ == "__main__":
    app.debug = True
    app.run()
