from django.urls import path, include
from . import views
from rest_framework import routers

post_routs = routers.DefaultRouter(trailing_slash=False)
post_routs.register('post', views.PostViewSet, basename='post')

urlpatterns = [
    path('user_information',  views.UserInformation.as_view()),
    path('user_mobile', views.UserMobile.as_view()),
    path('user_mobile_detail/<int:pk>', views.UserMobileDetail.as_view()),
    path('user_address', views.UserAddress.as_view()),
    path('user_address_detail/<int:pk>', views.UserAddressDetail.as_view()),
] 

urlpatterns += post_routs.urls