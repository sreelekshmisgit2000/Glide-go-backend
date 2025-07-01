from rest_framework import viewsets, status
from rest_framework.response import Response
from planner.models import Hotel
from ..serializers import HotelListSerializer
from planner.permissions import (
    CanView_Hotel, CanAdd_Hotel, CanChange_Hotel, CanDelete_Hotel
)
from rest_framework.permissions import IsAuthenticated


class HotelViewSet(viewsets.ModelViewSet):
    queryset = Hotel.objects.all()
    serializer_class = HotelListSerializer

    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            return [CanView_Hotel()]
        elif self.action == 'create':
            return [CanAdd_Hotel()]
        elif self.action in ['update', 'partial_update']:
            return [CanChange_Hotel()]
        elif self.action == 'destroy':
            return [CanDelete_Hotel()]
        return [IsAuthenticated()]
