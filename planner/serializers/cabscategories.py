from rest_framework import serializers
from planner.models import CabCategory

# ────────────────────────── WRITE ──────────────────────────
class CabCategoryWriteSerializer(serializers.ModelSerializer):
    """Used for create & update (POST / PUT / PATCH)."""
    class Meta:
        model = CabCategory
        fields = ['id', 'name', 'description']


# ────────────────────────── LIST ──────────────────────────
class CabCategoryListSerializer(serializers.ModelSerializer):
    """Compact fields for list views."""
    class Meta:
        model = CabCategory
        fields = ['id', 'name', 'description']


# ────────────────────────── DETAIL ──────────────────────────
class CabCategoryDetailSerializer(serializers.ModelSerializer):
    """Full detail view."""
    class Meta:
        model = CabCategory
        depth = 0
        fields = ['id', 'name', 'description']
