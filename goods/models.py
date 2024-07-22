from django.db import models
from django.urls import reverse

class Categories(models.Model):
    name=models.CharField(max_length=150, unique=True)
    slug=models.SlugField(max_length=200, unique=True, blank=True, null=True)

    def __str__(self) -> str:
        return self.name

    class Meta:
        db_table='category'
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

class Subcategories(models.Model):
    name=models.CharField(max_length=150)
    slug=models.SlugField(max_length=200, unique=True, blank=True, null=True)
    category = models.ForeignKey(Categories, on_delete=models.PROTECT, null=True, blank=True)

    def __str__(self) -> str:
        return self.name

    class Meta:
        db_table='subcategory'
        verbose_name = 'Subcategory'
        verbose_name_plural = 'Subcategories'


class Products(models.Model):
    name = models.CharField(max_length=150)
    slug = models.SlugField(max_length=200, unique=True, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='products/', null=True)
    price = models.DecimalField(default=0.00, max_digits=7, decimal_places=2)
    quantity=models.PositiveIntegerField(default=0)
    category = models.ForeignKey(Categories, on_delete=models.PROTECT, null=True, blank=True)
    subcategory = models.ForeignKey(Subcategories, on_delete=models.PROTECT, null=True, blank=True)
    discount = models.DecimalField(default=0.00, max_digits=7, decimal_places=2)

    def __str__(self) -> str:
        return self.name

    def display_id(self):
        return f'{self.pk:05}'

    def sell_price(self):
        if self.discount:
            return round(self.price - self.price*self.discount/100, 2)
        return self.price
    
    def get_absolute_url(self):
        return reverse("catalog:product", kwargs={"product_slug": self.slug})

    class Meta:
        db_table='product'
        verbose_name = 'Product'
        verbose_name_plural = 'Products'
        ordering = ("id",)

    
