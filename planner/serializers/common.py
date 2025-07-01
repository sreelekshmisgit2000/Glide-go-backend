from rest_framework import serializers
from planner.models import (
    BudgetRange,
    DaysOption,
    MembersOption,
    ChildrenOption,
    RoomsOption
)


# ───────────────────────────── BUDGET RANGE ─────────────────────────────
class BudgetRangeSerializer(serializers.ModelSerializer):
    class Meta:
        model = BudgetRange
        fields = ['id', 'min_price', 'max_price']


# ───────────────────────────── DAYS OPTION ─────────────────────────────
class DaysOptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = DaysOption
        fields = ['id', 'value']


# ───────────────────────────── MEMBERS OPTION ─────────────────────────────
class MembersOptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = MembersOption
        fields = ['id', 'value']


# ───────────────────────────── CHILDREN OPTION ─────────────────────────────
class ChildrenOptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChildrenOption
        fields = ['id', 'value']


# ───────────────────────────── ROOMS OPTION ─────────────────────────────
class RoomsOptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = RoomsOption
        fields = ['id', 'value']
