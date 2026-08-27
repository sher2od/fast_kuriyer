from rest_framework import serializers

from .models import Order, OrderItem, OrderStatusHistory


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = [
            "id",
            "user",
            "store",
            "address",
            "status",
            "total_price",
            "created_at",
        ]
        read_only_fields = [
            "id",
            "user",
            "status",
            "total_price",
            "created_at",
        ]


class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = [
            "id",
            "order",
            "product",
            "quantity",
            "price_at_order"
        ]
        read_only_fields = [
            "id",
            "price_at_order"
        ]


class OrderStatusHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderStatusHistory
        fields = [
            "id",
            "order",
            "status",
            "changed_at",
        ]
        read_only_fields = [
            "id",
            "status",
            "changed_at",
        ]