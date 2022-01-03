from datetime import date, datetime
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

@app.route("/home")
def home():
    return "Paws Rescue Center 🐾"

@app.route("/about")
def about():
    return '''We are a non-profit organization working as an animal rescue.\
     We aim to help you connect with the purrfect furbaby for you! The animals you find on our website are rescued and \
     rehabilitated animals. Our mission is to promote the ideology "adopt, don't hop"! .'''

@app.route("/age/<int:year>")
def calculate_age(year):
    today= date.today()
    if year>today.year: return "OOps, you havent born yet, try else"
    age= today.year- year
    return "age is " +str(age)


if __name__=="__main__":
    app.run(port=3030, debug=True)
