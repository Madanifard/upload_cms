import client
import datetime
from django.test.utils import override_settings
from django.utils import timezone
import io
from PIL import Image
from django.conf import settings
from django.test import TestCase
from rest_framework.test import APIClient, APITestCase
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

        self.client.credentials(HTTP_AUTHORIZATION='JWT ' + token)

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
        response = self.client.post(url, data=data_user, format='multipart')
        self.assertEqual(response.status_code, status.HTTP_200_OK, response.data)

        # GET - get user information
        url = reverse('v1_user_information')  
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK, response.data)





class UserMobileTest(TestCase):
    def create_user(self, user_data):
        User.objects.create_user(
            username=user_data['username'],
            password=user_data['password'])

    def setUp(self):
        self.client = APIClient()

        self.jwt_data = {
            'username': 'AmirAPITest',
            'password': 'Amir123Test',
        }
        self.create_user(self.jwt_data)

    @override_settings(USE_TZ=False)
    def test_mobile_user(self):
        # generate token
        url = reverse('token_auth')
        response = self.client.post(url, data=self.jwt_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK, response.data)
        token = response.data['token']

        self.client.credentials(HTTP_AUTHORIZATION='JWT ' + token)

        # POST - create the mobile phone
        url = reverse('v1_user_mobile')
        mobile_data = {
            "mobile": "09203176164"
        }
        response = self.client.post(url, data=mobile_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK, response.data)
        mobile_id = response.data['id'] 

        # GET - get list user mobile
        url = reverse('v1_user_mobile')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK, response.data)

        # GET - get the one mobile phone
        url = reverse('v1_user_mobile_detail', kwargs={'pk':mobile_id})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK, response.data)

        # PUT - update the mobile information
        url = reverse('v1_user_mobile_detail', kwargs={'pk':mobile_id})
        response = self.client.put(url, data=mobile_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK, response.data)

class UserAddress(APITestCase):

    def create_user(self, user_data):
        User.objects.create_user(
            username=user_data['username'],
            password=user_data['password'])

    def setUp(self):
        self.client = APIClient()

        self.jwt_data = {
            'username': 'AmirAPITest',
            'password': 'Amir123Test',
        }
        self.create_user(self.jwt_data)
    
    def test_user_address(self):
        # generate token
        url = reverse('token_auth')
        response = self.client.post(url, data=self.jwt_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK, response.data)
        token = response.data['token']

        self.client.credentials(HTTP_AUTHORIZATION='JWT ' + token)

        # POST create the new address
        url = reverse('v1_user_address')
        address_data = {
            "directions": "address directions2",
            "postal_code": "12345612",
            "phone": "+9855002230025812",
            "latitude": "35.719889",
            "longitude": "51.468056",
            "user": "100"
        }
        response = self.client.post(url, data=address_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK, response.data)
        address_id = response.data['id']

        # GET get list of address
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK, response.data)

        # GET get the one 
        url = reverse('v1_user_address_detail', kwargs={'pk': address_id})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK, response.data)

        # PUT update the address info
        response = self.client.put(url, data=address_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK, response.data)


