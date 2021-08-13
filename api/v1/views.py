from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from . import serializers
from client.queries import get_user_information
from api.my_response import message_response


class UserInformation(APIView):

    def find_user_information(self, user_id):
        return get_user_information(user_id)

    def get(self, request):
        user_information = self.find_user_information(request.user.id)
        if user_information['status']:
            information = serializers.UserInformationSerializers(user_information['information'])
            return Response(information.data, status=status.HTTP_200_OK) 
        else :
            return Response(message_response(user_information['message']), status=status.HTTP_404_NOT_FOUND)    
    
    def post(self, request):
        request.data['user'] = request.user.id
        if 'mode' in request.data.keys() and request.data['mode'] == "INSERT":
            information = serializers.UserInformationSerializers(data=request.data)
            if information.is_valid():
                information.save()
                return Response(information.data, status=status.HTTP_200_OK)
            else:
                return Response(information.errors, status=status.HTTP_400_BAD_REQUEST)    
        elif 'mode' in request.data.keys() and request.data['mode'] == "UPDATE":
            user_information = self.find_user_information(request.user.id)
            if user_information['status']:
                information = serializers.UserInformationSerializers(user_information['information'], data=request.data)
                if information.is_valid():
                    information.save()
                    return Response(information.data, status=status.HTTP_200_OK)
                else:
                    return Response(information.errors, status=status.HTTP_400_BAD_REQUEST)
            else :
                return Response(message_response(user_information['message']), status=status.HTTP_404_NOT_FOUND) 
        else:
            return Response(message_response('whats your Mode man!!'), status=status.HTTP_404_NOT_FOUND)
