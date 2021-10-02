from django import forms
from django.contrib.auth.models import User
from django.forms import fields
from .models import Information

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = '__all__'

class InformationUser(forms.ModelForm):
    class Meta:
        model = Information
        fields = '__all__'