# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

from django.utils import timezone

# Create your models here.

class Lead(models.Model):
    first_name = models.CharField(max_length=200)
    company_name = models.CharField(max_length=200)
    website = models.CharField(max_length=200)
    pitch = models.TextField()
    consultant_name = models.CharField(max_length=200)
    date = models.DateTimeField(default=timezone.now)


