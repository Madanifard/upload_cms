from django.contrib.auth import models
from django.http.response import Http404
from .models import Address, SecurityQuestions, Information, Mobiles
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404

def get_user_security_questions(user_id):
    user_questions = SecurityQuestions.objects.filter(user_id=user_id)
    question_list = []
    for question in user_questions:
        question_list.append({
            'question': question.question,
            'answer': question.answer
        })
    return {
        'items': question_list
    }


def get_user_information(user_id):
    output = {}
    try:
        output = {
            'status': True,
            'information': Information.objects.get(user_id=user_id)
        }
    except:
        output = {
            'status': False,
            'message': 'not have any Data for user'
        }

    finally:
        return output


def get_list_user_mobile(user_id):
    return Mobiles.objects.filter(user_id=user_id)


def get_user_mobile(user_id, mobile_id):
    output = {}
    try:
        output = {
            'status': True,
            'mobile': Mobiles.objects.get(user_id=user_id, id=mobile_id)
        }
    except:
        output = {
            'status': False,
            'message': "not found Data"
        }
    finally:
        return output


def get_list_user_address(user_id):
    return Address.objects.filter(user_id=user_id)


def get_user_address(user_id, address_id):
    output = {}
    try:
        output = {
            'status': True,
            'address': Address.objects.get(user_id=user_id, id=address_id)
        }
    except:
        output = {
            'status': False,
            'message': "data not found"
        }
    finally:
        return output

def get_list_admin_user():
    output = {}
    try:
        output = {
            'status': True,
            'users': User.objects.all(),
        }
    except:
        output = {
            'status': False,
            'message': 'not fount user',
        }
    finally:
        return output

def get_user(id):
    output = {}
    try:
        output = {
            'status': True,
            'user': User.objects.get(pk=id)
        }
    except:
        output = {
            'status': False,
            'message': 'not fount user',
        }
    finally:
        return output
    
def get_list_user_infromation():
    output = {}
    try:
        output = {
            'status': True,
            'inortmation_list': Information.objects.all()
        }
    except:
        output = {
            'status': False,
            'message': 'Not Fount Data'
        }
    finally:
        return output
    
def check_exists_user(user_id):
    get_object_or_404(User, pk=user_id)
    
def user_details(user_id):
    output = {}
    try:
        user_detail = User.objects.select_related().get(pk=user_id)
        information = user_detail.user_information
        mobiles = user_detail.user_mobile
        address = user_detail.user_address
        squrity_questions = user_detail.user_security_questions
        output = {
            'status': True,
            'user': user_detail,
            'information': information,
            'mobiles': mobiles,
            'address': address,
            'squrity_questions': squrity_questions,
        }
    except Exception as ex:
        output = {
            'status': False,
            'message': ex
        }
    finally:
        return output

def get_mobile_user(mobile_id):
    output = {}
    try:
        output = {
            'status': True,
            'mobile': Mobiles.objects.get(id=mobile_id)
        }
    except Exception as ex:
        output = {
            'status': False,
            'message': 'Mobile not Found'
        }
    finally:
        return output