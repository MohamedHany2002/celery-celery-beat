# Generated by Django 3.1.3 on 2020-11-12 10:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Data',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('gender_name', models.CharField(max_length=100)),
                ('country', models.CharField(max_length=100)),
                ('age', models.CharField(max_length=100)),
                ('date', models.CharField(max_length=100)),
                ('identity', models.CharField(max_length=100)),
                ('count', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Detail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('flow', models.FloatField()),
                ('pressure', models.FloatField()),
                ('created_date', models.DateField()),
                ('created_time', models.TimeField()),
            ],
        ),
    ]
