# Generated by Django 2.2.6 on 2020-09-15 22:02

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BlogAdmin', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='HeadImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='图片标题')),
                ('img', models.ImageField(blank=True, upload_to='head_img/%Y/%m/%d/', verbose_name='头部图片')),
            ],
        ),
        migrations.AlterField(
            model_name='blog',
            name='create_time',
            field=models.DateTimeField(default=datetime.datetime(2020, 9, 15, 22, 2, 31, 589457), verbose_name='创建时间'),
        ),
    ]