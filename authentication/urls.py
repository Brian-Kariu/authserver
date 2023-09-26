from django.urls import include, path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)
from .views import UserRegistrationView, user_login, user_logout, HomePageView, GroupViewSet
from rest_framework import routers

router = routers.SimpleRouter()
router.register(r"register", UserRegistrationView)
router.register(r"groups", GroupViewSet)

urlpatterns = [
    path("token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("token/verify/", TokenVerifyView.as_view(), name="token_verify"),
    path("login/", user_login, name="login"),
    path("logout/", user_logout, name="logout"),
    path("home/", HomePageView.as_view(), name="home"),
    path("", include(router.urls)),
]
