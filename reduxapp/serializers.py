from rest_framework import serializers
from .models import (
    Plan, Hotel, Amenity, Activity, HotelDocument,
    Driver, Cab
)
from .models import (
    HotelCategory, RoomType, DocumentType, ActivityType
)

# ---------- Classifier Serializers ----------

class HotelCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = HotelCategory
        fields = ['id', 'name']

class RoomTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = RoomType
        fields = ['id', 'name']

class DocumentTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = DocumentType
        fields = ['id', 'name', 'description']

class ActivityTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ActivityType
        fields = ['id', 'name', 'description']

# ---------- Core Serializers ----------

class AmenitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Amenity
        fields = ['id', 'name']

class ActivitySerializer(serializers.ModelSerializer):
    activity_type = ActivityTypeSerializer()

    class Meta:
        model = Activity
        fields = ['id', 'name', 'activity_type', 'latitude', 'longitude']

class HotelDocumentSerializer(serializers.ModelSerializer):
    document_type = DocumentTypeSerializer()

    class Meta:
        model = HotelDocument
        fields = ['id', 'document_type', 'file']

class HotelSerializer(serializers.ModelSerializer):
    category = HotelCategorySerializer()
    room_type = RoomTypeSerializer()
    amenities = AmenitySerializer(many=True)
    activities = ActivitySerializer(many=True)
    documents = HotelDocumentSerializer(many=True, read_only=True)

    class Meta:
        model = Hotel
        fields = [
            'id', 'name', 'category', 'room_type',
            'amenities', 'activities', 'latitude',
            'longitude', 'is_approved', 'documents'
        ]

class DriverSerializer(serializers.ModelSerializer):
    class Meta:
        model = Driver
        fields = ['id', 'name', 'license_doc', 'id_proof_doc', 'address_proof_doc']

class CabSerializer(serializers.ModelSerializer):
    driver = DriverSerializer()

    class Meta:
        model = Cab
        fields = [
            'id', 'vehicle_number', 'rc_doc',
            'permit_doc', 'insurance_doc', 'driver',
            'is_verified'
        ]

class PlanSerializer(serializers.ModelSerializer):
    hotels = HotelSerializer(many=True, read_only=True)
    activities = ActivitySerializer(many=True, read_only=True)
    cabs = CabSerializer(many=True, read_only=True)

    class Meta:
        model = Plan
        fields = [
            'id', 'plan_id', 'theme', 'hotels',
            'activities', 'cabs', 'created_at'
        ]