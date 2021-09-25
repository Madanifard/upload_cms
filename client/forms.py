from django import forms
from django.contrib.auth.models import User
from django.forms import fields

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = '__all__'