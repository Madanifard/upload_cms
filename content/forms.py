from django import forms
from .models import Post, PostComment

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = '__all__'

class CommentForm(forms.ModelForm):
    class Meta:
        model = PostComment
        fields = '__all__'