# Generated by Django 3.1 on 2020-09-16 09:10

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BlogAdmin', '0002_auto_20200915_2202'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='create_time',
            field=models.DateTimeField(default=datetime.datetime(2020, 9, 16, 9, 10, 43, 144585), verbose_name='创建时间'),
        ),
    ]
