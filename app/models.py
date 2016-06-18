from __future__ import unicode_literals

from django.db import models

# Create your models here.


class User(models.Model):
    gprofileId = models.CharField(max_length=40, primary_key=True)
    profileId = models.CharField(max_length=40, default="")
