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
            
class CommentManage(View):
    def get(self, request, post_id, comment_id):
        exist_post = queries.check_exits_post(post_id)
        if exist_post:
            comment = queries.get_comment(comment_id)
            if comment['status']:
                # Edit comment
                form = forms.CommentForm(instance=comment['comment'])
                is_edit = True
            else:
                # create the new Comment
                form = forms.CommentForm()
                is_edit = False
                
            return render(request, 'conetnt/comment_manage.html', {
                'form': form,
                'is_edit': is_edit,
                'post_id': post_id,
                'comment_id': comment_id,
            })
        else:
            # not found post
            return redirect(reverse('list_post'))
    
    def post(self, request, post_id, comment_id):
        exist_post = queries.check_exits_post(post_id)
        if exist_post:
            comment = queries.get_comment(comment_id)
            if comment['status']:
                # Update Comment
                form = forms.CommentForm(request.POST, instance=comment['comment'])
                is_edit = True
            else:
                # Insert Comment
                form = forms.CommentForm(request.POST)
                is_edit = False
            
            if form.is_valid():
                form.save()
                return redirect(reverse('post_detail', args=[post_id]))
            else:
                return render(request, 'conetnt/comment_manage.html', {
                    'form': form,
                    'is_edit': is_edit,
                    'post_id': post_id,
                    'comment_id': comment_id,
                })
        else:
            # not found post
            return redirect(reverse('list_post'))