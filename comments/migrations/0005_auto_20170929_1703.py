# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-09-29 17:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comments', '0004_auto_20170928_1740'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='modified_time',
            field=models.DateTimeField(auto_now=True, verbose_name='修改日期'),
        ),
    ]