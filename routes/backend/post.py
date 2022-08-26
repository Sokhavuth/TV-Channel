# routes/backend/post.py

from bottle import Bottle, get, redirect
from controllers.backend.post import Post
import config


app = Bottle()
post = Post()

@app.get("/")
def getPage():
    #if(config.checkLogged()):
        #return post.getPage()
    #else:
    redirect("/login")