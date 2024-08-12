from django.db import models

from goods.models import Products
from users.models import User


class OrderitemQuerySet(models.QuerySet):
    def total_price(self):
        return sum(cart.products_price() for cart in self)

    def total_quantity(self):
        if self:
            return sum(cart.quantity for cart in self)
        return 0


class Order(models.Model):
    user = models.ForeignKey(
        to=User, on_delete=models.SET_DEFAULT, blank=True, null=True, default=None
    )
    created_timestamp = models.DateTimeField(
        auto_now_add=True, verbose_name="Order creation date"
    )
    phone_number = models.CharField(max_length=20, verbose_name="Phone number")
    requires_delivery = models.BooleanField(
        default=False, verbose_name="Delivery required"
    )
    delivery_address = models.TextField(
        null=True, blank=True, verbose_name="Delivery address"
    )
    payment_on_get = models.BooleanField(default=False, verbose_name="Payment on get")
    is_paid = models.BooleanField(default=False, verbose_name="Paid")
    status = models.CharField(
        max_length=50, default="In process", verbose_name="Order status"
    )

    class Meta:
        db_table = "order"
        verbose_name = "Order"
        verbose_name_plural = "Orders"

    def __str__(self):
        return f"Order #{self.pk} | Client {self.user.first_name} {self.user.last_name}"


class OrderItem(models.Model):
    order = models.ForeignKey(
        to=Order, verbose_name=("Order"), on_delete=models.CASCADE
    )
    product = models.ForeignKey(
        Products,
        on_delete=models.SET_DEFAULT,
        null=True,
        verbose_name="Product",
        default=True,
    )
    name = models.CharField(max_length=150, verbose_name="Name")
    price = models.DecimalField(max_digits=7, decimal_places=2, verbose_name="Price")
    quantity = models.PositiveIntegerField(default=0, verbose_name="Quantity")
    created_timestamp = models.DateTimeField(
        auto_now_add=True, verbose_name="Created date"
    )

    class Meta:
        db_table = "order_item"
        verbose_name = "Selled item"
        verbose_name_plural = "Selled items"

    objects = OrderitemQuerySet.as_manager()

    def products_price(self):
        return round(self.product.sell_price() * self.quantity, 2)

    def __str__(self):
        return f"Item {self.name} | Order #{self.order.pk}"
