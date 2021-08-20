from enum import Flag
from django.contrib.auth.models import User
from .models import Post


def get_user_list_post(user_id):
    return Post.objects.filter(user_id=user_id)


def get_user_post(user_id, post_id):
    output = {}
    try:
        output = {
            'status': True,
            'post': Post.objects.get(id=post_id, user_id=user_id)
        }
    except:
        output = {
            'status': False,
            'message': 'not found data'
        }
    finally:
        return output
