# planner/views.py
from rest_framework import viewsets
from ..models import Activity
from ..serializers.activity import (
    ActivityWriteSerializer,
    ActivityListSerializer,
    ActivityDetailSerializer,
)
from ..permissions import (
    CanView_Activity, CanAdd_Activity, CanChange_Activity, CanDelete_Activity
)
from rest_framework.permissions import IsAuthenticated, DjangoModelPermissions

class ActivityViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated, DjangoModelPermissions]
    """
    /api/activities/       → list  + create
    /api/activities/<id>/  → retrieve • update • delete
    """
    queryset = Activity.objects.all().order_by("-id")
    lookup_field = "id"

    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            return [CanView_Activity()]
        elif self.action == 'create':
            return [CanAdd_Activity()]
        elif self.action in ['update', 'partial_update']:
            return [CanChange_Activity()]
        elif self.action == 'destroy':
            return [CanDelete_Activity()]
        return [IsAuthenticated()]

    def get_serializer_class(self):
        if self.action == "list":
            return ActivityListSerializer
        if self.action == "retrieve":
            return ActivityDetailSerializer
        # create / update / partial_update
        return ActivityWriteSerializer
