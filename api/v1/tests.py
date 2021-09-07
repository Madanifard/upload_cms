from django.test import TestCase
from rest_framework.test import APIClient
from django.urls import reverse
from rest_framework import status
from django.contrib.auth.models import User

class TokenSettings:
    jwt_data = {
        'username': 'AmirAPITest',
        'password': 'Amir123Test'
    }
    token = 'token generated'
    user_id = 0

    def create_user(self):
        user = User.objects.create_user(username=self.jwt_data['username'], password=self.jwt_data['password'])
        self.user_id = user.id


class ApiVersion1Test(TestCase):

    def setUp(self):
        self.token_obj = TokenSettings()
        self.token_obj.create_user()

        self.client = APIClient()

    def test_jwt_token(self):
        url = reverse('token_auth')
        response = self.client.post(
            url, data=self.token_obj.jwt_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK, response.data)
        self.token_obj.token = response.data['token']

