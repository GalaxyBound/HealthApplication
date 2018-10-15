# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.template import loader

from django.contrib.auth import login
from django.shortcuts import redirect
from django.views.generic import CreateView, TemplateView
from django.views.decorators.csrf import csrf_exempt

from .forms import PatientRegisterForm, ResponderRegisterForm
from .models import CustomUser


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

def dashboard(request):
    template = loader.get_template("ehealth/dashboard.html")
    context = {}
    return HttpResponse(template.render(context, request))

def map(request):
    template = loader.get_template("ehealth/map.html")
    context = {}
    return HttpResponse(template.render(context, request))

def signin(request):
    template = loader.get_template("ehealth/signin.html")
    context = {}
    return HttpResponse(template.render(context, request))

def index(request):
    template = loader.get_template("ehealth/index.html")
    context = {}
    return HttpResponse(template.render(context, request))

def help(request):
    template = loader.get_template("ehealth/help.html")
    context = {}
    return HttpResponse(template.render(context, request))

def signup(request):
    template = loader.get_template("ehealth/signup.html")
    context = {}
    return HttpResponse(template.render(context, request))

def signup_patient(request):
    template = loader.get_template("ehealth/signup-patient.html")
    context = {}
    return HttpResponse(template.render(context, request))

def signup_responder(request):
    template = loader.get_template("ehealth/signup-responder.html")
    context = {}
    return HttpResponse(template.render(context, request))

@csrf_exempt
def signup_confirm(request):
    template = loader.get_template("ehealth/signup-post.html")
    context = {}
    return HttpResponse(template.render(context, request))


# def home(request):
#     if request.user.is_authenticated:
#         if request.user.is_patient:
#             return redirect('ehealth/patient.html')
#         else:
#             return redirect('ehealth/responder.html')
#     return render(request, 'ehealth/home.html')
#
#
# class SignUpView(TemplateView):
#     template_name = 'ehealth/register.html'
#
#
# class PatientRegisterView(CreateView):
#     model = User
#     form_class = PatientRegisterForm
#     template_name = 'ehealth/register_form.html'
#
#     def get_context_data(self, **kwargs):
#         kwargs['user_type'] = 'patient'
#         return super().get_context_data(**kwargs)
#
#     def form_valid(self, form):
#         user = form.save()
#         login(self.request, user)
#         return redirect('ehealth/patient.html')
#
#
# class ResponderRegisterView(CreateView):
#     model = User
#     form_class = ResponderRegisterForm
#     template_name = 'ehealth/register_form.html'
#
#     def get_context_data(self, **kwargs):
#         kwargs['user_type'] = 'responder'
#         return super().get_context_data(**kwargs)
#
#     def form_valid(self, form):
#         user = form.save()
#         login(self.request, user)
#         return redirect('ehealth/responder.html')
#
#
# # For future views specific to user types, we can do the following:
# # @login_required
# # @type_required (where type is patient or responder)