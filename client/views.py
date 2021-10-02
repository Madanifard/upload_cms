from django.http.response import HttpResponseNotFound
from django.shortcuts import redirect, render
from django.views import View
from . import forms, queries
from django.urls import reverse

class AdminUserList(View):
    def get(self, request):
        users = queries.get_list_admin_user()
        if users['status']:
            users = users['users']
        else:
            users = []
        return render(request, 'client/show_list_admin_user.html', {
            'users': users,
        })

class AdminUserManage(View):
    def get(self, request, id=0):
        if id != 0:
            # Update mode 
            user = queries.get_user(id)
            if user['status']:
                user = user['user']
                form = forms.UserForm(instance=user)
            else:
                # not found any user
                return redirect(reverse('manage_admin_user'))
        else:
            # create new User
            form = forms.UserForm()
            id = 0
        
        return render(request, 'client/admin_user_manage.html', {
            'form' : form,
            'id': id,
        })

    def post(self, request, id=0):
        # ? TODO: check this method
        if id != 0:
            user = queries.get_user(id)
            form = forms.UserForm(request.POST, instance=user)
        else:
            form = forms.UserForm(request.POST) 

        if form.is_valid():
            form.save()
            
        return redirect(reverse('list_admin_user'))


class InformationUser(View):
    def get(self, request):
        list_user_information = queries.get_list_user_infromation()
        if list_user_information['status']:
            inortmation_list = list_user_information['inortmation_list']
        else:
            inortmation_list = []
        
        return render(request, 'client/list_information_user.html', {
            'inortmation_list': inortmation_list
        })