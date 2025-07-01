from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Permission

User = get_user_model()


class CustomUserAdmin(admin.ModelAdmin):
    list_display = ("username", "email", "first_name", "last_name", "is_staff", "is_superuser")
    search_fields = ("username", "email", "first_name", "last_name")
    list_filter = ("is_staff", "is_superuser", "is_active")
    ordering = ("username",)
    filter_horizontal = ("user_permissions", "groups")  # adds multi-select boxes
    fieldsets = (
        (None, {
            "fields": ("username", "password")
        }),
        ("Personal info", {
            "fields": ("first_name", "last_name", "email")
        }),
        ("Permissions", {
            "fields": ("is_active", "is_staff", "is_superuser", "groups", "user_permissions")
        }),
        ("Important dates", {
            "fields": ("last_login", "date_joined")
        }),
    )

@admin.register(Permission)
class PermissionAdmin(admin.ModelAdmin):
    list_display = ("name", "codename", "content_type")
    list_filter = ("content_type",)
    search_fields = ("name", "codename")
