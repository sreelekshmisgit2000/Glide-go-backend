from rest_framework import serializers
from planner.models import Cab

# ────────────────────────── WRITE ──────────────────────────
class CabWriteSerializer(serializers.ModelSerializer):
    """Used for create & update (POST/PUT/PATCH)."""
    class Meta:
        model = Cab
        fields = [
            'id', 'name', 'category', 'vehicle', 'driver',
            'price_per_km', 'description', 'is_available'
        ]


# ────────────────────────── LIST ──────────────────────────
class CabListSerializer(serializers.ModelSerializer):
    category_name = serializers.CharField(source='category.name', read_only=True)
    vehicle_model = serializers.CharField(source='vehicle.model', read_only=True)
    driver_name   = serializers.CharField(source='driver.name', read_only=True)

    class Meta:
        model = Cab
        fields = [
            'id', 'name', 'category_name', 'vehicle_model',
            'driver_name', 'price_per_km', 'is_available', 'description'
        ]


# ────────────────────────── DETAIL ──────────────────────────
class CabDetailSerializer(serializers.ModelSerializer):
    category_name = serializers.CharField(source='category.name', read_only=True)
    vehicle_model = serializers.CharField(source='vehicle.model', read_only=True)
    driver_name   = serializers.CharField(source='driver.name', read_only=True)

    class Meta:
        model = Cab
        depth = 0
        fields = [
            'id', 'name', 'category', 'vehicle', 'driver',
            'price_per_km', 'description', 'is_available',
            'created_at', 'updated_at',
            'category_name', 'vehicle_model', 'driver_name'
        ]
