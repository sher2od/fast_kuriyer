from django.db import transaction

from rest_framework import mixins, viewsets
from rest_framework.viewsets import ReadOnlyModelViewSet
from rest_framework.exceptions import ValidationError
from drf_spectacular.utils import extend_schema

from .models import Order, OrderItem

from .serializers import (
    OrderSerializer,
    OrderItemSerializer,
    OrderStatusHistorySerializer,
)
from cart.models import Cart
from users.permissions import IsAuthenticatedUser


@extend_schema(
    tags=["Order"],
    responses=OrderSerializer,
    request=OrderSerializer,
)
class OrderViewSet(
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    viewsets.GenericViewSet,
):
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticatedUser]

    def get_queryset(self):
        return Order.objects.filter(
            user=self.request.user
        )

    @transaction.atomic
    def perform_create(self, serializer):
        cart = Cart.objects.filter(
            user=self.request.user
        ).first()

        if not cart:
            raise ValidationError(
                "Sizda savat mavjud emas."
            )

        cart_items = cart.items.select_related("product")

        if not cart_items.exists():
            raise ValidationError(
                "Savat bo'sh."
            )

        order = serializer.save(
            user=self.request.user,
            store=cart.store,
            status=Order.Status.CREATED,
        )

        for item in cart_items:
            OrderItem.objects.create(
                order=order,
                product=item.product,
                quantity=item.quantity,
            )

        cart_items.delete()

@extend_schema( 
    tags=["Order Item"], 
    responses=OrderItemSerializer, 
    request=OrderItemSerializer, 
)
class OrderItemViewSet(
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    viewsets.GenericViewSet
   ):
    serializer_class = OrderItemSerializer
    permission_classes = [IsAuthenticatedUser]

    def get_queryset(self):
        return OrderItem.objects.filter(
            order__user=self.request.user
        )


@extend_schema(
    tags=["Order Status History"],
    responses=OrderStatusHistorySerializer,
)
class OrderStatusHistoryViewSet(ReadOnlyModelViewSet):
    serializer_class = OrderStatusHistorySerializer
    permission_classes = [IsAuthenticatedUser]

    def get_queryset(self):
        return OrderStatusHistory.objects.filter(
            order__user=self.request.user
        )