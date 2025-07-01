# urls.py  (project-level or app-level)
from django.urls import path
from django.http import HttpResponse

from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework_simplejwt import views as jwt_views
from .views import AssignUserToSingleRoleView, RoleListCreateView, RolePermissionsView,UserListWithRolesView,PermissionListView,RoleCreateUpdateView,RoleDeleteView,RoleListView
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)

urlpatterns = [
     path('', lambda request: HttpResponse("Welcome to GlideGo Users")),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
path('permissions/', PermissionListView.as_view(), name='permission-list'),
path('roles/', RoleListView.as_view(), name='role-list'),
path('roles/create-update/', RoleCreateUpdateView.as_view(), name='role-create-update'),
path('roles/delete/', RoleDeleteView.as_view(), name='role-delete'),
path('users-with-roles/', UserListWithRolesView.as_view(), name='users-with-roles'),
path('roles/<int:role_id>/permissions/', RolePermissionsView.as_view(), name='role-permissions'),
   path("roles-add/", RoleListCreateView.as_view(), name="roles"),
  path("assign-role/", AssignUserToSingleRoleView.as_view(), name="assign-user-to-role"),  # ✅ Updated view
]
