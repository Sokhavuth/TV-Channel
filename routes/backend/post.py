# routes/backend/post.py

from bottle import Bottle, get
from controllers.backend.post import Post


app = Bottle()
post = Post()

@app.get("/")
def getPage():
    return post.getPage()