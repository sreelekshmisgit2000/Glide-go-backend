from django.db import models
from django.conf import settings
from .base import Location
from .hotels import Hotel
from .cabs import CabType


class TripRequest(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )
    start_date = models.DateField()
    end_date = models.DateField()
    days = models.PositiveIntegerField()
    budget_min = models.PositiveIntegerField()
    budget_max = models.PositiveIntegerField()
    adults = models.PositiveIntegerField()
    children = models.PositiveIntegerField()
    infants = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.start_date}→{self.end_date} | ₹{self.budget_min}-{self.budget_max}"


class TripPlan(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    start_location = models.ForeignKey(Location, on_delete=models.CASCADE, related_name='trip_starts')
    end_location = models.ForeignKey(Location, on_delete=models.CASCADE, related_name='trip_ends')
    hotel = models.ForeignKey(Hotel, on_delete=models.SET_NULL, null=True, blank=True)
    cab_type = models.ForeignKey(CabType, on_delete=models.SET_NULL, null=True, blank=True)
    days = models.PositiveIntegerField()
    base_price = models.DecimalField(max_digits=10, decimal_places=2)

    def total_amount(self):
        hotel_price = self.hotel.price_per_day * self.days if self.hotel else 0
        cab_price = self.cab_type.price * self.days if self.cab_type else 0
        return float(hotel_price + cab_price)

    def __str__(self):
        return f"{self.name} ({self.start_location.name} → {self.end_location.name})"
