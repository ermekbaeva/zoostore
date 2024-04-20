from django.db import models

class Categories(models.Model):
    name=models.CharField(max_length=150, unique=True)
    slug=models.SlugField(max_length=200, unique=True, blank=True, null=True)

    def __str__(self) -> str:
        return self.name

    class Meta:
        db_table='Category'
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

class Subcategories(models.Model):
    name=models.CharField(max_length=150)
    slug=models.SlugField(max_length=200, unique=True, blank=True, null=True)
    category = models.ForeignKey(Categories, on_delete=models.PROTECT, null=True, blank=True,db_index=True)

    def __str__(self) -> str:
        return self.name

    class Meta:
        db_table='Subcategory'
        verbose_name = 'Subcategory'
        verbose_name_plural = 'Subcategories'


class Products(models.Model):
    name = models.CharField(max_length=150)
    slug = models.SlugField(max_length=200, unique=True, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='goods_images', blank=True, null=True)
    price = models.DecimalField(default=0.00, max_digits=7, decimal_places=2)
    quantity=models.PositiveIntegerField(default=0)
    category = models.ForeignKey(Categories, on_delete=models.PROTECT, null=True, blank=True,db_index=True)
    subcategory = models.ForeignKey(Subcategories, on_delete=models.PROTECT, null=True, blank=True,db_index=True)

    def __str__(self) -> str:
        return self.name

    class Meta:
        db_table='Product'
        verbose_name = 'Product'
        verbose_name_plural = 'Products'

    
