from django.db import models

# Create your models here.


class Data(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    gender_name = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    age = models.CharField(max_length=100)
    date = models.CharField(max_length=100)
    identity= models.CharField(max_length=100)
    count = models.IntegerField(default=0)
    # time=models.DataTimeField()sdf

    @staticmethod
    def data_count(self):
        return self.objects.count()

    def __str__(self):
        return self.first_name


class Detail(models.Model):
    name = models.CharField(max_length=100)
    flow = models.FloatField()
    pressure = models.FloatField()
    created_date = models.DateField()
    created_time = models.TimeField()