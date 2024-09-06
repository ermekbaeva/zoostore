from django.test import Client, TestCase
from django.urls import reverse

from users.models import User


class UserUrlsTest(TestCase):
    def setUp(self):
        self.client=Client()
        self.user = User.objects.create(username='testuser', password='testpassword55@')

    def test_login_url(self):
        url = reverse('users:login')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_signup_url(self):
        url = reverse('users:signup')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_profile_url(self):
        self.client.login(username='testuser', password='testpassword55@')
        url = reverse('users:profile')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 302)

    def test_change_password_url(self):
        self.client.login(username='testuser', password='testpassword55@')
        url = reverse('users:change_password')
        response = self.client.post(url, {'old_password': 'testpassword55@', 'new_password1': 'newpassword77@', 'new_password2': 'newpassword77@'})
        self.assertEqual(response.status_code, 302)

    def test_logout_url(self):
        self.client.login(username='testuser', password='testpassword55@')
        url = reverse('users:logout')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 302)

    def test_users_cart_url(self):
        self.client.login(username='testuser', password='testpassword55@')
        url = reverse('users:users_cart')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
