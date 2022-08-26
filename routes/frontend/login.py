# routes/frontend/login.py

from bottle import Bottle, get, post, redirect
from controllers.frontend.login import Login
import config

app = Bottle()
login = Login()

@app.get("/")
def getLogin():
    if(config.checkLogged()):
        return redirect("/admin/post")
    else:
        return login.getPage()


@app.post("/")
def postLogin():
    return login.postItem()


@app.get("/logout")
def logout():
    if(config.checkLogged()):
        return login.logOut()
    else:
       return redirect("/login") 
        
