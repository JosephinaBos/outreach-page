# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-25 12:43
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Lead',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=200)),
                ('company_name', models.CharField(max_length=200)),
                ('website', models.CharField(max_length=200)),
                ('pitch', models.TextField()),
                ('consultant_name', models.CharField(max_length=200)),
                ('consultant_avatar', models.CharField(max_length=200)),
                ('date', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
    ]