from rest_framework import serializers
from planner.models import Activity

# ────────────────────────── WRITE ──────────────────────────
class ActivityWriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Activity
        fields = [
            "id",
            "name",
            "description",
            "destination",  # nullable FK
            "place",        # nullable FK
            "price",
            "image",
        ]

    def validate(self, data):
        if not data.get("destination") and not data.get("place"):
            raise serializers.ValidationError("Either destination or place must be set.")
        return data


# ────────────────────────── LIST ──────────────────────────
class ActivityListSerializer(serializers.ModelSerializer):
    destination_name = serializers.CharField(source="destination.name", read_only=True)
    place_name = serializers.CharField(source="place.name", read_only=True)
    image_url = serializers.ImageField(source="image", read_only=True)

    class Meta:
        model = Activity
        fields = [
            "id",
            "name",
            "description",
            "destination_name",
            "place_name",
            "price",
            "image_url",
        ]


# ────────────────────────── DETAIL ──────────────────────────
class ActivityDetailSerializer(serializers.ModelSerializer):
    destination_name = serializers.CharField(source="destination.name", read_only=True)
    place_name = serializers.CharField(source="place.name", read_only=True)
    image_url = serializers.ImageField(source="image", read_only=True)

    class Meta:
        model = Activity
        depth = 0
        fields = [
            "id",
            "name",
            "description",
            "destination",
            "destination_name",
            "place",
            "place_name",
            "price",
            "image",
            "image_url",
        ]


# ────────────────────────── SHARED ──────────────────────────
class ActivitySerializer(serializers.ModelSerializer):
    destination_name = serializers.CharField(source='destination.name', read_only=True)
    place_name = serializers.CharField(source='place.name', read_only=True)

    class Meta:
        model = Activity
        fields = [
            'id', 'name', 'description', 'destination', 'destination_name',
            'place', 'place_name', 'price', 'image'
        ]
