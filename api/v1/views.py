from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from . import serializers
from client import queries as client_queries
from api.my_response import message_response


class UserInformation(APIView):

    def find_user_information(self, user_id):
        return client_queries.get_user_information(user_id)

    def get(self, request):
        user_information = self.find_user_information(request.user.id)
        if user_information['status']:
            information = serializers.UserInformationSerializers(
                user_information['information'])
            return Response(information.data, status=status.HTTP_200_OK)
        else:
            return Response(message_response(user_information['message']), status=status.HTTP_404_NOT_FOUND)

    def post(self, request):
        request.data['user'] = request.user.id
        if 'mode' in request.data.keys() and request.data['mode'] == "INSERT":
            information = serializers.UserInformationSerializers(
                data=request.data)
            if information.is_valid():
                information.save()
                return Response(information.data, status=status.HTTP_200_OK)
            else:
                return Response(information.errors, status=status.HTTP_400_BAD_REQUEST)
        elif 'mode' in request.data.keys() and request.data['mode'] == "UPDATE":
            user_information = self.find_user_information(request.user.id)
            if user_information['status']:
                information = serializers.UserInformationSerializers(
                    user_information['information'], data=request.data)
                if information.is_valid():
                    information.save()
                    return Response(information.data, status=status.HTTP_200_OK)
                else:
                    return Response(information.errors, status=status.HTTP_400_BAD_REQUEST)
            else:
                return Response(message_response(user_information['message']), status=status.HTTP_404_NOT_FOUND)
        else:
            return Response(message_response('whats your Mode man!!'), status=status.HTTP_404_NOT_FOUND)


class UserMobile(APIView):
    def get(self, request):
        user_mobiles = client_queries.get_list_user_mobile(request.user.id)
        mobile_serializer = serializers.UserMobileSerializers(
            user_mobiles, many=True)
        return Response(mobile_serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        request.data['user'] = request.user.id
        mobile_serializer = serializers.UserMobileSerializers(
            data=request.data)
        if mobile_serializer.is_valid():
            mobile_serializer.save()
            return Response(mobile_serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(mobile_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserMobileDetail(APIView):
    def get_mobile(self, user_id, mobile_id):
        return client_queries.get_user_mobile(user_id, mobile_id)

    def get(self, request, pk):
        mobile = self.get_mobile(request.user.id, pk)
        if mobile['status']:
            mobile_serializer = serializers.UserMobileSerializers(
                mobile['mobile'])
            return Response(mobile_serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(message_response(mobile['message']), status=status.HTTP_404_NOT_FOUND)

    def put(self, request, pk):
        request.data['user'] = request.user.id
        mobile = self.get_mobile(user_id=request.user.id, mobile_id=pk)
        if mobile['status']:
            mobile_serializer = serializers.UserMobileSerializers(
                mobile['mobile'], data=request.data)
            if mobile_serializer.is_valid():
                mobile_serializer.save()
                return Response(mobile_serializer.data, status=status.HTTP_200_OK)
            else:
                return Response(mobile_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(message_response(mobile['message']), status=status.HTTP_404_NOT_FOUND)
