# Generated by Django 2.2.6 on 2020-09-15 19:12

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='文章标签')),
                ('number', models.IntegerField(default=1, verbose_name='标签数目')),
            ],
            options={
                'verbose_name': '文章标签',
                'verbose_name_plural': '文章标签',
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True, verbose_name='文章分类')),
                ('number', models.IntegerField(default=1, verbose_name='分类数目')),
                ('lft', models.PositiveIntegerField(editable=False)),
                ('rght', models.PositiveIntegerField(editable=False)),
                ('tree_id', models.PositiveIntegerField(db_index=True, editable=False)),
                ('level', models.PositiveIntegerField(editable=False)),
                ('parent_name', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children', to='BlogAdmin.Category', verbose_name='上级分类')),
            ],
            options={
                'verbose_name': '文章分类',
                'verbose_name_plural': '文章分类',
                'db_table': 'category',
            },
        ),
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='标题')),
                ('abstract', models.TextField(blank=True, default='', max_length=200, verbose_name='摘要')),
                ('img', models.ImageField(blank=True, null=True, upload_to='article_img/%Y/%m/%d/', verbose_name='文章图片')),
                ('content', models.TextField()),
                ('create_time', models.DateTimeField(default=datetime.datetime(2020, 9, 15, 19, 12, 53, 586123), verbose_name='创建时间')),
                ('modify_time', models.DateTimeField(auto_now=True, verbose_name='修改时间')),
                ('click_nums', models.IntegerField(default=0, verbose_name='点击量')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='BlogAdmin.Category', verbose_name='文章分类')),
                ('tag', models.ManyToManyField(to='BlogAdmin.Tag', verbose_name='文章标签')),
            ],
            options={
                'verbose_name': '我的博客',
                'verbose_name_plural': '我的博客',
            },
        ),
    ]
