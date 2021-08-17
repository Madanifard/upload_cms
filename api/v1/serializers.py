from django.db.models import fields
from rest_framework import serializers
import random
from datetime import datetime
from client.models import Information, Mobiles, Address
from content.models import Post


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
    class Meta:
        models = Post
        fields = '__all__'
