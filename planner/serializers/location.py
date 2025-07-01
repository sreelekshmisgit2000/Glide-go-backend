from rest_framework import serializers
from planner.models import Location

# ────────────────────────── WRITE ──────────────────────────
class LocationWriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = ['id', 'name']


# ────────────────────────── LIST ──────────────────────────
class LocationListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = ['id', 'name']


# ────────────────────────── DETAIL ──────────────────────────
class LocationDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        depth = 0
        fields = ['id', 'name']
