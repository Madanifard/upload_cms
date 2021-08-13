from .models import SecurityQuestions, Information


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
