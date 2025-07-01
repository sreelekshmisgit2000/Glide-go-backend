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