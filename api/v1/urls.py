from django.urls import path
from . import views

urlpatterns = [
    path('user_information',  views.UserInformation.as_view()),
    path('user_mobile', views.UserMobile.as_view()),
    path('user_mobile_detail/<int:pk>', views.UserMobileDetail.as_view()),
    path('user_address', views.UserAddress.as_view()),
    path('user_address_detail/<int:pk>', views.UserAddressDetail.as_view()),
]