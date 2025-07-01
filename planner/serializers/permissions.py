from rest_framework import serializers
from planner.models import Page
from django.contrib.auth import get_user_model

# ──────────────────────────── PAGE SERIALIZER ────────────────────────────
class PageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Page
        fields = ["id", "code", "name"]


# ─────────────── Assign multiple pages to a user (bulk update) ───────────────
class UserPageSerializer(serializers.Serializer):
    page_ids = serializers.ListField(
        child=serializers.IntegerField(min_value=1),
        allow_empty=True
    )

    def validate_page_ids(self, value):
        # Optional: ensure every page ID exists
        qs = Page.objects.filter(id__in=value)
        if qs.count() != len(value):
            raise serializers.ValidationError("One or more pages do not exist.")
        return value


# ----------- DriverImage Permissions -----------

