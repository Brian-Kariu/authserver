from rest_framework import serializers
from .models import AuthUser
from django.contrib.auth.models import Permission, Group


class AuthUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = AuthUser
        fields = ("username", "email", "password")
        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data):
        user = AuthUser.objects.create(**validated_data)
        user.set_password(validated_data["password"])
        user.save()
        return user


class PermissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Permission
        fields = (
            "id",
            "name",
            "codename",
        )


class GroupSerializer(serializers.ModelSerializer):
    permissions = PermissionSerializer(many=True, read_only=True)

    class Meta:
        model = Group
        fields = (
            "id",
            "name",
            "permissions",
        )

    def update(self, instance, validated_data):
        permission_ids = validated_data.pop("permission_ids")
        instance.permissions.set(permission_ids)
        return super().update(instance, validated_data)


class CreateGroupSerializer(serializers.ModelSerializer):
    permissions = PermissionSerializer(many=True, read_only=True)
    permission_ids = serializers.PrimaryKeyRelatedField(many=True, write_only=True, queryset=Permission.objects.all())

    class Meta:
        model = Group
        fields = (
            "id",
            "name",
            "permissions",
            "permission_ids",
        )

    def create(self, validated_data):
        permission_ids = validated_data.pop("permission_ids")
        group = Group.objects.create(**validated_data)
        group.permissions.set(permission_ids)
        return group
