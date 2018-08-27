# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.template import loader

# Create your views here.
from django.http import HttpResponse
import datetime
def cur_time(request):
    now = datetime.datetime.now()
    #html = "<html><body>It is now %s.</body></html>" %now
    #return HttpResponse(html)
    template = loader.get_template("ehealth/index.html")
    context = {"now": now}
    return HttpResponse(template.render(context, request))

def hello(request):
    html = "<html><body>Hello there!</body></html>"
    return HttpResponse(html)
