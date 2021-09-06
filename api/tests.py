from django.test import TestCase
from rest_framework.test import APIRequestFactory
from api import views
from django.urls import reverse


class UseregisterTest(TestCase):

    def setUp(self):
        self.factory = APIRequestFactory()

    def test_user_registory(self):
        url = reverse('user_register')
        register_data = {
            "username": "AmirAPITest",
            "password": "Amir123Test",
            "email": "a@a.com",
            "first_name": "Amirreza",
            "last_name": "Madanifard",
        }
        request = self.factory.post(url, data=register_data, format='json')
        response = views.UserRegister.as_view()(request)
        response.render()
        self.assertEqual(response.status_code, 200)
