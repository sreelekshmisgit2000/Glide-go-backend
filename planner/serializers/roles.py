from rest_framework import serializers
from planner.models import RolePermission

# ────────────────────────── ROLE PERMISSION ──────────────────────────
class RolePermissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = RolePermission
        fields = ['id', 'role', 'allowed_pages']
