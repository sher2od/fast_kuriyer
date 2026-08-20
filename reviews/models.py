from django.db import models
from users.models import User
from orders.models import Order


class Review(models.Model):
    class TargetType(models.TextChoices):
        STORE = "store", "Store"
        COURIER = "courier", "Courier"

    order = models.ForeignKey(
        Order,
        on_delete=models.CASCADE,
        related_name="reviews"
    )

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="reviews"
    )

    target_type = models.CharField(
        max_length=20,
        choices=TargetType.choices
    )

    target_id = models.PositiveIntegerField()

    rating = models.PositiveSmallIntegerField()

    comment = models.TextField(
        blank=True,
        null=True
    )

    def __str__(self):
        return f"{self.user.phone} - {self.rating}"