from django.urls import path
from . import views

urlpatterns = [
    path('user_information',  views.UserInformation.as_view()),
    path('user_mobile', views.UserMobile.as_view()),
]