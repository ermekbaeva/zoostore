from django.core.exceptions import ValidationError
from django.test import TestCase

from users.models import User


class UsersModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create(username="Blackhippo", password="10293847Black@")

    def test_str_method(self):
        self.assertEqual(str(self.user), "Blackhippo")

    def test_phone_number_max_length(self):
        user2=User(username="BlackBlack", password="Black1234_", phone_number="05502330956")
        with self.assertRaises(ValidationError):
            user2.full_clean()

