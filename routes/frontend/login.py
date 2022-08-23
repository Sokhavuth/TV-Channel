# routes/frontend/login.py

from bottle import Bottle, get, post
from controllers.frontend.login import Login


app = Bottle()

@app.get("/")
def getLogin():
    login = Login()
    return login.getPage()