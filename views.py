import logging
import re
from random import choice
import string
from annoying.decorators import render_to
from django.shortcuts import get_object_or_404, redirect
from django import forms
from django.conf import settings
from django.core.urlresolvers import reverse, resolve
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponseRedirect, HttpResponseServerError,\
    HttpRequest
from django.template.context import Context
from django.template.loader import get_template, TemplateDoesNotExist
from django.utils import simplejson as json
from django.contrib.auth.models import User
from django.utils import simplejson
from django.http import HttpResponse, HttpResponseRedirect
from django.core.files.base import ContentFile
from devotionals.core.models import *
from django.core.servers.basehttp import FileWrapper
from django.core.mail import EmailMultiAlternatives
import os, uuid
from django.http import Http404
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

@render_to('home.html')
def home(request):        
    return {'devotionals': Devotional.objects.all()}

@render_to('devotional.html')
def devotional(request,month,day):
    try:
        return{'devotional': Devotional.objects.get(month=int(month),day=int(day))}
    except Exception as e:
        print e
        raise Http404