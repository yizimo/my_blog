# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-06-13 09:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comments', '0002_auto_20170613_1709'),
    ]

    operations = [
        migrations.AlterField(
            model_name='commenttest',
            name='data',
            field=models.TextField(verbose_name='测试数据'),
        ),
    ]