from django.db import models
from users.models import User

class Courier(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name = 'courier'
    )

    current_latitude = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)
    current_longitude = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)

    is_available = models.BooleanField(default=True)
    vehicle_type = models.CharField(max_length=50)

    def __str__(self):
        return self.user.phone
