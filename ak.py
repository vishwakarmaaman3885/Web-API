from flask import Flask
from flask import request # from flask import request 
# imports the request object, which is used to get data sent by a user to a Flask application.

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "Hello, World!"

@app.route("/hello1")
def hello_world1():
    return "Hello, World!1"

@app.route("/hello2")
def hello_world2():
    return "Hello, World!2"

@app.route('/test_fun')
def test():
    a = 5+6
    return "this my first fun in flask {}".format(a)

@app.route('/input_url')
def request_input():
    data = request.args.get('x')
    return "this is my input from url {}".format(data) # here anything i can write after ?x= (anything i want)

if __name__=="__main__":
    app.run(host="0.0.0.0") 
