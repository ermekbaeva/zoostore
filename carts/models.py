from django.db import models

from goods.models import Products
from users.models import User

class CartQuerySet(models.QuerySet):
    def total_price(self):
        return sum(cart.product_price() for cart in self)
    def total_quantity(self):
        if self:
            return sum(cart.quantity for cart in self)
        return 0

class Cart(models.Model):
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)
    product = models.ForeignKey(to=Products, on_delete=models.CASCADE)
    quantity = models.PositiveSmallIntegerField(default=0)
    session_key=models.CharField(max_length=32, null=True, blank=True)
    created_timestamp = models.DateTimeField(auto_now_add=True)
    objects=CartQuerySet().as_manager()

    class Meta:
        db_table = "cart"
        verbose_name = "Cart"
        verbose_name_plural = "Carts"

    def __str__(self):
        return f"Cart {self.user.username} | Item {self.product.name} | Quantity {self.quantity}"

    def product_price(self):
        return round(self.product.sell_price() * self.quantity, 2)
