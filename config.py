# config.py
# pip install python-dotenv
# pip install PyJWT
# pip install pymongo
# pip install redis


def settings():
    setup = {
        "siteTitle": "TV Channel",
        "pageTitle": "",
    }

    return setup


import os
from dotenv import load_dotenv
load_dotenv()
secret_key = os.getenv("SECRET_KEY")


import pymongo
client = pymongo.MongoClient(os.getenv("DATABASE_URI"))
db = client[os.getenv("DB_NAME")]


import redis
redis = redis.Redis(
    host = os.getenv("REDIS_URI"),
    port = int(os.getenv("REDIS_PORT")), 
    password = os.getenv("REDIS_PASSWORD")
)


configure = { 
    "settings": settings, 
    "secret_key": secret_key, 
    "db": db, 
    "redis": redis,
}
