from django.test import TestCase, Client
from django.urls import reverse
from goods.models import Products, Categories, Subcategories
from decimal import Decimal

class CatalogViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.category = Categories.objects.create(name="Toys", slug="toys")
        self.subcategory = Subcategories.objects.create(name="Dog Toys", slug="dog-toys", category=self.category)
        self.product1 = Products.objects.create(
            name="Bone Toy",
            price=Decimal("100.00"),
            slug="bone-toy",
            subcategory=self.subcategory,
            image="null",
        )
        self.product2 = Products.objects.create(
            name="Ball Toy",
            price=Decimal("150.00"),
            slug="ball-toy",
            subcategory=self.subcategory,
            image="null",
        )

    def test_catalog_view_with_subcategory(self):
        response = self.client.get(reverse('goods:index', args=['dog-toys']))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'goods/catalog.html')
        self.assertIn(self.product1, response.context['goods'])
        self.assertIn(self.product2, response.context['goods'])

    def test_catalog_view_with_all_subcategories(self):
        response = self.client.get(reverse('goods:index', args=['all']))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'goods/catalog.html')
        self.assertIn(self.product1, response.context['goods'])
        self.assertIn(self.product2, response.context['goods'])

    def test_catalog_view_with_search_query(self):
        response = self.client.get(reverse('goods:index', args=['dog-toys']) + '?q=Bone')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'goods/catalog.html')
        self.assertIn(self.product1, response.context['goods'])
        self.assertNotIn(self.product2, response.context['goods'])

    def test_catalog_view_with_price_range(self):
        response = self.client.get(reverse('goods:index', args=['dog-toys']) + '?min_price=120&max_price=200')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'goods/catalog.html')
        self.assertNotIn(self.product1, response.context['goods'])
        self.assertIn(self.product2, response.context['goods'])

    def test_catalog_view_with_ordering(self):
        response = self.client.get(reverse('goods:index', args=['dog-toys']) + '?order_by=price')
        self.assertEqual(response.status_code, 200)
        goods = response.context['goods'].object_list
        self.assertEqual(goods[0], self.product1)
        self.assertEqual(goods[1], self.product2)

class ProductViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.category = Categories.objects.create(name="Toys", slug="toys")
        self.subcategory = Subcategories.objects.create(name="Dog Toys", slug="dog-toys", category=self.category)
        self.product = Products.objects.create(
            name="Bone Toy",
            price=Decimal("100.00"),
            slug="bone-toy",
            subcategory=self.subcategory,
            image="null"
        )

    def test_product_view(self):
        response = self.client.get(reverse('goods:product', args=['bone-toy']))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'goods/product.html')
        self.assertEqual(response.context['product'], self.product)