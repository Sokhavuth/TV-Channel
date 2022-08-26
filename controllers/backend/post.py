# controllers/backend/post.py

import config, copy
from bottle import template, redirect, request

class Post:
    def __init__(self):
        self.setup = copy.deepcopy(config.settings())


    def getPage(self):
        self.setup["pageTitle"] = "POST PAGE"
        self.setup["route"] = "/admin/post"
        user = config.checkLogged()
        if(user):
            self.setup["username"] = user["name"]

        return template("base", data=self.setup)

