from rest_framework import serializers
from planner.models import Destination
from ..models import CabCategory,Location,Country



# ────────────────────────── BASIC ──────────────────────────
class DestinationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Destination
        fields = '__all__'


# ────────────────────────── WRITE ──────────────────────────

class DestinationWriteSerializer(serializers.ModelSerializer):
    country = serializers.PrimaryKeyRelatedField(queryset=Country.objects.all())
    location = serializers.PrimaryKeyRelatedField(queryset=Location.objects.all())
    category = serializers.PrimaryKeyRelatedField(queryset=CabCategory.objects.all())

    class Meta:
        model = Destination
        fields = '__all__'


# ────────────────────────── LIST ──────────────────────────
class DestinationListSerializer(serializers.ModelSerializer):
    thumbnail_url = serializers.ImageField(source='thumbnail', read_only=True)

    class Meta:
        model = Destination
        fields = [
            'id',
            'name',
            'country',
            'description',
            'location',
            'category',
            'thumbnail_url',
            'latitude',
            'longitude',
            'created_at',
        ]


# ────────────────────────── DETAIL ──────────────────────────
class DestinationDetailSerializer(serializers.ModelSerializer):
    thumbnail_url = serializers.ImageField(source='thumbnail', read_only=True)

    class Meta:
        model = Destination
        depth = 0
        fields = [
            'id',
            'name',
            'description',
            'country',
            'location',
            'category',
            'latitude',
            'longitude',
            'thumbnail',
            'thumbnail_url',
            'created_at',
        ]
