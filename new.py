# Q4. Create a “/welcome” route to display the welcome message “Welcome to ABC Corporation” and a “/”
# route to show the following details:
# Company Name: ABC Corporation
# Location: India
# Contact Detail: 999-999-9999
from flask import Flask
from flask import request

app = Flask(__name__)
@app.route("/")
def greets():
    return "welcome"

@app.route("/info1")
def details1():
    return "Company Name: ABC Corporation" 

@app.route("/info2")
def details2():
    return "Location: India"    

@app.route("/info3")
def details3():
    return "Contact Detail: 999-999-9999" 

@app.route("/info4")
def request_input():
    data = request.args.get('x')
    return "this is my input from url {}".format(data)

@app.route('/info5')
def test():
    a = 5+6
    return "this my first fun in Flask {}".format(a)

if __name__=="__main__":
    app.run(host="0.0.0.0") 