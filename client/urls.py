from django.urls import path, include
from . import views

urlpatterns = [
    path('list-admin-user/', views.AdminUserList.as_view(), name='list_admin_user'),
    path('mange-user/', views.AdminUserManage.as_view(), name='manage_admin_user'),
    path('mange-user/<int:id>', views.AdminUserManage.as_view(), name='manage_admin_user'),
    path('list-infromation-user', views.InformationUser.as_view(), name='list_information_user')
]
