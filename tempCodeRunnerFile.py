from flask import Flask # is a framefork or pythonic library by which you all will be create APIs



app = Flask(__name__)

@app.route("/")
def hello_world():
    return "Hello, Aman!"

@app.route("/hello1")
def hello_world1():
    return "Hello, Aman123"

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)