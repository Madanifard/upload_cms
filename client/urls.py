from os import name
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('list-admin-user/', views.AdminUserList.as_view(), name='list_admin_user'),
    path('user-detail/<int:user_id>', views.UserDetails.as_view(), name='user_detail'),
    path('infromation-user-manage/<int:user_id>', views.InformationUserManage.as_view(), name='infromation_user_manage'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)