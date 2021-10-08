from datetime import datetime
import random
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

class UserDetails(View):
    def get(self, request, user_id):
        queries.check_exists_user(user_id)
        user_detail = queries.user_details(user_id)
        if user_detail['status']:
            return render(request, 'client/user_details.html', {
                'status': user_detail['status'],
                'user': user_detail['user'],
                'information': user_detail['information'],
                'mobiles': user_detail['mobiles'],
                'address': user_detail['address'],
                'squrity_questions': user_detail['squrity_questions'],
            })
        else:
            return render(request, 'client/user_details.html', {
                'status': user_detail['status'],
                'message': user_detail['message'],
            })

class InformationUserManage(View):
    def get(self, request, user_id):
        queries.check_exists_user(user_id)
        infromation_user = queries.get_user_information(user_id)
        if infromation_user['status']:
            form = forms.InformationUser(instance=infromation_user['information'])
            is_edit = True
        else:
            form = forms.InformationUser()
            is_edit = False
        
        ## form.fields['national_code'].initial = 'testssssssss'

        return render(request, 'client/information_user_manage.html', {
            'form': form,
            'is_edit': is_edit,
            'user_id': user_id,
        })
            
            
    def post(self, request, user_id):
        infromation_user = queries.get_user_information(user_id)
        if infromation_user['status']:
            form = forms.InformationUser(
                request.POST,
                request.FILES,
                instance=infromation_user['information'])
            is_edit = True
        else:
            form = forms.InformationUser(request.POST, request.FILES)
            is_edit = False
        
        if form.is_valid():
            form.save()
            return redirect(reverse('user_detail', args=[user_id]))
        else:
            return render(request, 'client/information_user_manage.html', {
                'form': form,
                'is_edit': is_edit,
                'user_id': user_id,
            })

class MobileUserManage(View):
    def get(self, request, user_id=0, mobile_id=0):
        queries.check_exists_user(user_id)
        is_edit = False
        if mobile_id:
            mobile = queries.get_mobile_user(mobile_id)
            if mobile['status']:
                form = forms.MobileUser(instance=mobile['mobile'])
                is_edit = True
            else:
                form = forms.MobileUser()
        else:
            form = forms.MobileUser()
        
        form.fields['date_sent'].initial = datetime.today()
        form.fields['sms_code'].initial = random.sample(range(1111, 9999), 1)[0]
        
        return render(request, 'client/mobile_user_manage.html', {
            'form': form,
            'is_edit': is_edit,
            'user_id': user_id,
            'mobile_id': mobile_id,
        })
        
    def post(self, request, user_id=0, mobile_id=0):
        mobile = queries.get_mobile_user(mobile_id)
        if mobile['status']:
            form = forms.MobileUser(request.POST, instance=mobile['mobile'])
            is_edit = True
        else:
            form = forms.MobileUser(request.POST)
            is_edit = False
        
        if form.is_valid():
            form.save()
            return redirect(reverse('user_detail', args=[user_id]))
        else:
            return render(request, 'client/mobile_user_manage.html', {
                'form': form,
                'is_edit': is_edit,
                'user_id': user_id,
                'mobile_id': mobile_id,
            })
            
class AddressManagement(View):
    def get(self, request, user_id, address_id=0):
        queries.check_exists_user(user_id)
        is_edit = False
        if address_id:
            address = queries.get_address_user(address_id)
            if address['status']:
                form = forms.AddressUser(instance=address['address'])
                is_edit = True
            else:
                form = forms.AddressUser()
        else:
            form = forms.AddressUser()
            
        return render(request, 'client/address_user_manage.html', {
            'form': form,
            'is_edit': is_edit,
            'user_id': user_id,
            'address_id': address_id,
        })
    
    def post(self, request, user_id=0, address_id=0):
        address = queries.get_address_user(address_id)
        if address['status']:
            form = forms.AddressUser(request.POST, instance=address['address'])
            is_edit = True
        else:
            form = forms.AddressUser(request.POST)
            is_edit = False
        
        if form.is_valid():
            form.save()
            return redirect(reverse('user_detail', args=[user_id]))
        else:
            return render(request, 'client/address_user_manage.html', {
                'form': form,
                'is_edit': is_edit,
                'user_id': user_id,
                'address_id': address_id,
            })