from rest_framework.routers import DefaultRouter

from .views import (
    OrderViewSet,
    OrderItemViewSet,
    OrderStatusHistoryViewSet,
)

router = DefaultRouter()

router.register("orders", OrderViewSet, basename="order")
router.register("order-items", OrderItemViewSet, basename="order-item")
router.register(
    "order-status-history",
    OrderStatusHistoryViewSet,
    basename="order-status-history",
)

urlpatterns = router.urls