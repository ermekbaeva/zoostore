from decimal import Decimal
from django.test import TestCase
from django.urls import reverse, resolve
from goods import views
from goods.models import Categories, Products, Subcategories

class GoodsURLsTest(TestCase):
    def setUp(self):
        # Создаем категории и подкатегории
        self.category = Categories.objects.create(name="Dogs", slug="dogs")
        self.subcategory = Subcategories.objects.create(name="Dog Toys", slug="dogs-toys", category=self.category)
        
        # Создаем тестовый продукт
        self.product = Products.objects.create(
            name="Jolly Pets Push-n-Play Dog Toys",
            slug="Jolly-Pets1-Push-n-Play1-Dog-Toys-Blue-Color-X-Large-14-Inch",
            price=Decimal("100.00"),
            category=self.category,
            subcategory=self.subcategory,
            image='null'
        )
        
    def test_search_url_resolves(self):
        url = reverse('goods:search')
        self.assertEqual(resolve(url).func, views.catalog)

    def test_index_url_resolves(self):
        url = reverse('goods:index', kwargs={'subcategory_slug': 'dogs-toys'})
        resolved_view = resolve(url)
        self.assertEqual(resolved_view.func, views.catalog)
        self.assertEqual(resolved_view.kwargs['subcategory_slug'], 'dogs-toys')

    def test_product_url_resolves(self):
        url = reverse('goods:product', kwargs={'product_slug': 'Jolly-Pets1-Push-n-Play1-Dog-Toys-Blue-Color-X-Large-14-Inch'})
        resolved_view = resolve(url)
        self.assertEqual(resolved_view.func, views.product)
        self.assertEqual(resolved_view.kwargs['product_slug'], 'Jolly-Pets1-Push-n-Play1-Dog-Toys-Blue-Color-X-Large-14-Inch')

    def test_search_url_status_code(self):
        url = reverse('goods:search')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_index_url_status_code(self):
        url = reverse('goods:index', kwargs={'subcategory_slug': 'Jolly-Pets1-Push-n-Play1-Dog-Toys-Blue-Color-X-Large-14-Inch'})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_product_url_status_code(self):
        url = reverse('goods:product', kwargs={'product_slug': 'Jolly-Pets1-Push-n-Play1-Dog-Toys-Blue-Color-X-Large-14-Inch'})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)