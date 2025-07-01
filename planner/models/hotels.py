from django.db import models
from .base import Location

class Hotel(models.Model):
    name = models.CharField(max_length=100)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    price_per_day = models.PositiveIntegerField()
    def __str__(self): return self.name
