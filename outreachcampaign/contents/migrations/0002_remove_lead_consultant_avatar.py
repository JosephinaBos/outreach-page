# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-26 09:31
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contents', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='lead',
            name='consultant_avatar',
        ),
    ]