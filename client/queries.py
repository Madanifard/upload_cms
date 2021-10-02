from .models import Address, SecurityQuestions, Information, Mobiles
from django.contrib.auth.models import User

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