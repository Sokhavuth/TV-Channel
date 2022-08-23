# routes/frontend/index.py

import config, copy
from bottle import Bottle, template, get, request


app = Bottle()
@app.get('/')
def home():
    settings = copy.deepcopy(config.settings)
    setup = settings()
    setup["message"] = "Hello World!"
    setup["route"] = "/"
    return template('base', data=setup)
