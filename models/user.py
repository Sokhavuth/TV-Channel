# models/user.py

import config, hashlib, uuid
from bottle import request


class User:
    def __init__(self):
        self.db = config.conndb()


    def createRootUser(self):
        raw_salt = uuid.uuid4().hex
        password = "xxxxxxxxxxxxxxxxxxx".encode('utf-8')
        salt = raw_salt.encode('utf-8')
        hashed_password = hashlib.sha512(password + salt).hexdigest()

        user = { 
            "id": uuid.uuid4().hex, 
            "title": 'Guest',
            "content": '',
            "thumb": '',
            "date": '',
            "role": 'Guest',
            "email": 'guest@khmerweb.app',
            "salt": salt,
            "password": hashed_password,
        }

        self.db["users"].insert_one(user)


    def checkUser(self, email):
        return self.db["users"].find_one({ 'email': email })

