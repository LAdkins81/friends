from __future__ import unicode_literals

from django.db import models
from ..login_reg.models import User

# Create your models here.
class Friend(models.Model):
    sessionuser = models.ForeignKey(User, related_name='sessionuser', null=True)
    friend = models.ForeignKey(User, related_name='userfriend')
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
