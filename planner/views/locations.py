from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from planner.models import Location
from ..serializers import LocationListSerializer
from ..permissions import CanView_Location

class LocationViewSet(viewsets.ModelViewSet):
    queryset = Location.objects.all()
    serializer_class = LocationListSerializer
    permission_classes = [CanView_Location,IsAuthenticated]


    def list(self, request, *args, **kwargs):
        user = request.user
        role_names = [group.name for group in user.groups.all()]
        if 'Staff' in role_names:
            return Response({"detail": "Staff users are not allowed to view locations."},
                            status=status.HTTP_403_FORBIDDEN)
        return super().list(request, *args, **kwargs)
