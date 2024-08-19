from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>hello world!</p>"

@app.route("/comment")
def products():
    return "<p>there we go!</p>"
