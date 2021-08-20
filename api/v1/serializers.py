import os
from django.db.models import fields
from rest_framework import serializers
import random
from datetime import datetime
from client.models import Information, Mobiles, Address
from content.models import Post
from drf_extra_fields.fields import Base64ImageField


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

    def update(self, instance, validated_data):
        instance.mobile = validated_data.get('mobile', instance.mobile)
        instance.sms_code = random.sample(range(1111, 9999), 1)[0]
        instance.date_sent = datetime.today()
        instance.save()
        return instance


class UserAddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = '__all__'


class PostSerializer(serializers.ModelSerializer):
    image = Base64ImageField(required=False)  # pip install django-extra-fields

    class Meta:
        model = Post
        fields = '__all__'

    def update(self, instance, validated_data):
        if 'image' in validated_data:
            os.remove(instance.image.path)

        return super().update(instance, validated_data)
