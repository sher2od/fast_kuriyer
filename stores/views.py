from rest_framework.viewsets import ModelViewSet
from drf_spectacular.utils import extend_schema


from .models import Store
from .serializers import StoreSerializer
from users.permissions import IsAdminRole,IsAuthenticatedUser


@extend_schema(
    tags=["Store"],
    responses=StoreSerializer,
    request=StoreSerializer
    )
class StoreViewSet(ModelViewSet):
    serializer_class = StoreSerializer

    def get_queryset(self):
        return Store.objects.filter(is_active=True)

    def get_permissions(self):
        if self.action in ["create", "update", "partial_update", "destroy"]:
            return [IsAdminRole()]

        return [IsAuthenticatedUser()]
    

    
    
    
    
