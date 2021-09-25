from django.urls import path, include
from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token, verify_jwt_token
from api import views

urlpatterns = [
    path('user_register', views.UserRegister.as_view(), name='user_register'),
    path('token_auth', obtain_jwt_token, name='token_auth'),
    path('token_refresh', refresh_jwt_token, name='token_refresh'),
    path('token_verify', verify_jwt_token, name='token_verify'),
    path('security_questions', views.SecurityQuestions.as_view(), name='security_questions'),
    # include urls api version 1
    path('v1/', include('api.v1.urls'))
]
