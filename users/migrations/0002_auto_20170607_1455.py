# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-06-07 06:55
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='user',
            options={'verbose_name': '用户', 'verbose_name_plural': '用户'},
        ),
    ]
