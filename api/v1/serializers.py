from django.db.models import fields
from rest_framework import serializers
from client.models import Information


class UserInformationSerializers(serializers.ModelSerializer):
    class Meta:
        model = Information
        fields = '__all__'