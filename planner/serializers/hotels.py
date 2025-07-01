from rest_framework import serializers
from planner.models import Hotel

# ────────────────────────── WRITE ──────────────────────────
class HotelWriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hotel
        fields = ['id', 'name', 'location', 'price_per_day']


# ────────────────────────── LIST ──────────────────────────
class HotelListSerializer(serializers.ModelSerializer):
    location_name = serializers.CharField(source='location.name', read_only=True)

    class Meta:
        model = Hotel
        fields = ['id', 'name', 'location', 'location_name', 'price_per_day']


# ────────────────────────── DETAIL ──────────────────────────
class HotelDetailSerializer(serializers.ModelSerializer):
    location_name = serializers.CharField(source='location.name', read_only=True)

    class Meta:
        model = Hotel
        depth = 0
        fields = ['id', 'name', 'location', 'location_name', 'price_per_day']
