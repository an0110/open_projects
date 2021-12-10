from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return  "hello there!"


@app.route("/david")
def index2():
    return  "hello david "