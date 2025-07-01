from rest_framework import serializers
from planner.models import Driver

# ────────────────────────── WRITE ──────────────────────────
class DriverWriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Driver
        fields = [
            'id', 'name', 'phone_number', 'email',
            'license_number', 'address',
            'profile_image', 'is_active'
        ]


# ────────────────────────── LIST ──────────────────────────
class DriverListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Driver
        fields = [
            'id', 'name', 'phone_number',
            'email', 'is_active'
        ]


# ────────────────────────── DETAIL ──────────────────────────
class DriverDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Driver
        depth = 0
        fields = [
            'id', 'name', 'phone_number', 'email',
            'license_number', 'address',
            'profile_image', 'is_active',
            'created_at', 'updated_at'
        ]
