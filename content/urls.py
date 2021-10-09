from django.urls import path, include
from . import views

urlpatterns = [
    path('dashboard/', views.dashboard),
    path('list-post', views.PostList.as_view(), name='list_post'),
    path('post-detail/<int:id>', views.PostDetail.as_view(), name='post_detail'),
    path('post-manage/<int:id>', views.PostManage.as_view(), name='post_manage'),
]
