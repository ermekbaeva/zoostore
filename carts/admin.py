from django.contrib import admin

from carts.models import Cart


@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ["user","product_id", "product", "quantity", "created_timestamp"]
    list_filter=['created_timestamp', 'user','product',]
