from celery import shared_task
# from mytasks.models import table
from mytasks.models import Data,Detail
import pandas as pd
import os,time
import datetime
import shutil
import random
import string


# @shared_task
# def sample_task():
#     ptable.objects.create(name='ali')
    


def generate_new_name(filename):
    size=5
    chars=string.ascii_lowercase+string.digits+string.ascii_uppercase
    random_value=''.join([random.choice(chars) for _ in range(size)])
    return random_value+filename



@shared_task(name = "print_msg_with_name")
def print_message(*args, **kwargs):
  for filename in os.listdir("./files"):
    if filename.endswith('.xls') or filename.endswith('.xlsx'):
        file = "./files/"+filename
        # obj=datetime.datetime.strptime(time.ctime(os.path.getmtime(file)), "%a %b %d %H:%M:%S %Y")
        # print("this is datetime field ",obj)
        # print("hey")
        # print("time is good ",time.ctime(os.path.getmtime(file)))
        data=pd.read_excel(file)
        for index,data in data.iterrows():
          # if not Data.objects.filter(identity=data['Id']).exists():
          # Data.objects.create(first_name=data['First Name'],last_name=data['Last Name'],gender_name=data['Gender'],country=data['Country'],age=data['Age'],date=data['Date'],identity=data['Id'])
          Detail.objects.create(name=data['name'],flow=data['flow'],pressure=data['pressure'],created_date=data['date'],created_time=data['time'])

          # else:
          #   pass
        # os.mkdir('./archive/new/')

        if os.path.exists("./archive/"+filename):
          filename=generate_new_name(filename)
          print("exists")
          # os.mkdirs('./archive')
          shutil.move(file, './archive/'+filename)
        else:
          shutil.move(file, './archive/'+filename)
    else:
      print("no excell files")

# one terminal cd src : celery -A tasks beat -l info
# another termainal cd src : celery -A tasks worker -l info

