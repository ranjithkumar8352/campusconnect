# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-05 11:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0009_auto_20160625_0258'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='gcmId',
            field=models.CharField(default='', max_length=30),
        ),
    ]
