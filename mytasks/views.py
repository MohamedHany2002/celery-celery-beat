from django.shortcuts import render
import pandas as pd
from . models import Detail
import os
import redis
from django.conf import settings
# from django.contrib.sessions.backends.db import SessionStore
# redis_instance = redis.StrictRedis(host=settings.REDIS_HOST,port=settings.REDIS_PORT, db=0)
# src/mytasks/files
# Create your views here.
# x = 2.0
# time = None   
# r = redis.StrictRedis(host=settings.REDIS_HOST,port=settings.REDIS_PORT,db=settings.REDIS_DB)
def hello(request):
    # key = "sdf545"
    # my_session = SessionStore(session_key=key)
    # my_session.session_key == key
    # my_session["time"]='5.0'
    # print(redis)

    # redis.set("foo","boo")
    # x=redis.get("foo")
    # print(x)
    x = 5.0
    data=Detail.objects.all()
    request.session['time']=5.0
    return render(request,'index.html',{'count':Detail.objects.count(),'data':data})


# iput time as a variable 
# csv -- xsl
# path files and archives
