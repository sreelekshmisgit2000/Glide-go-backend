from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from planner.models import Place, PlaceImage
from planner.serializers.place import (
    PlaceWriteSerializer, PlaceListSerializer, PlaceDetailSerializer,
    PlaceImageSerializer
)
from planner.permissions import (
    CanView_Place, CanAdd_Place, CanChange_Place, CanDelete_Place,
    CanView_Placeimage, CanAdd_Placeimage, CanChange_Placeimage, CanDelete_Placeimage
)
from rest_framework import generics
from ..serializers.place import PlaceImageGroupedByPlaceSerializer

class PlaceViewSet(viewsets.ModelViewSet):
    queryset = Place.objects.all()
    lookup_field = 'id'

    def get_serializer_class(self):
        if self.action == 'list':
            return PlaceListSerializer
        elif self.action == 'retrieve':
            return PlaceDetailSerializer
        return PlaceWriteSerializer

    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            return [CanView_Place()]
        elif self.action == 'create':
            return [CanAdd_Place()]
        elif self.action in ['update', 'partial_update']:
            return [CanChange_Place()]
        elif self.action == 'destroy':
            return [CanDelete_Place()]
        return [IsAuthenticated()]

class PlaceImageViewSet(viewsets.ModelViewSet):
    queryset = PlaceImage.objects.all()
    serializer_class = PlaceImageSerializer
    lookup_field = 'id'

    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            return [CanView_Placeimage(), IsAuthenticated()]
        elif self.action == 'create':
            return [CanAdd_Placeimage(), IsAuthenticated()]
        elif self.action in ['update', 'partial_update']:
            return [CanChange_Placeimage(), IsAuthenticated()]
        elif self.action == 'destroy':
            return [CanDelete_Placeimage(), IsAuthenticated()]
        return [IsAuthenticated()]
    

class PlaceImagesGroupedView(generics.ListAPIView):
    queryset = Place.objects.prefetch_related('images').all()
    serializer_class = PlaceImageGroupedByPlaceSerializer


