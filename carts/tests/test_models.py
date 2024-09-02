from decimal import Decimal
from django.test import TestCase

from carts.models import Cart
from goods.models import Categories, Products, Subcategories
from users.models import User

class CartsModelsTest(TestCase):
    def setUp(self):
        self.user = User.objects.create(username="Meerim")
        self.category = Categories.objects.create(name="Toys")
        self.subcategory = Subcategories.objects.create(name="Dog Toys", category=self.category)
        self.product = Products.objects.create(name="Bone Toy", price=Decimal("100.00"), discount=Decimal("10.00"), category=self.category, subcategory=self.subcategory)
        self.product2 = Products.objects.create(name="Ball Toy", price=Decimal("50.00"), discount=Decimal("0.00"), category=self.category, subcategory=self.subcategory)

        self.cart = Cart.objects.create(user=self.user, product=self.product, quantity=2)
        self.cart2 = Cart.objects.create(user=self.user, product=self.product2, quantity=5)


    def test_total_quantity(self):
        self.assertEqual(Cart.objects.total_quantity(), 7)
    
    def test_total_price(self):
        self.assertEqual(Cart.objects.total_price(), Decimal("430.00"))

    def test_products_price(self):
        self.assertEqual(self.cart.products_price(), Decimal("180.00"))
        self.assertEqual(self.cart2.products_price(), Decimal("250.00"))

class ProductsStrTest(TestCase):
    def setUp(self):
        self.user = User.objects.create(username="Meerim")
        self.category = Categories.objects.create(name="Toys")
        self.subcategory = Subcategories.objects.create(name="Dog Toys", category=self.category)
        self.product = Products.objects.create(name="Bone Toy", price=Decimal("100.00"), discount=Decimal("10.00"), category=self.category, subcategory=self.subcategory)
        self.product2 = Products.objects.create(name="Ball Toy", price=Decimal("50.00"), discount=Decimal("0.00"), category=self.category, subcategory=self.subcategory)

        self.cart = Cart.objects.create(user=self.user, product=self.product, quantity=2)
        self.cart2 = Cart.objects.create(user=self.user, product=self.product2, quantity=5)
        self.cart_anonimous = Cart.objects.create(product=self.product2, quantity=5)

    def test_str_method(self):
        self.assertEqual(str(self.cart), "Cart Meerim | Item Bone Toy | Quantity 2")
        self.assertEqual(str(self.cart2), "Cart Meerim | Item Ball Toy | Quantity 5")
        self.assertEqual(str(self.cart_anonimous), "Anonimous cart | Item Ball Toy | Quantity 5")
