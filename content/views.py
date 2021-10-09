from django.db.models import query
from django.shortcuts import redirect, render
from django.urls import reverse
from django.views import View
from . import queries, forms

def dashboard(request):
    return render(request, 'content/dashboard.html')


class PostList(View):
    def get(self, request):
        posts = queries.get_all_post()
        return render(request, 'content/all_post.html', {
            'posts': posts['posts'],
        })

class PostDetail(View):
    def get(self, request, id):
        post = queries.get_post_id(id)
        return render(request, 'content/blog_detail.html', {
            'post': post['post']
        })

class PostManage(View):
    def get(self, request, id=0):
        is_edit = False
        if id:
            # edit
            post = queries.get_post_id(id)
            if post['status']:
                form = forms.PostForm(instance=post['post'])
                is_edit = True
            else:
                # post
                form = forms.PostForm()
        else:
            # post
            form = forms.PostForm()
        
        return render(request, 'content/post_manage.html', {
            'form': form,
            'is_edit': is_edit,
            'id': id,
        })
    
    def post(self, request, id=0):
        post = queries.get_post_id(id)
        if post['status']:
            form = forms.PostForm(
                request.POST,
                request.FILES,
                instance=post['post']
            )
            is_edit = True
        else:
            form = forms.PostForm(request.POST, request.FILES)
            is_edit = False
        
        if form.is_valid():
            form.save()
            return redirect(reverse('post_detail', args=[id]))
        else:
            return render(request, 'content/post_manage.html', {
                'form': form,
                'is_edit': is_edit,
                'id': id,
            })