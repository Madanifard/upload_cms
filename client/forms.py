from django import forms
from django.db.models.fields import files
from django.forms import fields
from .models import Address, Information, Mobiles


class InformationUser(forms.ModelForm):
    class Meta:
        model = Information
        fields = '__all__'

class MobileUser(forms.ModelForm):
    class Meta:
        model = Mobiles
        fields = '__all__'

class AddressUser(forms.ModelForm):
    class Meta:
        model = Address
        fields = '__all__'