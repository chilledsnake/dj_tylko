from rest_framework import routers

from api.v1.order.endpoints import OrderViewSet

router = routers.SimpleRouter()
router.register(r"", OrderViewSet, basename="order")

urlpatterns = router.urls
