from flask import Flask

app = Flask(__name__)



@app.route("/")
def welcome():
    return "Welcome to my exploration into building REST APIs!"
