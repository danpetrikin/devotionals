from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.core.urlresolvers import reverse
from django.utils.translation import ugettext_lazy as _
from djangotoolbox.fields import DictField
import random
import re
import os.path
import hashlib
import uuid


class BaseModel(models.Model):
    '''
    Base model class extended by all models defined in this project.
    '''

    created_at = models.DateTimeField(null=False, auto_now_add=True)
    modified_at = models.DateTimeField(null=False, auto_now=True)

    class Meta:
        abstract = True
    
    def META(self):
        return self._meta

class Devotional(BaseModel):
    title = models.CharField(max_length=200, default='')
    month = models.IntegerField(null=False, default=1)
    day = models.IntegerField(null=False, default=1)
    body = models.TextField(null=True, blank=True, default='')
