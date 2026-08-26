from rest_framework import serializers

from .models import Category,Product,ProductStock

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields  = [
            "id",
            "name",
            "parent",
        ]
        
        read_only_fields = ["id"]
        

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = [
            "id",
            "name",
            "description",
            "price",
            "discount_price",
            "unit",
            "image_url",
            "category",
        ]

        read_only_fields = ["id"]
        
        
class ProductStockSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductStock
        fields  = [
            "id",
            "product",
            "store",
            "quantity",
        ]
        
        read_only_fields = ["id"]
        
        



