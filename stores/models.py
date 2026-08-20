from django.db import models
from django.contrib.auth.models import AbstractUser

class Store(models.Model):
    name = models.CharField(max_length=255)
    
    latitude = models.DecimalField(max_digits=9, decimal_places=6)
    longitude = models.DecimalField(max_digits=9, decimal_places=6)

    working_hours = models.CharField(max_length=255)

    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name

