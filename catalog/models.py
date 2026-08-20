from django.db import models
from stores.models import Store


class Category(models.Model):
    name = models.CharField(max_length=100)

    parent = models.ForeignKey(
        "self",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="subcategories"
    )

    def __str__(self):
        return self.name


class Product(models.Model):
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name="products"
    )

    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    discount_price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        null=True,
        blank=True
    )
    unit = models.CharField(max_length=20)
    image_url = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.name


class ProductStock(models.Model):
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        related_name="stocks"
    )

    store = models.ForeignKey(
        Store,
        on_delete=models.CASCADE,
        related_name="product_stocks"
    )

    quantity = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"{self.product.name} - {self.store.name}"