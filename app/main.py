import os

from flask import Flask, render_template

app = Flask(__name__)

env = os.getenv("APP")
if not env:
 env = "NONE"

@app.route("/")
def index():
 return env 


@app.route("/app")
def t():
  return render_template("index.html")


app.run(host="0.0.0.0", port=8080)
