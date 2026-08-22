from django.urls import path
from rest_framework.routers import DefaultRouter

from .views import (
    RegisterView,
    LoginView,
    ProfileView,
    AddressViewSet,
)

urlpatterns = [
    path("register/", RegisterView.as_view(), name="register"),
    path("login/", LoginView.as_view(), name="login"),
    path("profile/", ProfileView.as_view(), name="profile"),
]

router = DefaultRouter()
router.register("addresses", AddressViewSet, basename="address")

urlpatterns += router.urls