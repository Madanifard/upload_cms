from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, viewsets
from rest_framework.decorators import action

from api import my_response
import content

from . import serializers
from client import queries as client_queries
from content import queries as conetnt_queries
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


class UserAddress(APIView):
    def get(self, request):
        addresses = client_queries.get_list_user_address(request.user.id)
        addresses_serializer = serializers.UserAddressSerializer(
            addresses, many=True)
        return Response(addresses_serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        request.data['user'] = request.user.id
        address_serializer = serializers.UserAddressSerializer(
            data=request.data)
        if address_serializer.is_valid():
            address_serializer.save()
            return Response(address_serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(address_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserAddressDetail(APIView):
    def get_address(self, user_id, address_id):
        return client_queries.get_user_address(user_id=user_id, address_id=address_id)

    def get(self, request, pk):
        addresses = self.get_address(user_id=request.user.id, address_id=pk)
        if addresses['status']:
            address_serializer = serializers.UserAddressSerializer(
                addresses['address'])
            return Response(address_serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(message_response(addresses['message']), status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        request.data['user'] = request.user.id
        addresses = self.get_address(user_id=request.user.id, address_id=pk)
        if addresses['status']:
            address_serializer = serializers.UserAddressSerializer(
                addresses['address'], data=request.data)
            if address_serializer.is_valid():
                address_serializer.save()
                return Response(address_serializer.data, status=status.HTTP_200_OK)
            else:
                return Response(address_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(message_response(addresses['message']), status=status.HTTP_404_NOT_FOUND)


class PostViewSet(viewsets.ViewSet):

    @action(methods=['get'], detail=False, url_path='user/list', name='post_user_list', url_name='post_user_list')
    def post_user_list(self, request):
        list_post = conetnt_queries.get_user_list_post(request.user.id)
        list_post_serializer = serializers.PostSerializer(list_post, many=True)
        return Response(list_post_serializer.data, status=status.HTTP_200_OK)

    @action(methods=['post'], detail=False, url_path='user/create', name='post_user_create', url_name='post_user_create')
    def post_user_create(self, request):
        request.data['user'] = request.user.id
        post_serializer = serializers.PostSerializer(data=request.data)
        if post_serializer.is_valid():
            post_serializer.save()
            return Response(post_serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(post_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @action(methods=['PUT'], detail=False, url_path='user/update/(?P<pk>\d+)', name='post_user_update', url_name='post_user_update')
    def post_user_update(self, request, pk):
        request.data['user'] = request.user.id
        post = conetnt_queries.get_user_post(
            user_id=request.user.id, post_id=pk)
        if post['status']:
            post_serializer = serializers.PostSerializer(
                post['post'], data=request.data)
            if post_serializer.is_valid():
                post_serializer.save()
                return Response(post_serializer.data, status=status.HTTP_200_OK)
            else:
                return Response(post_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(post['message'], status=status.HTTP_404_NOT_FOUND)


class PostCommentViewSet(viewsets.ViewSet):

    @action(methods=['get'], detail=False, url_path='list/(?P<post_id>\d+)', name='post_comments', url_name='post_comments')
    def post_comments(self, request, post_id):
        comments = conetnt_queries.get_comment_post(post_id)
        comments_serializer = serializers.PostCommentsSerializer(
            comments, many=True)
        return Response(comments_serializer.data, status=status.HTTP_200_OK)

    @action(methods=['post'], detail=False, url_path='create/(?P<post_id>\d+)', name='post_comment_create', url_name='post_comment_create')
    def post_comment_create(self, request, post_id):
        exists_post = conetnt_queries.check_exits_post(id=post_id)
        if exists_post:
            request.data['post'] = post_id
            comment_serializer = serializers.PostCommentsSerializer(
                data=request.data)
            if comment_serializer.is_valid():
                comment_serializer.save()
                return Response(comment_serializer.data, status=status.HTTP_200_OK)
            else:
                return Response(comment_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(message_response("not found data"), status=status.HTTP_404_NOT_FOUND)

    @action(methods=['post'], detail=False, url_path='(?P<post_id>\d+)/replay/(?P<comment_id>\d+)', name='post_comment_replay', url_name='post_comment_replay')
    def post_comment_replay(self, request, post_id, comment_id):
        exists_post = conetnt_queries.check_exists_comment_post(
            post_id=post_id, comment_id=comment_id)
        if exists_post:
            request.data['post'] = post_id
            request.data['replay_id'] = comment_id
            replay_comment_serializer = serializers.PostCommentsSerializer(
                data=request.data)
            if replay_comment_serializer.is_valid():
                replay_comment_serializer.save()
                return Response(replay_comment_serializer.data, status=status.HTTP_200_OK)
            else:
                return Response(replay_comment_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(message_response("not found data"), status=status.HTTP_404_NOT_FOUND)
