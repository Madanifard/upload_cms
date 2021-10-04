from os import name
from django.urls import path, include
from . import views

urlpatterns = [
    path('list-admin-user/', views.AdminUserList.as_view(), name='list_admin_user'),
    path('infromation-user-manage/<int:user_id>', views.InformationUserManage.as_view(), name='infromation_user_manage'),
]
