from rest_framework.viewsets import ModelViewSet
from drf_spectacular.utils import extend_schema

from .models import Category,Product,ProductStock
from .serializers import CategorySerializer,ProductSerializer,ProductStockSerializer
from users.permissions import IsAdminRole,IsAuthenticatedUser

@extend_schema(
    tags=["Category"],
    responses=CategorySerializer,
    request=CategorySerializer
    )
class CategoryViewSet(ModelViewSet):
    serializer_class = CategorySerializer

    def get_queryset(self):
        return Category.objects.filter(is_active=True)
        #return Category.objects.all()
    

    def get_permissions(self):
        if self.action in ["create", "update", "partial_update", "destroy"]:
            return [IsAdminRole()]

        return [IsAuthenticatedUser()]


@extend_schema(
    tags=["Product"],
    responses=ProductSerializer,
    request=ProductSerializer
    )
class ProductViewSet(ModelViewSet):
    serializer_class = ProductSerializer
    
    def get_queryset(self):
        return Product.objects.filter(is_active=True)
    
    def get_permissions(self):
        if self.action in ["create", "update", "partial_update", "destroy"]:
            return [IsAdminRole()]

        return [IsAuthenticatedUser()]  
    
    
    
    
@extend_schema(
    tags=["Product Stock"],
    responses=ProductStockSerializer,
    request=ProductStockSerializer,
)
class ProductStockViewSet(ModelViewSet):
    serializer_class = ProductStockSerializer

    def get_queryset(self):
        return ProductStock.objects.all()

    def get_permissions(self):
        if self.action in [
            "create",
            "update",
            "partial_update",
            "destroy",
        ]:
            return [IsAdminRole()]

        return [IsAuthenticatedUser()]