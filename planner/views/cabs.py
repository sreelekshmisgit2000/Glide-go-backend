from rest_framework import viewsets
from planner.models import CabType, Cab, CabCategory
from planner.serializers.cabs import (
    CabListSerializer,
    CabWriteSerializer, CabListSerializer, CabDetailSerializer
)
from planner.serializers.cabscategories import (
    CabCategoryWriteSerializer, CabCategoryListSerializer, CabCategoryDetailSerializer
)
from planner.permissions import (
    CanView_Cabtype, CanAdd_Cabtype, CanChange_Cabtype, CanDelete_Cabtype,
    CanView_CabcategorY, CanAdd_CabcategorY, CanChange_CabcategorY, CanDelete_CabcategorY,
    CanView_Cab
)
from rest_framework.permissions import IsAuthenticated

class CabTypeViewSet(viewsets.ModelViewSet):
    queryset = CabType.objects.all()
    serializer_class = CabListSerializer

    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            return [CanView_Cabtype()]
        elif self.action == 'create':
            return [CanAdd_Cabtype()]
        elif self.action in ['update', 'partial_update']:
            return [CanChange_Cabtype()]
        elif self.action == 'destroy':
            return [CanDelete_Cabtype()]
        return [IsAuthenticated()]

class CabViewSet(viewsets.ModelViewSet):
    queryset = Cab.objects.all()
    lookup_field = 'id'

    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            return [CanView_Cab()]
        elif self.action == 'create':
            return [CanAdd_Cabtype()]
        elif self.action in ['update', 'partial_update']:
            return [CanChange_Cabtype()]
        elif self.action == 'destroy':
            return [CanDelete_Cabtype()]
        return [IsAuthenticated()]

    def get_serializer_class(self):
        if self.action == 'list':
            return CabListSerializer
        if self.action == 'retrieve':
            return CabDetailSerializer
        return CabWriteSerializer

class CabCategoryViewSet(viewsets.ModelViewSet):
    queryset = CabCategory.objects.all()
    lookup_field = 'id'

    def get_serializer_class(self):
        if self.action == 'list':
            return CabCategoryListSerializer
        if self.action == 'retrieve':
            return CabCategoryDetailSerializer
        return CabCategoryWriteSerializer

    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            return [IsAuthenticated(), CanView_CabcategorY()]
        elif self.action == 'create':
            return [IsAuthenticated(), CanAdd_CabcategorY()]
        elif self.action in ['update', 'partial_update']:
            return [IsAuthenticated(), CanChange_CabcategorY()]
        elif self.action == 'destroy':
            return [IsAuthenticated(), CanDelete_CabcategorY()]
        return [IsAuthenticated()]
