from __future__ import unicode_literals

from django.db import models

# Create your models here.


class User(models.Model):
    gprofileId = models.CharField(max_length=40, primary_key=True)
    firstname = models.CharField(max_length=15, default="")
    lastname = models.CharField(max_length=15, default="")
    image_url = models.CharField(max_length=100, default="")
    email = models.CharField(max_length=30, default="")
    profileId = models.CharField(max_length=40, default="")
    collegeId = models.CharField(max_length=40,default="")
    batchName = models.CharField(max_length=10,default="")
    branchName = models.CharField(max_length=20, default="")
    sectionName = models.CharField(max_length=5, default="")
    gcmId = models.CharField(max_length=30,default="")
