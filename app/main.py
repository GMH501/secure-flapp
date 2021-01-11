import os
#test
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
  env = os.getenv("APP")
  if not env:
    env = "NONE"
  return env 

@app.route("/app")
def t():
  return render_template("index.html")


@app.route("/env/<env>")
def env(env):
  os.environ['APP'] = env
  return env

app.run(host="0.0.0.0", port=8080)
