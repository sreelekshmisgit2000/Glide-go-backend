# apps/authentication/serializers.py
from rest_framework_simplejwt.serializers import (
    TokenObtainPairSerializer,
    TokenRefreshSerializer,
)
from rest_framework_simplejwt.tokens       import RefreshToken
from rest_framework import serializers

class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    """
    Extends the default serializer so we can:
      • add custom user claims
      • shape the JSON response however we like
    """

    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        # ─── custom claims ───
        token["username"]  = user.username
        token["is_admin"]  = user.is_staff
        token["full_name"] = user.get_full_name()
        return token

    def validate(self, attrs):
        data = super().validate(attrs)

        # Add anything else you want returned at login time
        data.update(
            {
                "user_id": self.user.id,
                "email":   self.user.email,
                # e.g. put all roles/permissions in one go
                "permissions": list(self.user.get_all_permissions()),
            }
        )
        return data


class CustomTokenRefreshSerializer(TokenRefreshSerializer):
    """
    Lets us inject additional info when the client swaps a refresh
    token for a new access token.
    """

    def validate(self, attrs):
        data = super().validate(attrs)

        # You still have self.context["request"].user == Anonymous
        # so you can’t add user-specific info here.  But you *can*
        # add static metadata or a new refresh token.
        data["token_type"] = "access"
        return data

# In your Role serializer or view
from django.contrib.auth.models import Group

class RoleSerializer(serializers.ModelSerializer):
    user_count = serializers.SerializerMethodField()

    class Meta:
        model = Group
        fields = ['id', 'name', 'permissions', 'user_count']

    def get_user_count(self, obj):
        return obj.user_set.count()
