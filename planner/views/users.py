from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from planner.models import RolePermission

class CurrentUserAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        if user.is_superuser:
            role = "superuser"
        elif user.is_staff:
            role = "staff"
        else:
            role = "user"

        try:
            allowed_pages = RolePermission.objects.get(role=role).allowed_pages
        except RolePermission.DoesNotExist:
            allowed_pages = []

        return Response({
            "id": user.id,
            "username": user.username,
            "email": user.email,
            "is_superuser": user.is_superuser,
            "is_staff": user.is_staff,
            "role": role,
            "allowed_pages": allowed_pages,
        })
