from django.urls import include, path

from api.v1.cart.urls import router as cart_router
from api.v1.order.urls import router as order_router
from api.v1.shelf.urls import router as shelf_router

urlpatterns = [
    path("order/", include(order_router.urls)),
    path("cart/", include(cart_router.urls)),
    path("shelf/", include(shelf_router.urls)),
]
