from django.db import models
from .base import Location

class CabCategory(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(default='Default description')
    def __str__(self): return self.name

class Vehicle(models.Model):
    VEHICLE_TYPE_CHOICES = [('car', 'Car'), ('van', 'Van'), ('suv', 'SUV'), ('bike', 'Bike')]
    brand = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    registration_number = models.CharField(max_length=50, unique=True)
    seating_capacity = models.PositiveIntegerField()
    vehicle_image = models.ImageField(upload_to='vehicles/', blank=True, null=True)
    vehicle_type = models.CharField(max_length=20, choices=VEHICLE_TYPE_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self): return f"{self.brand} {self.model} ({self.registration_number})"

class VehicleImage(models.Model):
    vehicle = models.ForeignKey(Vehicle, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='vehicles/gallery/')
    caption = models.CharField(max_length=255, blank=True)

class Driver(models.Model):
    name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=15)
    email = models.EmailField(unique=True)
    license_number = models.CharField(max_length=100, unique=True)
    address = models.TextField()
    profile_image = models.ImageField(upload_to='drivers/', blank=True, null=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self): return self.name

class DriverImage(models.Model):
    driver = models.ForeignKey(Driver, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='drivers/gallery/')
    caption = models.CharField(max_length=255, blank=True)

class CabType(models.Model):
    name = models.CharField(max_length=100)
    price = models.PositiveIntegerField()
    def __str__(self): return self.name

class Cab(models.Model):
    name = models.CharField(max_length=100)
    category = models.ForeignKey(CabCategory, on_delete=models.SET_NULL, null=True, related_name='cabs')
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE)
    driver = models.ForeignKey(Driver, on_delete=models.SET_NULL, null=True)
    is_available = models.BooleanField(default=True)
    price_per_km = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self): return f"{self.name} ({self.vehicle.brand})"
