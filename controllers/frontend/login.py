# controllers/frontend/login.py

import config, copy, hashlib, jwt, uuid
from datetime import datetime, timezone, timedelta
from bottle import template, request, response, redirect
from models.user import User


class Login:
    def __init__(self):
        settings = copy.deepcopy(config.settings)
        self.setup = settings()
        self.redis = config.redis
        self.secret_key = config.secret_key
        self.user = User()


    def getPage(self):
        self.setup["pageTitle"] = "Log into Admin Page"
        self.setup["route"] = "/login"

        return template("base", data=self.setup)


    def checkLogged(self):
        sessionid = request.get_cookie('sessionid', secret=self.secret_key)
        encoded_jwt = self.redis.get(sessionid) 
        try:
            payload = jwt.decode(encoded_jwt, self.secret_key, algorithms=["HS256"])
            if(payload["userid"]):
                return True
        except jwt.ExpiredSignatureError:
            return False


    def postItem(self):
        password = request.forms.getunicode('password')
        email = request.forms.getunicode('email')

        user = self.user.checkUser(email)
        
        if user:
            passw = hashlib.sha512(password.encode("utf-8") + user["salt"]).hexdigest()
            if(passw == user["password"]):
                self.setup["pageTitle"] = 'Post Page'

                payload = {"userid": user["id"], "role": user["role"]}
                exp = datetime.now(timezone.utc) + timedelta(seconds=60*60*24*15)

                myjwt = jwt.encode({"user": payload, "exp": exp }, self.secret_key, algorithm="HS256")
                sessionid = uuid.uuid4().hex
                self.redis.set(str(sessionid), myjwt, {"ex": timedelta(seconds=60*60*24*15)})
                response.set_cookie('sessionid', str(sessionid), path='/', secret=self.secret_key)

                return redirect('/admin/post')
            else:
                self.setup["pageTitle"] = 'Log into Admin Page'
                self.setup['message'] = 'Your password is wrong!'
                self.setup['route'] = '/login'
                return template("base", data=self.setup)
        else:
            self.setup["pageTitle"] = 'Log into Admin Page'
            self.setup['message'] = 'Your Email is wrong!'
            self.setup['route'] = '/login'
            return template("base", data=self.setup)

