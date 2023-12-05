# Mad Guy Website using Flask Server Framework
# Made by Paul Ged - 12 June 2023.
import datetime
from flask import Flask, render_template, redirect, send_file

# creates app to run
app = Flask(__name__)

# get current year for website footer
now_time = datetime.datetime.now()
year = now_time.year


@app.route("/")
def index():
    # renders index.html file and adds year variable for jinja
    return render_template("index.html", year=year)

@app.route("/#services")
def services():
    # renders index.html file and adds year variable for jinja
    return redirect('/')

# cookie page
@app.route("/cookies")
def cookies():
    return render_template("cookies.html")

@app.route("/download_resume")
def download_resume():
    path = "static/download/Paulius Gedrimas Resume.pdf"
    return send_file(path)


# runs app from main.py
if __name__ == "__main__":
    app.run()
