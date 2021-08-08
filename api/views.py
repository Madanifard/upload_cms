from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from . import serializers, my_response


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


# class RefreshPassword(APIView):
#     def get(self):
#         pass
#
#     def put(self, request):
#         pass
