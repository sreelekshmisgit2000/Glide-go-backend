from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import ListAPIView, RetrieveAPIView
from .models import *
from .serializers import *
from django.shortcuts import get_object_or_404

# --- Plans ---

class PlanView(APIView):
    def post(self, request):
        serializer = PlanSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Plan saved successfully!'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request):
        plans = Plan.objects.prefetch_related('hotels', 'activities', 'cabs').all()
        serializer = PlanSerializer(plans, many=True)
        return Response(serializer.data)

class PlanDetailView(RetrieveAPIView):
    queryset = Plan.objects.prefetch_related('hotels', 'activities', 'cabs').all()
    serializer_class = PlanSerializer
    lookup_field = 'plan_id'


# --- Hotels ---

class ApprovedHotelsView(ListAPIView):
    queryset = Hotel.objects.filter(is_approved=True)
    serializer_class = HotelSerializer


# --- Activities ---

class ActivityListView(ListAPIView):
    queryset = Activity.objects.all()
    serializer_class = ActivitySerializer


# --- Cabs ---

class VerifiedCabListView(ListAPIView):
    queryset = Cab.objects.filter(is_verified=True)
    serializer_class = CabSerializer

from rest_framework.generics import ListAPIView
from .serializers import HotelCategorySerializer, RoomTypeSerializer, DocumentTypeSerializer, ActivityTypeSerializer

class HotelCategoryListView(ListAPIView):
    queryset = HotelCategory.objects.all()
    serializer_class = HotelCategorySerializer

class RoomTypeListView(ListAPIView):
    queryset = RoomType.objects.all()
    serializer_class = RoomTypeSerializer

class DocumentTypeListView(ListAPIView):
    queryset = DocumentType.objects.all()
    serializer_class = DocumentTypeSerializer

class ActivityTypeListView(ListAPIView):
    queryset = ActivityType.objects.all()
    serializer_class = ActivityTypeSerializer