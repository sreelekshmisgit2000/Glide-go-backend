from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from planner.models import Destination
from planner.serializers.destination import (
    DestinationWriteSerializer, DestinationListSerializer, DestinationDetailSerializer
)
from planner.permissions import (
    CanView_Destination, CanAdd_Destination, CanChange_Destination, CanDelete_Destination
)

class DestinationViewSet(viewsets.ModelViewSet):
    queryset = Destination.objects.all().order_by('-created_at')
    lookup_field = 'id'

    def get_serializer_class(self):
        if self.action == 'list':
            return DestinationListSerializer
        elif self.action == 'retrieve':
            return DestinationDetailSerializer
        return DestinationWriteSerializer

    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            return [CanView_Destination(),IsAuthenticated()]
        elif self.action == 'create':
            return [CanAdd_Destination(),IsAuthenticated()]
        elif self.action in ['update', 'partial_update']:
            return [CanChange_Destination()]
        elif self.action == 'destroy':
            return [CanDelete_Destination()]
        return [IsAuthenticated()]
