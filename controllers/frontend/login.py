# controllers/frontend/getPage.py

import config, copy
from bottle import template


class Login:
    def __init__(self):
        settings = copy.deepcopy(config.settings)
        self.setup = settings()

    def getPage(self):
        self.setup["pageTitle"] = "Log into Admin Page"
        self.setup["route"] = "/login"

        return template("base", data=self.setup)

