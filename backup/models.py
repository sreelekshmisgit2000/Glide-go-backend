# planner/models.py
from django.db import models
from django_countries.fields import CountryField
from geopy.geocoders import Nominatim


class Country(models.Model):
    name = models.CharField(max_length=100, unique=True)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name

class Location(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Hotel(models.Model):
    name = models.CharField(max_length=100)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    price_per_day = models.PositiveIntegerField()

    def __str__(self):
        return self.name

class CabType(models.Model):
    name = models.CharField(max_length=100)
    price = models.PositiveIntegerField()

    def __str__(self):
        return self.name


class DaysOption(models.Model):
    value = models.PositiveIntegerField()

    def __str__(self):
        return self.value





class CabCategory(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(null=False, default='Default description')
    
    def __str__(self):
        return self.name

# Vehicle model
class Vehicle(models.Model):
    VEHICLE_TYPE_CHOICES = [
        ('car', 'Car'),
        ('van', 'Van'),
        ('suv', 'SUV'),
        ('bike', 'Bike'),
    ]

    brand = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    registration_number = models.CharField(max_length=50, unique=True)
    seating_capacity = models.PositiveIntegerField()
    vehicle_image = models.ImageField(upload_to='vehicles/', blank=True, null=True)
    vehicle_type = models.CharField(max_length=20, choices=VEHICLE_TYPE_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.brand} {self.model} ({self.registration_number})"

# Vehicle Image model (inline to Vehicle)
class VehicleImage(models.Model):
    vehicle = models.ForeignKey(Vehicle, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='vehicles/gallery/')
    caption = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return f"Image for {self.vehicle.brand}"

# Driver model
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

    def __str__(self):
        return self.name



# Cab model
class Cab(models.Model):
    name = models.CharField(max_length=100)
    category = models.ForeignKey(CabCategory, on_delete=models.SET_NULL, null=True,related_name='cabs')
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE)
    driver = models.ForeignKey(Driver, on_delete=models.SET_NULL, null=True)
    is_available = models.BooleanField(default=True)
    price_per_km = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField(blank=True,null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Cab - {self.vehicle.brand} with Driver - {self.driver.name}"
    


# ===========================================================================

class Destination(models.Model):
    CATEGORY_CHOICES = [
        ('beach', 'Beach'),
        ('mountain', 'Mountain'),
        ('city', 'City'),
        ('historical', 'Historical Site'),
        ('adventure', 'Adventure'),
        ('natural','Natural'),
        ('cultural','Cultural'),
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
        return f"{self.name} - {self.destination.name if self.destination else self.place.name}"
    

    


# =================================

from django.conf import settings
from django.db import models





class TripRequest(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,  # <-- lazy reference to custom user
        on_delete=models.CASCADE
    )
    start_date  = models.DateField()
    end_date    = models.DateField()
    days        = models.PositiveIntegerField()
    budget_min  = models.PositiveIntegerField()
    budget_max  = models.PositiveIntegerField()
    adults      = models.PositiveIntegerField()
    children    = models.PositiveIntegerField()
    infants     = models.PositiveIntegerField()
    created_at  = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.start_date}→{self.end_date} | ₹{self.budget_min}-{self.budget_max}"


# planner/models.py

from django.db import models


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

from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404

from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status



class UserPageUpdate(APIView):

    def put(self, request, pk):
        user = get_object_or_404(get_user_model(), pk=pk)
        serializer = UserPageSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user.pages.set(serializer.validated_data["page_ids"])
        return Response(status=204)
    
# planner/models.py   (put it in the same app where you keep other core models)

from django.conf import settings
from django.db import models


class Page(models.Model):
    """
    Represents a logical React/DRF section.
    • `code`  – machine-friendly key used in React (pageCode) and permissions.
    • `name`  – human label shown in Django admin or any UI.
    • `users` – which individual users may open the page.
    """
    code = models.CharField(max_length=50, unique=True)   # e.g. 'destinations'
    name = models.CharField(max_length=100)               # e.g. 'Destinations'

  
    class Meta:
        verbose_name = "CRM Page"
        verbose_name_plural = "CRM Pages"
        ordering = ['code']

    def __str__(self):
        return self.name


# models.py
from django.db import models

class RolePermission(models.Model):
    ROLE_CHOICES = [
        ('superuser', 'Superuser'),
        ('staff', 'Staff'),
        ('user', 'User'),
    ]

    role = models.CharField(max_length=20, choices=ROLE_CHOICES, unique=True)
    allowed_pages = models.JSONField(default=list)  # store as ["dashboard", "hotels", ...]

    def __str__(self):
        return self.role


class BudgetRange(models.Model):
    min_price = models.IntegerField()
    max_price = models.IntegerField()

    def __str__(self):
        return f"{self.min_price} - {self.max_price}"


class DriverImage(models.Model):
    driver = models.ForeignKey('Driver', related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='drivers/gallery/')
    caption = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return f"Image for {self.driver.name}"


    

