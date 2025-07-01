from rest_framework import serializers
from planner.models import Place, PlaceImage


# ────────────────────────── PLACE IMAGE ──────────────────────────
class PlaceImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlaceImage
        fields = ['id', 'place', 'image']


# ───────── GROUPED IMAGES: Return images grouped by place ─────────
class PlaceImageGroupedByPlaceSerializer(serializers.ModelSerializer):
    images = PlaceImageSerializer(many=True, read_only=True)

    class Meta:
        model = Place
        fields = ['id', 'name', 'images']




# ─────────────────────────── PLACE WRITE ─────────────────────────
class PlaceWriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Place
        fields = [
            'id', 'destination',
            'name', 'description',
            'latitude', 'longitude',
            'map_link',
        ]


# ─────────────────────────── PLACE LIST ──────────────────────────
class PlaceListSerializer(serializers.ModelSerializer):
    destination_name = serializers.CharField(source='destination.name', read_only=True)

    class Meta:
        model = Place
        fields = [
            'id', 'name', 'destination', 'destination_name',
            'latitude', 'longitude',
        ]


# ────────────────────────── PLACE DETAIL ─────────────────────────
class PlaceDetailSerializer(serializers.ModelSerializer):
    destination_name = serializers.CharField(source='destination.name', read_only=True)
    images = PlaceImageSerializer(many=True, read_only=True)

    class Meta:
        model = Place
        depth = 0
        fields = [
            'id', 'destination', 'destination_name',
            'name', 'description',
            'latitude', 'longitude', 'map_link',
            'images',
        ]


# ────────────────────────── COMPACT ──────────────────────────
class PlaceSerializer(serializers.ModelSerializer):
    destination_name = serializers.CharField(source='destination.name', read_only=True)

    class Meta:
        model = Place
        fields = [
            'id', 'destination', 'destination_name',
            'name', 'description', 'latitude', 'longitude', 'map_link'
        ]
