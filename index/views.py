'''
:@Author: tangchengqin
:@Date: 2024/11/26 12:24:37
:@LastEditors: tangchengqin
:@LastEditTime: 2024/11/26 12:24:37
:Description: 
:Copyright: Copyright (©) 2024 Clarify. All rights reserved.
'''
from django.shortcuts import render
from common.const import BASE_URL

def getContext():
    context = {
        "index": "http://" + BASE_URL + "index/",
        "media": "http://" + BASE_URL + "index/media/",
        "games": "http://" + BASE_URL + "index/games/",
        "about": "http://" + BASE_URL + "index/about/",
        "blog": "http://" + BASE_URL + "index/blog/",
    }
    return context

# Create your views here.
def index(request):
    context = getContext()
    return render(request, "index.html", context)

def media(request):
    context = getContext()
    return render(request, "media.html", context)

def games(request):
    context = getContext()
    return render(request, "games.html", context)

def about(request):
    context = getContext()
    return render(request, "about.html", context)

def blog(request):
    context = getContext()
    return render(request, "blog.html", context)
