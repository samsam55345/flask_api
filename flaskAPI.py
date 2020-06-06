from flask import Flask, render_template
from datetime import datetime


app = Flask(__name__)
page_count = 0

@app.route("/")
def welcome():
    global page_count
    page_count += 1
    return render_template("welcome.html",
    message = "current number of refreshes: %d" % page_count)

@app.route("/date")
def date():
    now = datetime.now()
    return "The date is %s-%s-%s" % (now.month, now.day, now.year)

@app.route("/sadday")
def sad():
    return "When it rains, it pours :("
