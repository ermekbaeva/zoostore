from decimal import Decimal
from django.db import models

from goods.models import Products
from users.models import User

class CartQueryset(models.QuerySet):
    def total_price(self):
        return sum(cart.products_price() for cart in self)
    def total_quantity(self):
        if self:
            return sum(cart.quantity for cart in self)
        return 0

class Cart(models.Model):
    user = models.ForeignKey(to=User, null=True, blank=True, on_delete=models.CASCADE)
    product = models.ForeignKey(to=Products, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=0)
    session_key=models.CharField(max_length=32, null=True, blank=True)
    created_timestamp = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        db_table = "cart"
        verbose_name = "Cart"
        verbose_name_plural = "Carts"
        ordering = ("id",)
    
    objects=CartQueryset().as_manager()

    def __str__(self):
        if self.user:
            return f"Cart {self.user.username} | Item {self.product.name} | Quantity {self.quantity}" 
        return f"Anonimous cart | Item {self.product.name} | Quantity {self.quantity}"

    def products_price(self):
        return round(self.product.sell_price() * Decimal(self.quantity), 2)
