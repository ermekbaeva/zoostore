from decimal import Decimal
from django.test import TestCase, Client
from django.urls import reverse
from carts.models import Cart
from goods.models import Categories, Products, Subcategories
from users.models import User

class CartUrlsTest(TestCase):

    def setUp(self):
        self.client = Client()
        self.user = User.objects.create(username='testuser', password='testpassword55@')
        self.category = Categories.objects.create(name="Toys")
        self.subcategory = Subcategories.objects.create(name="Dog Toys", category=self.category)
        self.product = Products.objects.create(name="Bone Toy", price=Decimal("100.00"), discount=Decimal("10.00"), category=self.category, subcategory=self.subcategory)
        self.cart = Cart.objects.create(user=self.user, product=self.product, quantity=1)
        self.client.login(username='testuser', password='testpassword55@')

    def test_cart_add_url(self):
        url = reverse('carts:cart_add')
        response = self.client.post(url, {'product_id': self.product.id})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['success'], True)

    def test_cart_change_url(self):
        url = reverse('carts:cart_change')
        response = self.client.post(url, {'cart_id': self.cart.id, 'quantity': 3})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['success'], True)
        self.cart.refresh_from_db()
        self.assertEqual(self.cart.quantity, 3)

    def test_cart_remove_url(self):
        url = reverse('carts:cart_remove')
        response = self.client.post(url, {'cart_id': self.cart.id})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['success'], True)
        with self.assertRaises(Cart.DoesNotExist):
            Cart.objects.get(id=self.cart.id)