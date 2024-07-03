from django.contrib import admin
from goods.models import Categories,Products, Subcategories


@admin.register(Categories)
class CategoriesAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    list_display=['name',]

@admin.register(Subcategories)
class SubcategoriesAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}

@admin.register(Products)
class ProductsAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    list_display=['id','name', 'quantity', 'price', 'discount']
    list_editable=['discount',]
    search_fields=['name', 'description']
    hst_filter=['discount', 'quantity', 'category']
    fields=['name', 'category', 'slug', 'description', 'image', ('price', 'discount'), 'quntity']