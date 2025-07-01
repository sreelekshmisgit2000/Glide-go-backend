from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from planner.models import Driver
from ..serializers import DriverListSerializer
from ..permissions import (
    CanView_Driver, CanAdd_Driver, CanChange_Driver, CanDelete_Driver
)

class DriversViewSet(viewsets.ModelViewSet):
    queryset = Driver.objects.all()
    serializer_class = DriverListSerializer

    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            return [IsAuthenticated(), CanView_Driver()]
        elif self.action == 'create':
            return [IsAuthenticated(), CanAdd_Driver()]
        elif self.action in ['update', 'partial_update']:
            return [IsAuthenticated(), CanChange_Driver()]
        elif self.action == 'destroy':
            return [IsAuthenticated(), CanDelete_Driver()]
        return [IsAuthenticated()]
