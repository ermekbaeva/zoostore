from django.test import TestCase
from django.urls import reverse
from orders.models import Order
from users.models import User
from goods.models import Products
from carts.models import Cart

class AddToCartAndCheckoutTest(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='Testpassword123', first_name='Meerim', last_name='Ermekbaeva')
        self.product = Products.objects.create(name='Test Product', price=100, quantity=5)

    def test_add_to_cart_and_checkout(self):
        self.client.login(username='testuser', password='Testpassword123')

        response = self.client.post(reverse('carts:cart_add'), {
            'product_id': self.product.id,
            'quantity': 1
        })
        self.assertEqual(response.status_code, 200)

        cart = Cart.objects.get(user=self.user)
        self.assertEqual(cart.quantity, 1)
        self.assertEqual(cart.product, self.product)

        response = self.client.post(reverse('orders:create_order'), {
            'first_name': 'Meerim',
            'last_name': 'Ermekbaeva',
            'phone_number': '+996550233095',
            'requires_delivery': "0",
            'delivery_address': 'Test Address',
            'payment_on_get': "0", 
        })

        self.assertEqual(response.status_code, 302)

        self.assertFalse(Cart.objects.filter(user=self.user).exists())
        self.assertTrue(Order.objects.filter(user=self.user).exists())