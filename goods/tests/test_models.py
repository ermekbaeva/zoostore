from decimal import Decimal
from django.core.exceptions import ValidationError
from django.test import TestCase
from django.urls import reverse
from goods.models import Products, Categories, Subcategories


class ProductsModelTest(TestCase):
    def setUp(self):
        self.category = Categories.objects.create(name="Toys")
        self.subcategory = Subcategories.objects.create(
            name="Dog Toys", category=self.category
        )
        self.product = Products.objects.create(
            name="Bone Toy",
            price=Decimal("100.00"),
            discount=Decimal("10.00"),
            category=self.category,
            subcategory=self.subcategory,
        )

    def test_sell_price_with_discount(self):
        self.assertEqual(self.product.sell_price(), Decimal("90.00"))

    def test_sell_price_without_discount(self):
        self.product.discount = Decimal("0.00")
        self.assertEqual(self.product.sell_price(), Decimal("100.00"))


class ProductsDisplayIdTest(TestCase):
    def setUp(self):
        self.product = Products.objects.create(name="Bone Toy", price=Decimal("100.00"))

    def test_display_id_format(self):
        self.assertEqual(self.product.display_id(), f"{self.product.pk:05}")


class ProductsGetAbsoluteUrlTest(TestCase):
    def setUp(self):
        self.product = Products.objects.create(
            name="Bone Toy",
            price=Decimal("100.00"),
            slug="bone-toy",
        )

    def test_get_absolute_url(self):
        expected_url = reverse(
            "catalog:product", kwargs={"product_slug": self.product.slug}
        )
        self.assertEqual(self.product.get_absolute_url(), expected_url)


class ProductsStrTest(TestCase):
    def setUp(self):
        self.product = Products.objects.create(name="Bone Toy", price=Decimal("100.00"))

    def test_str_method(self):
        self.assertEqual(str(self.product), "Bone Toy")


class CategoriesModelValidationTest(TestCase):
    def setUp(self):
        self.category1 = Categories.objects.create(name="Toys", slug="toys")

    def test_slug_uniqueness(self):
        # Создаем вторую категорию с тем же slug
        category2 = Categories(name="Games", slug="toys")
        # Ожидаем, что произойдет ValidationError из-за уникальности slug
        with self.assertRaises(ValidationError):
            category2.full_clean()

    def test_name_max_length(self):
        # Превышаем максимальную длину имени
        category = Categories(name="x" * 151)  # Длина имени 151 символ
        # Ожидаем ValidationError из-за превышения максимальной длины
        with self.assertRaises(ValidationError):
            category.full_clean()

class ProductsModelValidationTest(TestCase):
    def setUp(self):
        self.category = Categories.objects.create(name="Toys")
    
    def test_quantity_positive(self):
        # Создаем продукт с отрицательным значением quantity
        product = Products(
            name="Bone Toy",
            price=Decimal("10.00"),
            quantity=-1,  # Некорректное значение
            category=self.category
        )
        # Ожидаем ValidationError из-за отрицательного значения
        with self.assertRaises(ValidationError):
            product.full_clean()

    def test_price_decimal_places(self):
        # Создаем продукт с более чем двумя знаками после запятой в цене
        product = Products(
            name="Bone Toy",
            price=Decimal("10.123"),  # Некорректное значение
            quantity=1,
            category=self.category
        )
        # Ожидаем ValidationError из-за некорректного числа знаков после запятой
        with self.assertRaises(ValidationError):
            product.full_clean()

class ProductsModelRequiredFieldsTest(TestCase):
    def setUp(self):
        self.category = Categories.objects.create(name="Toys")

    def test_name_required(self):
        product = Products(
            name=None,  # None для обязательного поля
            price=Decimal("10.00"),
            quantity=1,
            category=self.category
        )
        # Ожидаем ValidationError из-за отсутствия имени
        with self.assertRaises(ValidationError):
            product.full_clean()

    def test_price_required(self):
        product = Products(
            name="Bone Toy",
            price=None,  # None для обязательного поля
            quantity=1,
            category=self.category
        )
        # Ожидаем ValidationError из-за отсутствия цены
        with self.assertRaises(ValidationError):
            product.full_clean()