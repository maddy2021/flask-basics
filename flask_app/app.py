from datetime import datetime
from flask import Flask
from datetime import datetime

print(__name__)
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World"

@app.route("/<my_name>")
def greetings(my_name):
    greet = "Night"
    now = datetime.now()
    time = now.hour
    if time<12:
        greet = "Morning"
    elif time<16:
        greet = "Afternoon"
    elif time<19:
        greet = "Evening"
    return "Its " + greet + " " + my_name

@app.route("/square/<int:number>")
def square(number):
    return f'square of {number} is {number*number}'

if __name__=="__main__":
    app.run(port=3030, debug=True)
