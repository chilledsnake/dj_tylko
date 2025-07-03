from rest_framework import routers

from api.v1.cart.endpoints import CartViewSet

router = routers.SimpleRouter()
router.register(r"", CartViewSet, basename="cart")

urlpatterns = router.urls
