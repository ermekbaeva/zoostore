from django.test import TestCase, Client
from django.urls import reverse
from django.http import JsonResponse
from decimal import Decimal
from carts.models import Cart
from goods.models import Products, Categories, Subcategories
from users.models import User

class CartViewsTest(TestCase):

    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='testuser', password='testpassword55@')
        self.category = Categories.objects.create(name="Toys")
        self.subcategory = Subcategories.objects.create(name="Dog Toys", category=self.category)
        self.product = Products.objects.create(name="Bone Toy", price=Decimal("100.00"), discount=Decimal("10.00"), category=self.category, subcategory=self.subcategory)
        self.cart = Cart.objects.create(user=self.user, product=self.product, quantity=1)
        self.client.login(username='testuser', password='testpassword55@')

    def test_cart_add_authenticated_user(self):
        url = reverse('carts:cart_add')
        response = self.client.post(url, {'product_id': self.product.id})
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertEqual(data['success'], True)
        self.assertEqual(data['message'], "Item was added to cart")
        self.assertEqual(Cart.objects.filter(user=self.user).count(), 1)
        cart = Cart.objects.get(user=self.user, product=self.product)
        self.assertEqual(cart.quantity, 2)

    def test_cart_add_anonymous_user(self):
        self.client.logout()
        url = reverse('carts:cart_add')
        response = self.client.post(url, {'product_id': self.product.id})
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertEqual(data['success'], True)
        self.assertEqual(data['message'], "Item was added to cart")
        self.assertEqual(Cart.objects.filter(session_key=self.client.session.session_key).count(), 1)
        cart = Cart.objects.get(session_key=self.client.session.session_key, product=self.product)
        self.assertEqual(cart.quantity, 1)

    def test_cart_change_authenticated_user(self):
        url = reverse('carts:cart_change')
        response = self.client.post(url, {'cart_id': self.cart.id, 'quantity': 3})
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertEqual(data['success'], True)
        self.assertEqual(data['message'], "Quantity was changed")
        self.cart.refresh_from_db()
        self.assertEqual(self.cart.quantity, 3)

    def test_cart_remove_authenticated_user(self):
        url = reverse('carts:cart_remove')
        response = self.client.post(url, {'cart_id': self.cart.id})
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertEqual(data['success'], True)
        self.assertEqual(data['message'], "Item was removed")
        with self.assertRaises(Cart.DoesNotExist):
            Cart.objects.get(id=self.cart.id)

    def test_cart_add_invalid_product(self):
        url = reverse('carts:cart_add')
        response = self.client.post(url, {'product_id': 999})
        self.assertEqual(response.status_code, 404) 

    def test_cart_change_invalid_cart_id(self):
        url = reverse('carts:cart_change')
        response = self.client.post(url, {'cart_id': 999, 'quantity': 3})
        self.assertEqual(response.status_code, 404) 

    def test_cart_remove_invalid_cart_id(self):
        url = reverse('carts:cart_remove')
        response = self.client.post(url, {'cart_id': 999})
        self.assertEqual(response.status_code, 404)