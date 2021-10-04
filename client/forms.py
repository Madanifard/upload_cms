from django import forms
from django.forms import fields
from .models import Information


class InformationUser(forms.ModelForm):
    class Meta:
        model = Information
        fields = '__all__'