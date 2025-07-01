from rest_framework import serializers
from planner.models import DriverImage, Driver

# ────────────────────────── DRIVER IMAGE ──────────────────────────
class DriverImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = DriverImage
        fields = ['id', 'driver', 'image', 'caption']


# ─────── GROUPED: Return images grouped by driver (read-only use) ───────
class DriverImageGroupedSerializer(serializers.ModelSerializer):
    images = DriverImageSerializer(many=True, read_only=True)

    class Meta:
        model = Driver
        fields = ['id', 'name', 'images']
