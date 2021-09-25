from django.shortcuts import render
from django.views import View
from . import forms, queries

class AdminUser(View):
    def get(self, request):
        # user_form = forms.UserForm()
        users = queries.get_list_admin_user()
        if users['status']:
            users = users['users']
        else:
            users = []
        return render(request, 'client/show_list_admin_user.html', {
            'users': users,
        })