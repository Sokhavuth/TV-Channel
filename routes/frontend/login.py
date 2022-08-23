# routes/frontend/login.py

from bottle import Bottle, get, template


app = Bottle()

@app.get("/")
def login():
    return template("base")