from rest_framework import serializers
from planner.models import TripPlan

# ────────────────────────── TRIP PLAN ──────────────────────────
class TripPlanSerializer(serializers.ModelSerializer):
    start_location_name = serializers.CharField(source='start_location.name', read_only=True)
    end_location_name = serializers.CharField(source='end_location.name', read_only=True)

    class Meta:
        model = TripPlan
        fields = [
            'id',
            'name',
            'description',
            'start_location',
            'start_location_name',
            'end_location',
            'end_location_name',
            'hotel',
            'cab_type',
            'days',
            'base_price',
        ]
