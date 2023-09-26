from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny, IsAdminUser
from django.contrib.auth import login, logout, authenticate
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from rest_framework_simplejwt.tokens import RefreshToken
from .serializers import (
    AuthUserSerializer,
    GroupSerializer,
    CreateGroupSerializer,
    PermissionSerializer,
)
from .models import AuthUser
from rest_framework import permissions
from django.contrib.auth.models import Group, Permission
from rest_framework.decorators import action
from rest_framework import mixins
from rest_framework import viewsets


class UserRegistrationView(
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    viewsets.GenericViewSet,
    generics.CreateAPIView,
):
    queryset = AuthUser.objects.all()
    serializer_class = AuthUserSerializer
    permission_classes = (AllowAny,)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()

        refresh = RefreshToken.for_user(user)
        tokens = {
            "refresh": str(refresh),
            "access": str(refresh.access_token),
        }

        return Response(tokens, status=status.HTTP_201_CREATED)

    @action(
        detail=False,
        methods=["get", "post"],
    )
    def groups(self, request):
        if request.method == "POST":
            # TODO: set user groups
            return Response({})
        return Response(GroupSerializer(Group.objects.filter(user=request.user), many=True).data)

    @action(
        detail=False,
        methods=["get", "post"],
    )
    def permissions(self, request):
        if request.method == "POST":
            # TODO: set user permissions
            return Response({})

        user = request.user
        if user.is_superuser:
            permissions = Permission.objects.all()
        else:
            permissions = list(user.user_permissions.all() | Permission.objects.filter(group__user=user))
        return Response(PermissionSerializer(permissions, many=True).data)


def user_login(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return render(request, "home.html")
        else:
            messages.error(request, "Invalid username or password")

    return render(request, "login.html")


def user_logout(request):
    logout(request)
    return redirect("/login")


class HomePageView(generics.ListAPIView):
    queryset = AuthUser.objects.all()
    serializer_class = AuthUserSerializer

    @login_required
    def home(request):
        return render(request, "home.html")


class GroupViewSet(mixins.ListModelMixin, mixins.CreateModelMixin, viewsets.GenericViewSet):
    """
    Manage user groups
    """

    queryset = Group.objects.all()
    permission_classes = [IsAdminUser]

    def get_serializer_class(self):
        if self.request.method in ["POST", "PUT"]:
            return CreateGroupSerializer
        return GroupSerializer
