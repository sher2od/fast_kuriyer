from django.urls import path
from rest_framework.routers import DefaultRouter

from .views import (
    RegisterView,
    LoginView,
    ProfileView,
    AddressViewSet,
    EmployeeCreateView
)

urlpatterns = [
    path("register/", RegisterView.as_view(), name="register"),
    path("login/", LoginView.as_view(), name="login"),
    path("profile/", ProfileView.as_view(), name="profile"),
    path("employees/create/", EmployeeCreateView.as_view(), name="employee-create"),
]

router = DefaultRouter()
router.register("addresses", AddressViewSet, basename="address")

urlpatterns += router.urls