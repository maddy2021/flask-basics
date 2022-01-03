from flask import Flask

print(__name__)
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World"

if __name__=="__main__":
    app.run(port=3030)
