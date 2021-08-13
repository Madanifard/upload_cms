from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from . import serializers, my_response
from client.queries import get_user_security_questions


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
        return Response(get_user_security_questions(request.user.id), status=status.HTTP_200_OK)

    def post(self, request):
        request.data['user_id'] = request.user.id
        questions_serializer = serializers.SecurityQuestionsSerializer(
            data=request.data)
        if questions_serializer.is_valid():
            questions_serializer.save()
            return Response(my_response.message_response('successful add security question'), status=status.HTTP_200_OK)
        else:
            return Response(questions_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
