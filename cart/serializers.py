from rest_framework import serializers

from .models import Cart,CartItem

class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = [
            "id",
            "user",
            "store",
            "created_at"
        ]
        
        read_only_fields = [
            "id",
            "user",
            "created_at"
        ]
    
class CartItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = CartItem
        fields = [
            "id",
            "cart",
            "product",
            "quantity",
        ]
        read_only_fields = ["id"]