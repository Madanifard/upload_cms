from django import forms
from .models import Post, PostComment

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = '__all__'