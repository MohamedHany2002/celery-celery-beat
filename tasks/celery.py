from __future__ import absolute_import,unicode_literals
import os
from celery import Celery
# from mytasks.views import time
from django.conf import settings
import redis
# from urllib import request
from django.http import request
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'tasks.settings')
app = Celery('tasks')

app.config_from_object('django.conf:settings')

app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)
# from mytasks.tasks import print_message





app.conf.beat_schedule = {
    #name of the scheduler

    'add-every-2-seconds': {
        # task name which we have created in tasks.py

        'task': 'print_msg_with_name',  
        # set the period of running
        
        'schedule': 5.0,
         # set the args 
         
        # 'args': (16, 16) 
    },
    #name of the scheduler

    # 'print-name-every-5-seconds': {  
    #     # task name which we have created in tasks.py

    #     'task': 'print_msg_with_name',  
        
    #     # set the period of running

    #     'schedule': 5.0,  
    #     # set the args

    #    'args': ("DjangoPY", )  
    # },
}