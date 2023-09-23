from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
from django.contrib.auth import login, logout, authenticate
from django.shortcuts import render, redirect
from django.contrib import messages
from rest_framework_simplejwt.tokens import RefreshToken
from .serializers import AuthUserSerializer 
from .models import AuthUser


class UserRegistrationView(generics.CreateAPIView):
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
