# Generated by Django 4.2.10 on 2024-04-20 13:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('goods', '0002_alter_products_options_alter_subcategories_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='name',
            field=models.CharField(max_length=150),
        ),
        migrations.AlterField(
            model_name='subcategories',
            name='name',
            field=models.CharField(max_length=150),
        ),
    ]
