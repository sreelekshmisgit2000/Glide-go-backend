from django.contrib.auth.models import Group, Permission
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.models import Group, Permission
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class RoleListView(APIView):
    """
    GET /roles/
    Returns all roles with their assigned permissions.
    """
    def get(self, request):
        roles = Group.objects.all()
        data = []
        for role in roles:
            data.append({
                "id": role.id,
                
                "name": role.name,
                "permissions": sorted([
                    f"{perm.content_type.app_label}.{perm.codename}"
                    for perm in role.permissions.all()
                ])
            })
        return Response(data)


class RoleCreateUpdateView(APIView):

    def post(self, request):
        name = request.data.get("name")
        permissions = request.data.get("permissions", [])
        


        if not name:
            return Response({"detail": "Role name is required"}, status=400)

        group, created = Group.objects.get_or_create(name=name)

        # Resolve permission codes
        valid_perms = []
        invalid = []
        for code in permissions:
            if "." in code:
                app_label, codename = code.split(".", 1)
                try:
                    perm = Permission.objects.get(content_type__app_label=app_label, codename=codename)
                    valid_perms.append(perm)
                except Permission.DoesNotExist:
                    invalid.append(code)
            else:
                invalid.append(code)

        if invalid:
            return Response({"detail": "Invalid permission(s)", "invalid": invalid}, status=400)

        group.permissions.set(valid_perms)

        return Response({
            "name": group.name,
            "permissions": sorted([
                f"{p.content_type.app_label}.{p.codename}" for p in group.permissions.all()
            ]),
            "created": created,
        }, status=201 if created else 200)


class RoleDeleteView(APIView):
    """
    DELETE /roles/
    {
      "name": "Planner"
    }
    Deletes a role (group) by name.
    """
    def delete(self, request):
        print(request.data)
        name = request.data.get("name")
        name=int(name)
        if not name:
            return Response({"detail": "Role name is required"}, status=400)

        try:
            group = Group.objects.get(id=name)
            group.delete()
            return Response({"detail": f"Role '{name}' deleted."}, status=200)
        except Group.DoesNotExist:
            return Response({"detail": f"Role '{name}' not found."}, status=404)


class PermissionListView(APIView):
    """
    GET /permissions/
    Returns all permission codes in the system.
    """
    def get(self, request):
        perms = Permission.objects.all()
        data = sorted([f"{p.content_type.app_label}.{p.codename}" for p in perms])
        return Response(data)


from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth.models import User

class UserListWithRolesView(APIView):
    """
    GET /users-with-roles/
    Returns a list of all users with their ID, username, and associated roles.
    """

    def get(self, request):
        users = User.objects.all()
        data = []
        for user in users:
            data.append({
                "id": user.id,
                "username": user.username,
                "roles": [group.name for group in user.groups.all()]
            })
        return Response(data)
    


class RolePermissionsView(APIView):


    def get(self, request, role_id):
        try:
            group = Group.objects.get(id=role_id)
        except Group.DoesNotExist:
            return Response({"detail": "Role not found"}, status=404)

        permissions = group.permissions.all()
        permission_codes = [
            f"{p.content_type.app_label}.{p.codename}" for p in permissions
        ]
        return Response({
            "id": group.id,
            "name": group.name,
            "permissions": permission_codes,
        })

    def put(self, request, role_id):
        permissions = request.data.get("permissions", [])
        print(permissions)
        try:
            group = Group.objects.get(id=role_id)
        except Group.DoesNotExist:
            return Response({"detail": "Role not found"}, status=404)

        valid_perms = []
        invalid_perms = []

        for code in permissions:
            if "." not in code:
                invalid_perms.append(code)
                continue
            app_label, codename = code.split(".", 1)
            try:
                perm = Permission.objects.get(
                    content_type__app_label=app_label,
                    codename=codename
                )
                valid_perms.append(perm)
            except Permission.DoesNotExist:
                invalid_perms.append(code)

        if invalid_perms:
            return Response(
                {"detail": "Invalid permission(s)", "invalid": invalid_perms},
                status=400
            )

        group.permissions.set(valid_perms)
        return Response({
            "detail": f"Permissions updated for role '{group.name}'.",
            "permissions": [f"{p.content_type.app_label}.{p.codename}" for p in valid_perms]
        }, status=200)


from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .serializers import RoleSerializer
from django.contrib.auth.models import Permission

class RoleListCreateView(APIView):
    """
    GET: List all roles
    POST: Create a new role with permissions
    """

    def get(self, request):
        roles = Group.objects.all()
        data = []
        for role in roles:
            data.append({
                "id": role.id,
                "name": role.name,
                "permissions": [p.codename for p in role.permissions.all()],
                "user_count": role.users.count() if hasattr(role, 'users') else 0
            })
        return Response(data)

    def post(self, request):
        name = request.data.get("name")
        permissions = request.data.get("permissions", [])

        if not name:
            return Response({"error": "Role name is required"}, status=status.HTTP_400_BAD_REQUEST)

        role = Group.objects.create(name=name)

        # Filter only valid permissions (skip any junk)
        valid_perms = Permission.objects.filter(codename__in=[
            p.split(".")[1] if "." in p else p for p in permissions
        ])
        role.permissions.set(valid_perms)
        role.save()

        return Response({
            "id": role.id,
            "name": role.name,
            "permissions": [p.codename for p in valid_perms]
        }, status=status.HTTP_201_CREATED)



class RoleDeleteByIdView(APIView):
    """
    DELETE /roles/<int:role_id>/
    Deletes a role (group) by ID.
    """
    def delete(self, request, role_id):
        try:
            group = Group.objects.get(id=role_id)
            group.delete()
            return Response({"detail": f"Role with ID {role_id} deleted."}, status=status.HTTP_200_OK)
        except Group.DoesNotExist:
            return Response({"detail": f"Role with ID {role_id} not found."}, status=status.HTTP_404_NOT_FOUND)



class AssignUserToSingleRoleView(APIView):
    """
    POST /assign-role/
    {
        "user_id": 2,
        "role_id": 1
    }
    Assigns a user to only the given role (replaces any existing ones).
    """
    def post(self, request):
        user_id = request.data.get("user_id")
        role_id = request.data.get("role_id")

        if not user_id or not role_id:
            return Response({"detail": "Both 'user_id' and 'role_id' are required."}, status=400)

        try:
            user = User.objects.get(id=user_id)
        except User.DoesNotExist:
            return Response({"detail": f"User with id {user_id} not found."}, status=404)

        try:
            group = Group.objects.get(id=role_id)
        except Group.DoesNotExist:
            return Response({"detail": f"Role with id {role_id} not found."}, status=404)

        # Remove all roles from the user first
        user.groups.clear()
        # Assign the selected one
        user.groups.add(group)
        print(f"User '{user.username}' assigned to role '{group.name}'.")
        ## also anothe rprint function to show all the pemrissions in that group
        print(group.permissions.all())


        return Response({
            "detail": f"User '{user.username}' assigned to role '{group.name}'.",
            "user_id": user.id,
            "role": group.name
        }, status=200)
