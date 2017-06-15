# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-06-15 22:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0011_auto_20170615_1504'),
    ]

    operations = [
        migrations.CreateModel(
            name='VisitRecord',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('http_host', models.CharField(max_length=30, verbose_name='host')),
                ('http_referer', models.CharField(max_length=40, verbose_name='referer')),
                ('http_user_agent', models.CharField(max_length=100, verbose_name='agent')),
                ('ip', models.CharField(max_length=20, verbose_name='ip')),
                ('server_name', models.CharField(max_length=10, verbose_name='server_name')),
                ('created_time', models.DateTimeField(verbose_name='请求时间')),
            ],
            options={
                'verbose_name_plural': '访问记录',
                'verbose_name': '访问记录',
            },
        ),
        migrations.AlterModelOptions(
            name='friendsite',
            options={'verbose_name': '友情链接', 'verbose_name_plural': '友情链接'},
        ),
    ]
