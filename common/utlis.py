from .const import BASE_URL
import hashlib

def getMd5(str):
    md5 = hashlib.md5()
    md5.update(str.encode('utf-8'))
    return md5.hexdigest()

def getContext():
    context = {
        "index": "http://" + BASE_URL + "index/",
        "media": "http://" + BASE_URL + "media/",
        "games": "http://" + BASE_URL + "games/",
        "about": "http://" + BASE_URL + "about/",
        "blog": "http://" + BASE_URL + "blog/",
    }
    return context
