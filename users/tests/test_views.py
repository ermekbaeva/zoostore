from django.test import Client, TestCase
from django.urls import reverse
from users.models import User


class LoginViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='testuser', password='testpassword55@')

    def test_login_view_get(self):
        response = self.client.get(reverse('users:login'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'users/login.html')

    def test_login_view_post_valid_data(self):
        response = self.client.post(reverse('users:login'), {'username': 'testuser', 'password': 'testpassword55@'})
        self.assertEqual(response.status_code, 302)

    def test_signup_view_get(self):
        response = self.client.get(reverse('users:signup'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'users/signup.html')

    def test_signup_view_post_valid_data(self):
        response = self.client.post(reverse('users:signup'), {
            'username': 'newuser',
            'password1': 'Newuser123@',
            'password2': 'Newuser123@'
        })
        self.assertEqual(response.status_code, 200)

    def test_profile_view_authenticated(self):
        self.client.login(username='testuser', password='testpassword55@')
        response = self.client.get(reverse('users:profile'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'users/profile.html')

    def test_profile_view_unauthenticated(self):
        response = self.client.get(reverse('users:profile'))
        self.assertEqual(response.status_code, 302)

    def test_change_password_view_authenticated(self):
        self.client.login(username='testuser', password='testpassword55@')
        response = self.client.post(reverse('users:change_password'), {'old_password': 'testpassword55@', 'new_password1': 'newpassword77@', 'new_password2': 'newpassword77@'})
        self.assertEqual(response.status_code, 302)

    def test_change_password_view_unauthenticated(self):
        response = self.client.get(reverse('users:change_password'))
        self.assertEqual(response.status_code, 302)

    def test_logout_view_authenticated(self):
        self.client.login(username='testuser', password='testpassword55@')
        response = self.client.get(reverse('users:logout'))
        self.assertEqual(response.status_code, 302)

    def test_users_cart_view(self):
        response = self.client.get(reverse('users:users_cart'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'users/users_cart.html')