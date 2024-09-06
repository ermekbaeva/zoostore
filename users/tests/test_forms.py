from django.test import TestCase
from users.forms import (
    UserLoginForm,
    UserRegistrationForm,
    ProfileForm,
    CustomPasswordChangeForm
)
from users.models import User


class UserLoginFormTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='mer1bel', password='430467218955Ee')
        
    def test_form_fields(self):
        form = UserLoginForm()
        self.assertEqual(list(form.fields), ['username', 'password'])

    def test_form_valid_data(self):
        form = UserLoginForm(data={'username': 'mer1bel', 'password': '430467218955Ee'})
        self.assertTrue(form.is_valid())

    def test_form_invalid_data(self):
        form = UserLoginForm(data={'username': '', 'password': ''})
        self.assertFalse(form.is_valid())


class UserRegistrationFormTest(TestCase):
    def test_form_fields(self):
        form = UserRegistrationForm()
        self.assertEqual(list(form.fields), ['first_name', 'last_name', 'username', 'email', 'password1', 'password2'])

    def test_form_valid_data(self):
        form = UserRegistrationForm(data={
            'first_name': 'John',
            'last_name': 'Doe',
            'username': 'johndoe',
            'email': 'johndoe@example.com',
            'password1': 'strongPassword123',
            'password2': 'strongPassword123'
        })
        self.assertTrue(form.is_valid())

    def test_form_invalid_data(self):
        form = UserRegistrationForm(data={
            'first_name': '',
            'last_name': '',
            'username': '',
            'email': '',
            'password1': 'pass123',
            'password2': 'pass456'
        })
        self.assertFalse(form.is_valid())


class ProfileFormTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='johndoe', password='strongPassword123', email='johndoe@example.com')

    def test_form_fields(self):
        form = ProfileForm(instance=self.user)
        self.assertEqual(list(form.fields), ['image', 'first_name', 'last_name', 'username', 'email', 'password'])

    def test_form_valid_data(self):
        form = ProfileForm(data={
            'first_name': 'John',
            'last_name': 'Doe',
            'username': 'johndoe',
            'email': 'johndoe@example.com'
        }, instance=self.user)
        self.assertTrue(form.is_valid())

    def test_form_invalid_data(self):
        form = ProfileForm(data={'username': ''}, instance=self.user)
        self.assertFalse(form.is_valid())


class CustomPasswordChangeFormTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='johndoe', password='old_password')

    def test_form_fields(self):
        form = CustomPasswordChangeForm(user=self.user)
        self.assertEqual(list(form.fields), ['old_password', 'new_password1', 'new_password2'])

    def test_form_valid_data(self):
        form = CustomPasswordChangeForm(data={
            'old_password': 'old_password',
            'new_password1': 'new_password123',
            'new_password2': 'new_password123'
        }, user=self.user)
        self.assertTrue(form.is_valid())

    def test_form_invalid_data(self):
        form = CustomPasswordChangeForm(data={
            'old_password': 'wrong_password',
            'new_password1': 'new_password123',
            'new_password2': 'new_password456'
        }, user=self.user)
        self.assertFalse(form.is_valid())