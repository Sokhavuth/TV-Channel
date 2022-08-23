# routes/frontend/index.py

from bottle import Bottle, template, get, request
from copy import deepcopy


appIndex = Bottle()

@appIndex.get('/')
def indexHandler():
    config = request.app.config["myapp.config"]
    settings = deepcopy(config["settings"])
    setup = settings()
    setup["message"] = "Hello World!"

    return template('base', data=setup)
