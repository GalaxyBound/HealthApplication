from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction

from .models import CustomUser, Patient, Responder

class PatientRegisterForm(UserCreationForm):
    # interests = forms.ModelMultipleChoiceField(
    #     queryset=Subject.objects.all(),
    #     widget=forms.CheckboxSelectMultiple,
    #     required=True
    # )

    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = ('username', 'first_name', 'last_name', 'email', 'dob', 'phone_number', 'password1', 'password2',)

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_patient = True
        user.save()
        # patient = Patient.objects.create(user=user)
        # patient.interests.add(*self.cleaned_data.get('interests'))
        return user



class ResponderRegisterForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = ('username', 'first_name', 'last_name', 'email', 'dob', 'phone_number', 'password1', 'password2',)

    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_responder = True
        if commit:
            user.save()
        return user