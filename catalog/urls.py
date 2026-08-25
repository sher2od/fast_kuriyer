from rest_framework.routers import DefaultRouter

from .views import (
    CategoryViewSet,
    ProductViewSet,
    ProductStockViewSet,
)


router = DefaultRouter()

router.register("categories", CategoryViewSet, basename="category")
router.register("products", ProductViewSet, basename="product")
router.register(
    "product-stocks",
    ProductStockViewSet,
    basename="product-stock"
)

urlpatterns = router.urls


