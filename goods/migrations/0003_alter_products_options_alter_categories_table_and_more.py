# Generated by Django 4.2.10 on 2024-05-31 14:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('goods', '0002_products_discount'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='products',
            options={'ordering': ('id',), 'verbose_name': 'Product', 'verbose_name_plural': 'Products'},
        ),
        migrations.AlterModelTable(
            name='categories',
            table='category',
        ),
        migrations.AlterModelTable(
            name='products',
            table='product',
        ),
        migrations.AlterModelTable(
            name='subcategories',
            table='subcategory',
        ),
    ]