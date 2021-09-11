import io
from PIL import Image
from django.test import TestCase
from rest_framework.test import APIClient
from django.urls import reverse
from rest_framework import status
from django.contrib.auth.models import User


class UserInformationTest(TestCase):

    def create_user(self, user_data):
        User.objects.create_user(
            username=user_data['username'],
            password=user_data['password'])
    
    def generate_photo_file(self):
        file = io.BytesIO()
        image = Image.new('RGBA', size=(100, 100), color=(155, 0, 0))
        image.save(file, 'png')
        file.name = 'test.png'
        file.seek(0)
        return file

    def setUp(self):
        self.client = APIClient()

        self.jwt_data = {
            'username': 'AmirAPITest',
            'password': 'Amir123Test',
        }
        self.create_user(self.jwt_data)

    def test_user_information(self):
        # generate token
        url = reverse('token_auth')
        response = self.client.post(url, data=self.jwt_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK, response.data)
        token = response.data['token']

        # POST - create new information
        url = reverse('v1_user_information')
        avatar = self.generate_photo_file()
        data_user = {
            'national_code' : '123456333333',
            'nationality': 'Iranian',
            'passport_code' : '123465',
            'avatar' : avatar,
            'mode': 'INSERT'
        }
        self.client.credentials(HTTP_AUTHORIZATION='JWT ' + token)
        response = self.client.post(url, data=data_user, format='multipart')
        self.assertEqual(response.status_code, status.HTTP_200_OK, response.data)

        # POST - Update the information
        url = reverse('v1_user_information')
        avatar = self.generate_photo_file()
        data_user = {
            'national_code' : '1234563333335',
            'nationality': 'Iranian',
            'passport_code' : '123465',
            'avatar' : avatar,
            'mode': 'UPDATE'
        }
        self.client.credentials(HTTP_AUTHORIZATION='JWT ' + token)
        response = self.client.post(url, data=data_user, format='multipart')
        self.assertEqual(response.status_code, status.HTTP_200_OK, response.data)

        # GET - get user information
        url = reverse('v1_user_information')
        self.client.credentials(HTTP_AUTHORIZATION='JWT ' + token)
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK, response.data)

