from django.test import TestCase
from django.urls import reverse

class UserRegistrationLoginProfileTest(TestCase):

    def test_registration_login_profile_access(self):
        response = self.client.post(reverse('users:signup'), {
            'username': 'testuser',
            'password1': 'Testpassword123',
            'password2': 'Testpassword123',
            'email': 'testuser@example.com',
            'first_name': 'Test',
            'last_name': 'User'
        })
        self.assertEqual(response.status_code, 302)

        response = self.client.post(reverse('users:login'), {
            'username': 'testuser',
            'password': 'Testpassword123'
        })
        self.assertEqual(response.status_code, 302)

        response = self.client.get(reverse('users:profile'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test')