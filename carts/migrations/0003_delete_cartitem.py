# Generated by Django 4.2.10 on 2024-07-13 16:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('carts', '0002_alter_cart_quantity_cartitem'),
    ]

    operations = [
        migrations.DeleteModel(
            name='CartItem',
        ),
    ]