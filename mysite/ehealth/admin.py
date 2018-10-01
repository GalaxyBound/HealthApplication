    # -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import CustomUser, HealthData, Patient, Responder, EmergencyContact
#
# # Register your models here.
admin.site.register(CustomUser)
admin.site.register(HealthData)
admin.site.register(Patient)
admin.site.register(Responder)
admin.site.register(EmergencyContact)

# from .models import HealthData, EmergencyContact
# admin.site.register(HealthData)
# admin.site.register(EmergencyContact)

