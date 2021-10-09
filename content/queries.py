from django.contrib.auth.models import User
from .models import Post, PostComment


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


def get_comment_post(post_id):
    return PostComment.objects.filter(post_id=post_id)

def check_exits_post(id):
    return Post.objects.filter(id=id).exists()


def check_exists_comment_post(post_id, comment_id):
    return Post.objects.filter(id=post_id).filter(content_post_comment__id=comment_id).exists()

def get_all_post():
    output = {}
    try:
        output = {
            'status': True,
            'posts': Post.objects.all()
        }
    except Exception as ex:
        output = {
            'status': False,
            'message': ex
        }
    finally:
        return output

def get_post_id(id):
    output = {}
    try:
        output = {
            'status': True,
            'post': Post.objects.get(id=id)
        }
    except Exception as ex:
        output = {
            'status': False,
            'message': ex
        }
    finally:
        return output