# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-06-17 19:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0022_auto_20170617_1902'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blacklist',
            name='ip',
            field=models.CharField(max_length=20, verbose_name='ip地址'),
        ),
    ]
