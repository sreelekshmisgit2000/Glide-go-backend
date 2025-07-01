# planner/views/vehicles.py
from rest_framework import viewsets
from planner.models import Vehicle
from planner.permissions import CanView_Vehicle
from ..serializers.vehicles import (
    VehicleWriteSerializer,
    VehicleListSerializer,
    VehicleDetailSerializer
)
from ..permissions import (
    CanView_Vehicle, CanAdd_Vehicle, CanChange_Vehicle, CanDelete_Vehicle
)
from rest_framework.permissions import IsAuthenticated

class VehicleViewSet(viewsets.ModelViewSet):
    queryset = Vehicle.objects.all()

    def get_serializer_class(self):
        if self.action == 'list':
            return VehicleListSerializer
        elif self.action == 'retrieve':
            return VehicleDetailSerializer
        return VehicleWriteSerializer
    
    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            return [CanView_Vehicle()]
        elif self.action == 'create':
            return [CanAdd_Vehicle()]
        elif self.action in ['update', 'partial_update']:
            return [CanChange_Vehicle()]
        elif self.action == 'destroy':
            return [CanDelete_Vehicle()]
        return [IsAuthenticated()]
