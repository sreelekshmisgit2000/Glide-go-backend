from rest_framework import serializers
from planner.models import Vehicle, VehicleImage


# ────────────────────────── VEHICLE IMAGE ──────────────────────────
class VehicleImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = VehicleImage
        fields = ['id', 'vehicle', 'image', 'caption']


class VehicleImageGroupedByVehicleSerializer(serializers.ModelSerializer):
    images = VehicleImageSerializer(many=True, read_only=True)

    class Meta:
        model = Vehicle
        fields = ['id', 'brand', 'model', 'registration_number', 'images']


# ────────────────────────── VEHICLE WRITE ──────────────────────
class VehicleWriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vehicle
        fields = [
            'id', 'brand', 'model', 'registration_number',
            'seating_capacity', 'vehicle_image', 'vehicle_type'
        ]


# ────────────────────────── VEHICLE LIST ───────────────────────
class VehicleListSerializer(serializers.ModelSerializer):
    image_url = serializers.ImageField(source='vehicle_image', read_only=True)

    class Meta:
        model = Vehicle
        fields = [
            'id', 'brand', 'model', 'registration_number',
            'seating_capacity', 'vehicle_type', 'image_url'
        ]


# ───────────────────────── VEHICLE DETAIL ──────────────────────
class VehicleDetailSerializer(serializers.ModelSerializer):
    images = VehicleImageSerializer(many=True, read_only=True)
    image_url = serializers.ImageField(source='vehicle_image', read_only=True)

    class Meta:
        model = Vehicle
        fields = [
            'id', 'brand', 'model', 'registration_number',
            'seating_capacity', 'vehicle_type',
            'vehicle_image', 'image_url',
            'created_at', 'updated_at',
            'images'
        ]
