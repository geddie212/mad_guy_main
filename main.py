# Mad Guy Website using Flask Server Framework
# Made by Paul Ged - 12 June 2023
import datetime
from flask import Flask, render_template

# creates app to run
app = Flask(__name__)

# get current year for website footer
now_time = datetime.datetime.now()
year = now_time.year


@app.route("/")
def index():
    # renders index.html file and adds year variable for jinja
    return render_template("index.html", year=year)

# cookie page
@app.route("/cookies")
def cookies():
    return render_template("cookies.html")


# runs app from main.py
if __name__ == "__main__":
    app.run()
