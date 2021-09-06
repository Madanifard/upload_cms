from django.urls import path, include
from . import views
from rest_framework import routers

post_routs = routers.DefaultRouter(trailing_slash=False)
post_routs.register('post', views.PostViewSet, basename='post')

post_comment_routes = routers.DefaultRouter(trailing_slash=False)
post_comment_routes.register('post/comment', views.PostCommentViewSet, basename='post_comment')

urlpatterns = [
    path('user_information',  views.UserInformation.as_view(), name='v1_user_information'),
    path('user_mobile', views.UserMobile.as_view(), name='v1_user_mobile'),
    path('user_mobile_detail/<int:pk>', views.UserMobileDetail.as_view(), name='v1_user_mobile_detail'),
    path('user_address', views.UserAddress.as_view(), name='v1_user_address'),
    path('user_address_detail/<int:pk>', views.UserAddressDetail.as_view(), name='v1_user_address_detail'),
] 

urlpatterns += post_routs.urls
urlpatterns += post_comment_routes.urls