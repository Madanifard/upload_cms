from django.test import TestCase
from rest_framework.test import APIClient
from django.urls import reverse
from rest_framework import status
from django.contrib.auth.models import User


class ApiVersion1Test(TestCase):

    def create_user(self, user_data):
        user = User.objects.create_user(
            username=user_data['username'],
            password=user_data['password'])

    def setUp(self):
        self.client = APIClient()
        
        self.jwt_data = {
            'username': 'AmirAPITest',
            'password': 'Amir123Test'
        }
        self.create_user(self.jwt_data)
        self.token = 'token generated'

    def test_jwt_token(self):
        url = reverse('token_auth')
        response = self.client.post(url, data=self.jwt_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK, response.data)
        self.token = response.data['token']
