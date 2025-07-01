from django.db import models

class Country(models.Model):
    name = models.CharField(max_length=100, unique=True)
    class Meta:
        ordering = ["name"]
    def __str__(self): return self.name

class Location(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self): return self.name

class MembersOption(models.Model):
    value = models.PositiveIntegerField()

    def __str__(self):
        return self.value

class ChildrenOption(models.Model):
    value = models.PositiveIntegerField()

    def __str__(self):
        return self.value

class RoomsOption(models.Model):
    value = models.PositiveIntegerField()

    def __str__(self):
        return self.value
    

