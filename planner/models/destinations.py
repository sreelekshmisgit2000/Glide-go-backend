from django.db import models
from .base import Country, Location  # Assuming these are in base.py


class Destination(models.Model):
    CATEGORY_CHOICES = [
        ('beach', 'Beach'),
        ('mountain', 'Mountain'),
        ('city', 'City'),
        ('historical', 'Historical Site'),
        ('adventure', 'Adventure'),
        ('natural', 'Natural'),
        ('cultural', 'Cultural'),
        ('other', 'Other'),
    ]

    name = models.CharField(max_length=255)
    description = models.TextField()
    country = models.ForeignKey(Country, on_delete=models.SET_NULL, null=True, blank=True)
    location = models.ForeignKey(Location, on_delete=models.SET_NULL, null=True, blank=True)
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES, default='other')
    latitude = models.FloatField(blank=True, null=True)
    longitude = models.FloatField(blank=True, null=True)
    thumbnail = models.ImageField(upload_to='thumbnails/', blank=False, null=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} ({self.category})"


class Place(models.Model):
    destination = models.ForeignKey(Destination, on_delete=models.CASCADE, related_name="places")
    name = models.CharField(max_length=255)
    description = models.TextField()
    latitude = models.FloatField()
    longitude = models.FloatField()
    map_link = models.URLField(max_length=1000)

    def __str__(self):
        return self.name


class PlaceImage(models.Model):
    place = models.ForeignKey(Place, related_name="images", on_delete=models.CASCADE)
    image = models.ImageField(upload_to="places/")
    caption = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return f"Image for {self.place.name}"


class Activity(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    destination = models.ForeignKey(
        Destination, on_delete=models.CASCADE, related_name="activities", null=True, blank=True
    )
    place = models.ForeignKey(
        Place, on_delete=models.CASCADE, related_name="activities", null=True, blank=True
    )
    price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    image = models.ImageField(upload_to="activities/", null=True, blank=True)
    def __str__(self):
        loc = self.destination.name if self.destination else self.place.name
        return f"{self.name} - {loc}"
