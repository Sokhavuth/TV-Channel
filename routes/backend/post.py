# routes/backend/post.py

from bottle import Bottle, get, redirect
from controllers.backend.post import Post
from controllers.frontend.login import Login


app = Bottle()
post = Post()
login= Login()

@app.get("/")
def getPage():
    if(login.checkLogged()):
        return post.getPage()
    else:
        redirect("/login")