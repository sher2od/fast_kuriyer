from rest_framework.viewsets import ModelViewSet
from rest_framework.exceptions import PermissionDenied
from rest_framework.response import Response
from rest_framework import status
from drf_spectacular.utils import extend_schema

from .models import Cart,CartItem
from .serializers import CartSerializer,CartItemSerializer
from users.permissions import IsAuthenticatedUser

@extend_schema(
    tags=["Cart"],
    responses=CartSerializer,
    request=CartSerializer,
)
class CartViewSet(ModelViewSet):
    serializer_class = CartSerializer
    permission_classes = [IsAuthenticatedUser]

    def get_queryset(self):
        return Cart.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
        

@extend_schema(
    tags=["Cart Item"],
    responses=CartItemSerializer,
    request=CartItemSerializer,
)

class CartItemViewSet(ModelViewSet):
    serializer_class = CartItemSerializer
    permission_classes = [IsAuthenticatedUser]

    def get_queryset(self):
        return CartItem.objects.filter(
            cart__user=self.request.user
        )

    def perform_create(self, serializer):
        cart = serializer.validated_data["cart"]

        if cart.user != self.request.user:
            raise PermissionDenied(
                "Bu cart sizniki emass"
            )

        serializer.save()