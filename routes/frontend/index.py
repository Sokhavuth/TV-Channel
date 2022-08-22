# routes/frontend/index.py

from bottle import Bottle, template, get


app = Bottle()

@app.get('/')
def index():
    return template('base')