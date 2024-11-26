'''
:@Author: tangchengqin
:@Date: 2024/11/25 11:25:52
:@LastEditors: tangchengqin
:@LastEditTime: 2024/11/25 11:25:52
:Description: 
:Copyright: Copyright (©) 2024 Clarify. All rights reserved.
'''
from django.db import models

# Create your models here.
class User(models.Model):
    userName = models.CharField(max_length=50, unique=True)
    password = models.CharField(max_length=50)
    createTime = models.IntegerField()

    def __str__(self):
        return "this is the user table"
