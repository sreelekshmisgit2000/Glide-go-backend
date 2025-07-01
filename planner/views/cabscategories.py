# planner/views.py
from rest_framework import viewsets
from models import CabCategory
from serializers.cabscategories import (
    CabCategoryWriteSerializer,
    CabCategoryListSerializer,
    CabCategoryDetailSerializer,
)
from rest_framework.permissions import IsAuthenticated, DjangoModelPermissions
from ..permissions import CanView_CabcategorY, CanAdd_CabcategorY, CanChange_CabcategorY, CanDelete_CabcategorY


class CabCategoryViewSet(viewsets.ModelViewSet):
    queryset = CabCategory.objects.all()
    lookup_field = 'id'

    def initial(self, request, *args, **kwargs):
        """Debug permission and user info on every request."""
        user = request.user
        print(f"\n🔐 User: {user}")
        print(f"📛 Is Authenticated: {user.is_authenticated}")
        print(f"🧾 Permissions: {user.get_all_permissions()}\n")
        return super().initial(request, *args, **kwargs)

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

    def get_serializer_class(self):
        if self.action == 'list':
            return CabCategoryListSerializer
        elif self.action == 'retrieve':
            return CabCategoryDetailSerializer
        return CabCategoryWriteSerializer
