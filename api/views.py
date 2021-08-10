from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from . import serializers, my_response
from client.models import SecurityQuestions as model_SecurityQuestions


class UserRegister(APIView):
    authentication_classes = []  # disables authentication
    permission_classes = []  # disables permission

    def post(self, request):
        user_serializer = serializers.UserSerializer(data=request.data)
        if user_serializer.is_valid():
            user_serializer.save()
            return Response(my_response.message_response('successful add new user'), status=status.HTTP_200_OK)
        else:
            return Response(user_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class SecurityQuestions(APIView):
    def get(self, request):
        pass
        # TODO : SHow list security question
        # user_questions = model_SecurityQuestions.objects.filter(user_id=request.user.id)
        # question_list = []
        # for question in user_questions:
        #     question_list.append({
        #         'question': question['question'],
        #         'answer': question['answer']
        #     }) 
        # questions_serializer = serializers.SecurityQuestionsSerializer(user_questions, many=True)
        # return  Response(questions_serializer.data, status=status.HTTP_200_OK)
        

    def post(self, request):
        request.data['user_id'] = request.user.id
        questions_serializer = serializers.SecurityQuestionsSerializer(
            data=request.data)
        if questions_serializer.is_valid():
            questions_serializer.save()
            return Response(my_response.message_response('successful add security question'), status=status.HTTP_200_OK)
        else:
            return Response(questions_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# class RefreshPassword(APIView):
#     def get(self):
#         pass
#
#     def put(self, request):
#         pass
