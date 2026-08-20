from django.db import models
from users.models import User, Address
from stores.models import Store


class Order(models.Model):

    class Status(models.TextChoices):
        CREATED = "created", "Created"
        CONFIRMED = "confirmed", "Confirmed"
        PREPARING = "preparing", "Preparing"
        COURIER_ASSIGNED = "courier_assigned", "Courier Assigned"
        ON_THE_WAY = "on_the_way", "On The Way"
        DELIVERED = "delivered", "Delivered"
        CANCELLED = "cancelled", "Cancelled"

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="orders"
    )

    store = models.ForeignKey(
        Store,
        on_delete=models.CASCADE,
        related_name="orders"
    )

    address = models.ForeignKey(
        Address,
        on_delete=models.SET_NULL,
        null=True,
        related_name="orders"
    )

    status = models.CharField(
        max_length=30,
        choices=Status.choices,
        default=Status.CREATED
    )

    total_price = models.DecimalField(
        max_digits=12,
        decimal_places=2
    )

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Order #{self.id}"


class OrderItem(models.Model):

    order = models.ForeignKey(
        Order,
        on_delete=models.CASCADE,
        related_name="items"
    )

    product = models.ForeignKey(
        "catalog.Product",
        on_delete=models.CASCADE,
        related_name="order_items"
    )

    quantity = models.PositiveIntegerField(default=1)

    price_at_order = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )

    def __str__(self):
        return f"{self.product.name} x {self.quantity}"


class OrderStatusHistory(models.Model):

    order = models.ForeignKey(
        Order,
        on_delete=models.CASCADE,
        related_name="status_history"
    )

    status = models.CharField(max_length=30)

    changed_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Order #{self.order.id} - {self.status}"