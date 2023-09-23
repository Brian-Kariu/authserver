from rest_framework import serializers
from .models import AuthUser 


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
