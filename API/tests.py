from rest_framework.test import APITestCase
from django.urls import reverse
from rest_framework import status
from .models import Users

class UserSignupViewSetTests(APITestCase):
    def test_user_signup_success(self):
        url = reverse('usersignup')  # Assuming you have defined a proper URL name for this viewset
        data = {
            'username': 'testuser',
            'email': 'test@example.com',
            'phone_number': '9645610883',
            'password': 'testpassword',
            'confirm_password': 'testpassword'
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_user_signup_validation_error(self):
        url = reverse('usersignup')  # Assuming 'usersignup' is the name you've given to the URL
        # Missing 'confirm_password' field intentionally to trigger validation error
        data = {
            'username': 'testuser',
            'email': 'test@example.com',
            'phone_number': '9234567890',
            'password': 'testpassword',
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

class DriverSignupViewSetTests(APITestCase):
    def test_driver_signup_success(self):
        url = reverse('ridersignup')  # Assuming you have defined a proper URL name for this viewset
        data = {
            "username": "abhijith",
            "email": "abhijith@gmail.com",
            "phone_number": "7845121289",
            "password": "abhijith@123",
            "confirm_password": "abhijith@123",
            "vehicle_number":"kl02be8203"
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_driver_signup_validation_error(self):
        url = reverse('ridersignup')  # Assuming 'usersignup' is the name you've given to the URL
        # Missing 'confirm_password' field intentionally to trigger validation error
        data = {
            "username": "abhijith",
            "email": "abhijith@gmail.com",
            "phone_number": "7845121289",
            "password": "abhijith@123",
            "vehicle_number":"kl02be8203"
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

class UserLoginViewSetTests(APITestCase):
    def test_user_login_success(self):
        # Create a test user
        Users.objects.create(email='test@gmail.com', password='testpassword',is_user=True)
        # URL for the login endpoint
        url = reverse('userlogin')
        # Data to send in the request
        data = {
            'email': 'test@gmail.com',
            'password': 'testpassword'
        }
        breakpoint()
        # Make POST request to login endpoint
        response = self.client.post(url, data, format='json')
        if response.status_code != status.HTTP_201_CREATED:
            print(response.content.decode())
        # Assert response status code
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # Assert response data
        self.assertIn('access', response.data)
        self.assertIn('refresh', response.data)
        self.assertEqual(response.data['message'], 'User logged in successfully')