from celery import shared_task
# from mytasks.models import table
from mytasks.models import table
# @shared_task
# def sample_task():
#     ptable.objects.create(name='ali')
    
@shared_task(name = "print_msg_with_name")
def print_message( *args, **kwargs):
  table.objects.create(name='ali')
  # print(table.objects.all())
  print("Celery is working!! {} have implemented it correctly.")



# one terminal cd src : celery -A tasks beat -l info
# another termainal cd src : celery -A tasks worker -l info

