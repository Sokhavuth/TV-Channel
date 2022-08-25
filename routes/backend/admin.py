# routes/backend/admin.py

from bottle import Bottle, get


app = Bottle()

from . import post
app.mount("/post", post.app)