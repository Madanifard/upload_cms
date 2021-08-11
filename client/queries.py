from .models import SecurityQuestions


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
