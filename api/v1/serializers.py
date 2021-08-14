from django.db.models import fields
from rest_framework import serializers
from client import models
from client.models import Information, Mobiles
import random
from datetime import datetime


class UserInformationSerializers(serializers.ModelSerializer):
    class Meta:
        model = Information
        fields = '__all__'

class UserMobileSerializers(serializers.ModelSerializer):
    class Meta:
        model = Mobiles
        fields = '__all__'
    
    def create(self, validated_data):
        return Mobiles.objects.create(
            user=validated_data['user'],
            mobile=validated_data['mobile'],
            sms_code=random.sample(range(1111, 9999), 1)[0],
            date_sent=datetime.today(),
        )