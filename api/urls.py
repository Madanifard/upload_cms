from django.urls import path
from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token, verify_jwt_token
from . import views

urlpatterns = [
    path('user_register', views.UserRegister.as_view()),
    path('token_auth', obtain_jwt_token),
    path('token_refresh', refresh_jwt_token),
    path('token_verify', verify_jwt_token),
]
