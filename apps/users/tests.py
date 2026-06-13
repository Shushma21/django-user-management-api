from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from .models import User

class UserTests(TestCase):
    
    def setUp(self):
        self.client = APIClient()

    def test_register_user(self):
        data = {
            'username':'testuser',
            'email':'test@gmail.com',
            'password': 'Test@1234',
            'role':'user'
        }

        response = self.client.post('/api/users/register/',data)
        self.assertEqual(response.status_code,201)

    def test_register_duplicate_email(self):
        data = {
            'username': 'testuser',
            'email': 'test@gmail.com',
            'password': 'Test@1234',
            'role': 'user'
        }
        self.client.post('/api/users/register/', data)
        response = self.client.post('/api/users/register/', data)
        self.assertEqual(response.status_code, 400)

    def test_login(self):
        User.objects.create_user(username='testuser', email='test@gmail.com', password='Test@1234')
        data = {'username': 'testuser', 'password': 'Test@1234'}
        response = self.client.post('/api/token/', data)
        self.assertEqual(response.status_code, 200)
        self.assertIn('access', response.data)

    def test_get_current_user(self):
        user = User.objects.create_user(username='testuser', email='test@gmail.com', password='Test@1234')
        self.client.force_authenticate(user=user)
        response = self.client.get('/api/users/me/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['data']['username'], 'testuser')

    def test_admin_can_list_users(self):
        admin = User.objects.create_user(username='admin', email='admin@gmail.com', password='Admin@1234', role='admin')
        self.client.force_authenticate(user=admin)
        response = self.client.get('/api/users/')
        self.assertEqual(response.status_code, 200)

    def test_regular_user_cannot_list_users(self):
        user = User.objects.create_user(username='testuser', email='test@gmail.com', password='Test@1234', role='user')
        self.client.force_authenticate(user=user)
        response = self.client.get('/api/users/')
        self.assertEqual(response.status_code, 403)