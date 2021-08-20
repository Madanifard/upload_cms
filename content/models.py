from django.db import models
from django.contrib.auth.models import User
from django.db.models.base import Model
from django.db.models.deletion import CASCADE

class Post(models.Model):
    user = models.ForeignKey(User, on_delete=CASCADE, related_name='content_post')
    title = models.CharField(max_length=200)
    summery = models.TextField(blank=True, default='')
    text = models.TextField()
    descripe_seo = models.CharField(max_length=300)
    key_word_seo = models.TextField()
    image = models.ImageField(upload_to='posts')
    showable = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True, blank=True)
    updated_at = models.DateTimeField(auto_now_add=True, blank=True)

class PostComment(models.Model):
    post = models.ForeignKey(Post, on_delete=CASCADE, related_name='content_post_comment')
    subject = models.CharField(max_length=150)
    email = models.EmailField()
    name = models.CharField(max_length=150)
    text = models.TextField()
    replay_id = models.IntegerField(blank=True, default=0)
    verified = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True, blank=True)
