# tests.py
from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from django.contrib.auth import get_user_model
from rest_framework_simplejwt.tokens import RefreshToken

User = get_user_model()

class UsersViewSetTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            name="testuser",
            email="apple@gmail.com",
            username="apple123",
            password="12345"
        )
        self.user2 = User.objects.create_user(
            name="testuser2",
            email="apple1@gmail.com",
            username="apple1234",
            password="123145"
        )
        self.refresh_token = RefreshToken.for_user(self.user)
        self.access_token = str(self.refresh_token.access_token)

    def test_list_authenticated(self):
        # Create an instance of the API client
        client = APIClient()

        # Set the authentication token for the client
        client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.access_token}')

        # Define the URL for the list endpoint of your viewset
        url = 'http://localhost:8000/api/emr-users/'

        # Send a GET request to the list endpoint
        response = client.get(url)
        print('response', response)
        # Check that the response status code is 200 OK
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Check that the response data contains the expected number of objects
        # self.assertEqual(len(response.data), User.objects.count())

