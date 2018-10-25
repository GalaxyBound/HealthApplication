# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import AbstractUser
from datetime import date
from django.utils import timezone

# Create your models here.

### PREVIOUS MODEL IMPLEMENTATION (AS OF 17/09/18) ###
# class Person(models.Model):
# 	name = models.CharField(max_length=200)
# 	age = models.IntegerField()
#
# class HealthData(models.Model):
# 	person = models.ForeignKey(Person, on_delete=models.CASCADE)
# 	data = models.CharField(max_length=500)
# 	rec_date = models.DateTimeField('recorded')




### CURRENT MODEL IMPLEMENTATION (AS OF 01/10/18) ###

# CUSTOM FIELDS OPTIONS:
# location: django-easy-maps, django-gmapi, django-coordinatesfield, django-location-field
# address: django-postal, django-address, location packages above
# phone number: django-phonenumber-field

# ## AbstractUser serves as a base user class, allowing for shared attributes between different types of users
class CustomUser(AbstractUser):
	first_name = models.CharField(max_length=200, verbose_name='first name')
	last_name = models.CharField(max_length=200, verbose_name='last name')
	email = models.EmailField(verbose_name='email address', max_length=200, unique=True)
	current_location = models.CharField(max_length=200) # Eventually must update this to use geographical locations
	dob = models.DateField(default=timezone.now, verbose_name='date of birth')
	address = models.CharField(max_length=200) # Eventually must update this to use geographical locations
	phone_number = models.CharField(max_length=200) # Eventually must update this to use phone number
	is_patient = models.BooleanField(default=True)
	is_responder = models.BooleanField(default=False)

	def __str__(self):
		return self.username

	def get_full_name(self):
		return self.first_name + " " + self.last_name

	def get_age(self):
		today = date.today()
		try: birthday = self.dob.replace(year=today.year)

		# Raise exception when birthday is Feb 29 and current year isn't a leap year
		except ValueError: birthday = self.dob.replace(year=today.year, day=self.dob.day-1)

		if birthday > today: return today.year - self.dob.year - 1
		else: return today.year - self.dob.year


# For now we don't specify this as a user object, since it only requires a few fields
class EmergencyContact(models.Model):
	first_name = models.CharField(max_length=200, verbose_name='first name')
	last_name = models.CharField(max_length=200, verbose_name='last name')
	email = models.EmailField(verbose_name='email address', max_length=200, unique=True)
	phone_number = models.CharField(max_length=200) # Eventually must update this to use phone number

	def __str__(self):
		return "Name: %s %s, Number: %s" % (self.first_name, self.last_name, self.phone_number)


# Eventually must update health data to Arduino specifications
class HealthData(models.Model):
	spo2 = models.CharField(max_length=500)
	temp = models.CharField(max_length=500)
	heartrate = models.CharField(max_length=500)
	# TODO: Implement
	# rec_date = models.DateTimeField('recorded')


# # Subclass of base user class; patients are registered as potential victims of a heart attack
class Patient(models.Model):
	user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, primary_key=True)
	health_data = models.OneToOneField(HealthData, on_delete=models.CASCADE, related_name='patient_data')
	emergency_contacts = models.ManyToManyField(EmergencyContact, related_name='emergency_contacts')

	# Eventually must update these 2 fields to be a list of strings
	existing_conditions = models.CharField(max_length=300, verbose_name='existing conditions')
	allergies = models.CharField(max_length=300)

	def __str__(self):
		return self.user.name
	
	def register(postData):
		
		return True


# Subclass of base user class; responders are registered to help patients in case of heart attacks
class Responder(models.Model):
	user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, primary_key=True)
	certification = models.CharField(max_length=300) # Eventually must update this to be a file type or ranking
	expiration_date = models.DateField(verbose_name='certification expiration date')

	def __str__(self):
		return self.user.name






