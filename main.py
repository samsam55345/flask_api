from flask import Flask, render_template
from datetime import datetime


app = Flask(__name__)

class Vars(dict):
    def __init__(self):
        self.page_count = 0

vars = Vars()

@app.route("/")
def welcome():
    vars.page_count += 1
    return render_template("welcome.html",
                            message = "current number of refreshes: %d"
                            % (vars.page_count - 1))

@app.route("/date")
def date():
    now = datetime.now()
    return "The date is %s-%s-%s" % (now.month, now.day, now.year)

@app.route("/sadday")
def sad():
    return "When it rains, it pours :("

@app.route("/form")
def form():
    return form("form.html")


if __name__ == "__main__":
    app.run(host = "0.0.0.0", port = "8080", debug = True)
