from django.contrib.auth.models import User
from .models import Post


def get_user_list_post(user_id):
    return Post.objects.filter(user_id=user_id)
