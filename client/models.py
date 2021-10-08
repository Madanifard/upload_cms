from django.db import models
from django.contrib.auth.models import User
from django.db.models import CASCADE
from django.core.validators import MinValueValidator, MaxValueValidator


class Information(models.Model):
    user = models.OneToOneField(User, on_delete=CASCADE, related_name='user_information')
    national_code = models.CharField(max_length=50)
    avatar = models.ImageField(upload_to='avatars')
    nationality = models.CharField(max_length=50)
    passport_code = models.CharField(max_length=50)
    
    def __str__(self) -> str:
        return self.national_code


class Mobiles(models.Model):
    user = models.ForeignKey(User, related_name='user_mobile', on_delete=CASCADE)
    information = models.ForeignKey(Information, related_name='information_mobile', on_delete=CASCADE)
    mobile = models.CharField(max_length=30)
    sms_code = models.CharField(max_length=10, blank=True, default=None)
    date_sent = models.DateTimeField(blank=True, default=None)
    count_sent = models.IntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(3)])
    verified = models.BooleanField(default=False)


class Address(models.Model):
    user = models.ForeignKey(User, related_name='user_address', on_delete=CASCADE)
    directions = models.CharField(max_length=151)
    postal_code = models.CharField(max_length=50)
    phone = models.CharField(max_length=30)
    latitude = models.DecimalField(max_digits=9, decimal_places=6)
    longitude = models.DecimalField(max_digits=9, decimal_places=6)


class SecurityQuestions(models.Model):
    user = models.ForeignKey(User, related_name='user_security_questions', on_delete=CASCADE)
    question = models.TextField()
    answer = models.TextField()
