# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-06-16 13:13
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0018_auto_20170616_1306'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='visitstatistics',
            name='today_ip',
        ),
        migrations.RemoveField(
            model_name='visitstatistics',
            name='total_ip',
        ),
        migrations.RemoveField(
            model_name='visitstatistics',
            name='total_visit',
        ),
    ]