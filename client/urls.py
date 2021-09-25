from django.urls import path, include
from . import views

urlpatterns = [
    path('list-admin-user/', views.AdminUser.as_view(), name='list_admin_user'),
]
