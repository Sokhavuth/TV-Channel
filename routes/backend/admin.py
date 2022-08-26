# routes/backend/admin.py

from bottle import Bottle


app = Bottle()

from . import post
app.mount("/post", post.app)