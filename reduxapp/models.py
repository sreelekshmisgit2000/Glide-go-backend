from django.db import models

class HotelCategory(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def _str_(self):
        return self.name

class RoomType(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def _str_(self):
        return self.name

class DocumentType(models.Model):
    name = models.CharField(max_length=50, unique=True)  # e.g., GST
    description = models.TextField(blank=True)

    def _str_(self):
        return self.name

class ActivityType(models.Model):
    name = models.CharField(max_length=50, unique=True)
    description = models.TextField(blank=True)

    def _str_(self):
        return self.name
    

class Amenity(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def _str_(self):
        return self.name

class Activity(models.Model):
    name = models.CharField(max_length=100)
    activity_type = models.ForeignKey(ActivityType, on_delete=models.SET_NULL, null=True)
    latitude = models.FloatField()
    longitude = models.FloatField()

    def _str_(self):
        return self.name

class Hotel(models.Model):
    name = models.CharField(max_length=255)
    category = models.ForeignKey(HotelCategory, on_delete=models.SET_NULL, null=True)
    room_type = models.ForeignKey(RoomType, on_delete=models.SET_NULL, null=True)
    amenities = models.ManyToManyField(Amenity, blank=True)
    activities = models.ManyToManyField(Activity, blank=True)
    latitude = models.FloatField()
    longitude = models.FloatField()
    is_approved = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def _str_(self):
        return self.name

class HotelDocument(models.Model):
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE, related_name='documents')
    document_type = models.ForeignKey(DocumentType, on_delete=models.SET_NULL, null=True)
    file = models.FileField(upload_to='hotel_documents/')

    def _str_(self):
        return f"{self.hotel.name} - {self.document_type}"

class Driver(models.Model):
    name = models.CharField(max_length=100)
    license_doc = models.FileField(upload_to='driver_docs/')
    id_proof_doc = models.FileField(upload_to='driver_docs/')
    address_proof_doc = models.FileField(upload_to='driver_docs/')

    def _str_(self):
        return self.name

class Cab(models.Model):
    vehicle_number = models.CharField(max_length=50)
    rc_doc = models.FileField(upload_to='cab_docs/')
    permit_doc = models.FileField(upload_to='cab_docs/')
    insurance_doc = models.FileField(upload_to='cab_docs/')
    driver = models.OneToOneField(Driver, on_delete=models.CASCADE, related_name='cab')
    is_verified = models.BooleanField(default=False)

    def _str_(self):
        return self.vehicle_number

class Plan(models.Model):
    plan_id = models.CharField(max_length=100, unique=True)
    theme = models.CharField(max_length=255)
    hotels = models.ManyToManyField(Hotel, blank=True)
    activities = models.ManyToManyField(Activity, blank=True)
    cabs = models.ManyToManyField(Cab, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def _str_(self):
        return self.plan_id