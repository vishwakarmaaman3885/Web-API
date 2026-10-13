from flask import Flask # is a framefork or pythonic library by which you all will be create APIs


app = Flask(__name__)

@app.route("/") #.route() — A Flask method that connects a URL path to a function.

def hello_world(): # "/" — The home page path of your application.
    return "Hello, it's aman "

@app.route("/hello1")
def hello_world1():
    return "Hello, World!1"

@app.route("/hello2")
def hello_world2():
    return "Hello, World!2"

if __name__=="__main__":
    app.run(host="0.0.0.0",port=5000,debug=True)  