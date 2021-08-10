from django.core.exceptions import RequestAborted
from rest_framework import serializers
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from rest_framework.fields import ChoiceField
from client.models import SecurityQuestions


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

    def create(self, validated_data):
        return User.objects.create(
            username=validated_data['username'],
            password=make_password(validated_data['password']),
            email=validated_data['email'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
        )


class SecurityQuestionsSerializer(serializers.Serializer):
    items = serializers.JSONField(required=True)
    user_id = serializers.IntegerField(required=True)

    def validate_items(self, items):
        for item in items:
            if 'question' not in item.keys() or 'answer' not in item.keys():
                raise serializers.ValidationError('not set true item')
        return items

    def create(self, validated_data):
        save_data = []
        print(validated_data)
        for item in validated_data['items']:
            save_data.append(SecurityQuestions(
                question=item['question'],
                answer=item['answer'],
                user_id=validated_data['user_id']
            ))

        return SecurityQuestions.objects.bulk_create(list(save_data))
