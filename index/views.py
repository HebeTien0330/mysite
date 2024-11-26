'''
:@Author: tangchengqin
:@Date: 2024/11/26 12:24:37
:@LastEditors: tangchengqin
:@LastEditTime: 2024/11/26 12:24:37
:Description: 
:Copyright: Copyright (©) 2024 Clarify. All rights reserved.
'''
from django.shortcuts import render
from common.utlis import getContext

# Create your views here.
def index(request):
    context = getContext()
    return render(request, "index.html", context)

def media(request):
    context = getContext()
    return render(request, "media.html", context)

def about(request):
    context = getContext()
    return render(request, "about.html", context)
