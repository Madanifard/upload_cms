from django.urls import path
from . import views

urlpatterns = [
    path('user_information',  views.UserInformation.as_view()),
]