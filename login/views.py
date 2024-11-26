from django.shortcuts import render
from django.http import HttpResponse
from login.models import User
from common.const import CODE_FAIL, CODE_SUCCESS
from common.utlis import getMd5
import time
import json

def login(request):
    if request.method == 'GET':
        return render(request, 'login.html')
    if request.method == 'POST':
        username = str(request.POST.get('username'))
        password = str(request.POST.get('password'))
        record = User.objects.filter(userName=username)
        print(username, password, record)
        if not record.exists():
            return HttpResponse(json.dumps({"code": CODE_FAIL, "msg": "username or password error"}))
        if record[0].password != getMd5(password):
            return HttpResponse(json.dumps({"code": CODE_FAIL, "msg": "username or password error"}))
        return HttpResponse(json.dumps({"code": CODE_SUCCESS, "msg": "login success"}))

def register(request):
    if request.method == 'GET':
        return render(request, 'register.html')
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        record = User.objects.filter(userName=username)
        if record.exists():
            return HttpResponse(json.dumps({"code": CODE_FAIL, "msg": "username already exist"}))
        username = str(username)
        password = str(password)
        User.objects.create(userName=username, password=getMd5(password), createTime=time.time())
        return HttpResponse(json.dumps({"code": CODE_SUCCESS, "msg": "register success"}))
