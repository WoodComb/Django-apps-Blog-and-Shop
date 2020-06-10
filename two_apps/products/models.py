from django.db import models
from django.utils import timezone
# Create your models here.
class Products(models.Model):
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)
    price = models.FloatField()
    weight = models.FloatField()

    def __str__(self):
        return self.name
