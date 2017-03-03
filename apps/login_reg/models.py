from __future__ import unicode_literals

from django.db import models

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=64)
    alias = models.CharField(max_length=64, null=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=256)
    birthday = models.CharField(max_length=12, null=True)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
