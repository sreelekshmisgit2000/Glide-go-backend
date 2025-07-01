from rest_framework import generics, viewsets
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.permissions import IsAuthenticated
from planner.models import (
    DriverImage, VehicleImage, Driver, Vehicle, PlaceImage, Place
)
from planner.serializers.place import PlaceImageGroupedByPlaceSerializer, PlaceImageSerializer
from ..serializers.driver_images import DriverImageGroupedSerializer,DriverImageSerializer
from ..serializers.vehicles import VehicleImageGroupedByVehicleSerializer,VehicleImageSerializer
from rest_framework.response import Response
from ..permissions import CanView_DriverImagesGroup,CanView_Vehicleimage,CanView_Placeimage



# DRIVER IMAGES
class DriverImageListCreateView(generics.ListCreateAPIView):
    queryset = DriverImage.objects.all()
    serializer_class = DriverImageGroupedSerializer
    parser_classes = [MultiPartParser, FormParser]
    permission_classes = [IsAuthenticated,CanView_DriverImagesGroup]


    def post(self, request, *args, **kwargs):
        files = request.FILES.getlist('images')
        driver_id = request.data.get('driver')
        images = [DriverImage(driver_id=driver_id, image=f) for f in files]
        DriverImage.objects.bulk_create(images)
        return Response(DriverImageGroupedSerializer(images, many=True).data)

class DriverImageDeleteView(generics.DestroyAPIView):
    queryset = DriverImage.objects.all()
    serializer_class = DriverImageSerializer

class DriverImageGroupedView(generics.ListAPIView):
    queryset = Driver.objects.prefetch_related('images')
    serializer_class = DriverImageGroupedSerializer
    permission_classes = [IsAuthenticated,CanView_DriverImagesGroup]


# VEHICLE IMAGES
class VehicleImageViewSet(viewsets.ModelViewSet):
    queryset = VehicleImage.objects.all()
    serializer_class = DriverImageSerializer
    parser_classes = [MultiPartParser, FormParser]
    permission_classes = [IsAuthenticated,CanView_Vehicleimage]
    lookup_field = 'pk'

class VehicleImageGroupedViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Vehicle.objects.prefetch_related('images').all()
    serializer_class = VehicleImageGroupedByVehicleSerializer
    permission_classes = [IsAuthenticated,CanView_Vehicleimage]

class VehicleImageDeleteView(generics.DestroyAPIView):
    queryset = VehicleImage.objects.all()
    serializer_class = VehicleImageSerializer
    permission_classes = [IsAuthenticated,CanView_Vehicleimage]
    lookup_field = 'pk'

# PLACE IMAGES
