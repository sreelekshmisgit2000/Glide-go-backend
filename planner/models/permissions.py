from django.db import models


class Page(models.Model):
    """
    Represents a logical frontend/React page or section.
    - `code`: Used as a unique identifier for permission logic and frontend routing.
    - `name`: Human-readable name for UI/admin.
    """
    code = models.CharField(max_length=50, unique=True)  # e.g., 'dashboard', 'destinations'
    name = models.CharField(max_length=100)              # e.g., 'Dashboard', 'Destinations'

    class Meta:
        verbose_name = "CRM Page"
        verbose_name_plural = "CRM Pages"
        ordering = ['code']

    def __str__(self):
        return self.name


class RolePermission(models.Model):
    """
    Maps a predefined user role to allowed pages.
    Use this to enforce access control per role.
    - `role`: superuser, staff, user, etc.
    - `allowed_pages`: list of allowed page `code`s.
    """
    ROLE_CHOICES = [
        ('superuser', 'Superuser'),
        ('staff', 'Staff'),
        ('user', 'User'),
    ]

    role = models.CharField(max_length=20, choices=ROLE_CHOICES, unique=True)
    allowed_pages = models.JSONField(default=list)  # Stores page codes: ["dashboard", "hotels"]

    def __str__(self):
        return self.role
