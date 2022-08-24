# routes/frontend/login.py

from bottle import Bottle, get, post, redirect
from controllers.frontend.login import Login


app = Bottle()
login = Login()

@app.get("/")
def getLogin():
    if(login.checkLogged()):
        return redirect("/admin/post")
    else:
        return login.getPage()


@app.post("/")
def postLogin():
    return login.postItem()
        
        